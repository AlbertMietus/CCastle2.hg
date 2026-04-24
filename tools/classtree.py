#!/usr/bin/env python3
"""
classtree.py — Static ASCII class-hierarchy viewer for Python packages.

Scans .py source files using AST (no imports, no side effects).
Dynamically created classes (via type(), decorators, etc.) are NOT visible.

Usage:
    python classtree.py <path> [options]

Examples:
    python classtree.py aigr/
    python classtree.py aigr/ --root AigrNode
    python classtree.py aigr/ -m                       # module column
    python classtree.py aigr/ -M                       # show methods
    python classtree.py aigr/ -M -H                    # methods, hide hidden
    python classtree.py aigr/ -m -M -l --orphans
    python classtree.py aigr/ --html                   # HTML output, inline CSS
    python classtree.py aigr/ --html --css external:my.css
    python classtree.py aigr/ --html --css generate:my.css
"""

from __future__ import annotations

import ast
import argparse
import html as html_mod
import sys
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

_NOTABLE_DECORATORS: frozenset[str] = frozenset({
    "property", "staticmethod", "classmethod", "abstractmethod",
    "override", "final",
})

_DECORATOR_ABBREV: dict[str, str] = {
    "property":       "prop",
    "staticmethod":   "static",
    "classmethod":    "cls",
    "abstractmethod": "abstract",
}


@dataclass
class MethodInfo:
    """One method definition extracted from a class body."""
    name: str
    params: str            # parameter string; self/cls already stripped
    decorators: list[str]  # filtered to _NOTABLE_DECORATORS, abbreviated

    def signature(self) -> str:
        """Compact one-liner: 'foo(x, y)  [prop, abstract]'."""
        tags = f"  [{', '.join(self.decorators)}]" if self.decorators else ""
        return f"{self.name}({self.params}){tags}"


@dataclass
class ClassInfo:
    """All statically known information about one class definition."""
    name: str
    qualified_name: str       # module.ClassName  (best effort)
    base_names: list[str]     # raw base names as written in source
    source_file: Path         # absolute path
    rel_file: str             # path relative to scan root
    module_path: str          # dotted module path relative to scan root
    lineno: int
    methods: list[MethodInfo] = field(default_factory=list)

    # Populated during the resolution pass:
    resolved_bases: list[ClassInfo] = field(default_factory=list)
    children: list[ClassInfo]       = field(default_factory=list)
    mixin_bases: list[ClassInfo]    = field(default_factory=list)

    def label(self) -> str:
        """Plain-text display name: 'Foo' or 'Foo  <+Bar, Baz>'."""
        if self.mixin_bases:
            names = ", ".join(b.name for b in self.mixin_bases)
            return f"{self.name}  <+{names}>"
        return self.name

    def __hash__(self) -> int:
        return hash(self.qualified_name)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ClassInfo) and self.qualified_name == other.qualified_name


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------

class SourceScanner:
    """
    Walk a directory tree, parse every .py file with ast, and collect
    ClassInfo objects.  No code is executed.
    """

    def __init__(self, root: Path) -> None:
        self._root = root
        self._base: Path         = root if root.is_dir() else root.parent
        self._by_qualified: dict[str, ClassInfo]       = {}
        self._by_simple:    dict[str, list[ClassInfo]] = defaultdict(list)

    def scan(self) -> list[ClassInfo]:
        """Scan all .py files under root and return a flat list of ClassInfo."""
        for py_file in self._find_sources():
            self._scan_file(py_file)
        self._resolve_bases()
        return list(self._by_qualified.values())

    def _find_sources(self) -> list[Path]:
        if self._root.is_dir():
            return sorted(self._root.rglob("*.py"))
        return [self._root]

    def _scan_file(self, py_file: Path) -> None:
        try:
            source = py_file.read_text(encoding="utf-8", errors="replace")
            tree   = ast.parse(source, filename=str(py_file))
        except SyntaxError as exc:
            print(f"[warning] Syntax error in {py_file}: {exc}", file=sys.stderr)
            return
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                self._register_class(node, py_file)

    def _register_class(self, node: ast.ClassDef, py_file: Path) -> None:
        module_path = self._to_module_path(py_file)
        qualified   = f"{module_path}.{node.name}" if module_path else node.name
        if qualified in self._by_qualified:
            return  # skip re-exports / duplicates
        info = ClassInfo(
            name=node.name,
            qualified_name=qualified,
            base_names=[_unparse_expr(b) for b in node.bases],
            source_file=py_file,
            rel_file=self._to_rel_file(py_file),
            module_path=module_path,
            lineno=node.lineno,
            methods=_extract_methods(node),
        )
        self._by_qualified[qualified] = info
        self._by_simple[node.name].append(info)

    def _resolve_bases(self) -> None:
        """
        Resolve raw base names to ClassInfo references.

        base_names[0]  → primary parent  → added to its .children list
        base_names[1:] → mixin bases     → stored in .mixin_bases only
                                           (NOT added to .children)

        This ensures every class appears exactly once in the rendered tree.
        """
        for info in self._by_qualified.values():
            for index, base_name in enumerate(info.base_names):
                resolved = self._lookup(base_name, info.module_path)
                if resolved is None:
                    continue
                info.resolved_bases.append(resolved)
                if index == 0:
                    resolved.children.append(info)
                else:
                    info.mixin_bases.append(resolved)

    def _lookup(self, name: str, from_module: str) -> ClassInfo | None:
        """
        Resolve a base name to a ClassInfo using three strategies in order:
          1. Exact qualified match    (e.g. 'aigr.base.AigrNode')
          2. Simple name, same module (local definition)
          3. Simple name, unique globally
        """
        if name in self._by_qualified:
            return self._by_qualified[name]
        simple     = name.split(".")[-1]
        candidates = self._by_simple.get(simple, [])
        same       = [c for c in candidates if c.module_path == from_module]
        if same:
            return same[0]
        if len(candidates) == 1:
            return candidates[0]
        return None  # ambiguous or external

    def _to_rel_file(self, py_file: Path) -> str:
        try:
            return str(py_file.relative_to(self._base))
        except ValueError:
            return str(py_file)

    def _to_module_path(self, py_file: Path) -> str:
        try:
            rel = py_file.relative_to(self._base)
        except ValueError:
            rel = py_file
        parts = list(rel.parts)
        if parts and parts[-1].endswith(".py"):
            parts[-1] = parts[-1][:-3]
        if parts and parts[-1] == "__init__":
            parts = parts[:-1]
        return ".".join(parts) if parts else "<root>"


# ---------------------------------------------------------------------------
# AST helpers
# ---------------------------------------------------------------------------

def _unparse_expr(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    return ast.unparse(node)  # Attribute, subscript (Generic[T]), etc.


def _extract_methods(class_node: ast.ClassDef) -> list[MethodInfo]:
    """Collect all direct (non-nested) method definitions from a class body."""
    return [
        _build_method_info(stmt)
        for stmt in class_node.body
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]


def _build_method_info(func: ast.FunctionDef | ast.AsyncFunctionDef) -> MethodInfo:
    return MethodInfo(
        name=func.name,
        params=_params_string(func),
        decorators=_notable_decorators(func),
    )


def _notable_decorators(func: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    """Return abbreviated names of notable decorators, in source order."""
    result: list[str] = []
    for dec in func.decorator_list:
        raw = (dec.id        if isinstance(dec, ast.Name)      else
               dec.attr      if isinstance(dec, ast.Attribute) else "")
        if raw in _NOTABLE_DECORATORS:
            result.append(_DECORATOR_ABBREV.get(raw, raw))
    return result


def _params_string(func: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """
    Parameter list as a compact string:
    - self / cls stripped
    - type annotations omitted
    - *args / **kwargs included if present
    """
    args       = func.args
    positional = list(args.posonlyargs) + list(args.args)
    if positional and positional[0].arg in ("self", "cls"):
        positional = positional[1:]
    names = [a.arg for a in positional]
    if args.vararg:
        names.append(f"*{args.vararg.arg}")
    if args.kwarg:
        names.append(f"**{args.kwarg.arg}")
    return ", ".join(names)


# ---------------------------------------------------------------------------
# Tree building
# ---------------------------------------------------------------------------

class HierarchyForest:
    """Derive roots and orphans from the resolved ClassInfo graph."""

    def __init__(self, classes: list[ClassInfo]) -> None:
        self._all = classes

    def roots(self, filter_root: str | None = None) -> list[ClassInfo]:
        """
        Return top-level nodes (no primary parent in the scanned set).
        If filter_root is given, return only that named node.
        """
        if filter_root:
            return self._find_named_root(filter_root)
        return self._find_all_roots()

    def orphans(self) -> list[ClassInfo]:
        """Classes with no resolved bases AND no children."""
        return [c for c in self._all if not c.resolved_bases and not c.children]

    def _find_named_root(self, name: str) -> list[ClassInfo]:
        matches = [c for c in self._all if c.name == name]
        if not matches:
            raise ValueError(f"Root class '{name}' not found in scanned sources.")
        return matches

    def _find_all_roots(self) -> list[ClassInfo]:
        all_qualified = {c.qualified_name for c in self._all}
        return [
            c for c in self._all
            if not any(
                b.qualified_name in all_qualified
                for b in c.resolved_bases[:1]   # only primary base counts
            )
        ]


# ---------------------------------------------------------------------------
# Sort keys
# ---------------------------------------------------------------------------

def _sort_key(name: str) -> tuple:
    """
    Ordering:  Uppercase-initial  <  lowercase-initial  <  underscore-initial.
    Within each bucket, standard string comparison applies.
    """
    if name.startswith("_"):
        return (2, name.lower())
    if name[0].isupper():
        return (0, name)
    return (1, name)


def _class_sort_key(c: ClassInfo)   -> tuple: return _sort_key(c.name)
def _method_sort_key(m: MethodInfo) -> tuple: return _sort_key(m.name)


# ---------------------------------------------------------------------------
# Intermediate representation shared by all formatters
# ---------------------------------------------------------------------------

_ANN_MODULE = "module"
_ANN_LINENO = "lineno"

# Box-drawing characters
_TEE    = "├── "
_LAST   = "└── "
_INDENT = "│   "
_SPACE  = "    "

_M_TEE  = "├─ "    # lighter connectors used for method lines
_M_LAST = "└─ "


@dataclass
class RenderOptions:
    annotations:  list[str] = field(default_factory=list)
    show_methods: bool = False
    hide_hidden:  bool = False
    sort:         bool = True


@dataclass
class _RawLine:
    """
    One not-yet-formatted output line, collected during the tree walk.
    Formatters consume a list[_RawLine] to produce their final output.
    """
    prefix:     str         # box-drawing characters + connector
    class_node: ClassInfo | None   # set for class lines
    method:     MethodInfo | None  # set for method lines
    ann_values: list[str]          # annotation column values (class lines only)

    @property
    def is_method(self) -> bool:
        return self.method is not None


# ---------------------------------------------------------------------------
# Tree collector  (pass 1: format-agnostic)
# ---------------------------------------------------------------------------

class TreeCollector:
    """
    Walks the ClassInfo tree and produces a list of _RawLine objects.
    Knows nothing about text vs HTML formatting.
    """

    def __init__(self, opts: RenderOptions) -> None:
        self._opts = opts

    def collect_forest(self, roots: list[ClassInfo]) -> list[_RawLine]:
        out: list[_RawLine] = []
        for i, root in enumerate(self._sorted_classes(roots)):
            self._collect_class(root, prefix="", is_last=(i == len(roots) - 1),
                                is_root=True, out=out)
        return out

    def collect_list(self, classes: list[ClassInfo]) -> list[_RawLine]:
        """Flat-list collection — used for the orphans section."""
        return [
            _RawLine(prefix="  ", class_node=c, method=None,
                     ann_values=self._ann_values(c))
            for c in self._sorted_classes(classes)
        ]

    def _collect_class(
        self,
        node: ClassInfo,
        prefix: str,
        is_last: bool,
        is_root: bool,
        out: list[_RawLine],
    ) -> None:
        connector = "" if is_root else (_LAST if is_last else _TEE)
        out.append(_RawLine(
            prefix     = prefix + connector,
            class_node = node,
            method     = None,
            ann_values = self._ann_values(node),
        ))
        child_prefix = prefix if is_root else prefix + (_SPACE if is_last else _INDENT)
        if self._opts.show_methods:
            self._collect_methods(node, child_prefix, out)
        self._collect_children(node, child_prefix, out)

    def _collect_methods(
        self, node: ClassInfo, prefix: str, out: list[_RawLine]
    ) -> None:
        methods = self._visible_methods(node)
        for i, m in enumerate(self._sorted_methods(methods)):
            connector = _M_LAST if i == len(methods) - 1 else _M_TEE
            out.append(_RawLine(
                prefix     = prefix + connector,
                class_node = None,
                method     = m,
                ann_values = [],
            ))

    def _collect_children(
        self, node: ClassInfo, prefix: str, out: list[_RawLine]
    ) -> None:
        children = self._visible_children(node)
        for i, child in enumerate(self._sorted_classes(children)):
            self._collect_class(child, prefix,
                                is_last=(i == len(children) - 1),
                                is_root=False, out=out)

    def _ann_values(self, node: ClassInfo) -> list[str]:
        lookup = {_ANN_MODULE: node.module_path, _ANN_LINENO: f"L{node.lineno}"}
        return [lookup[a] for a in self._opts.annotations if a in lookup]

    def _visible_children(self, node: ClassInfo) -> list[ClassInfo]:
        if self._opts.hide_hidden:
            return [c for c in node.children if not c.name.startswith("_")]
        return node.children

    def _visible_methods(self, node: ClassInfo) -> list[MethodInfo]:
        if self._opts.hide_hidden:
            return [m for m in node.methods if not m.name.startswith("_")]
        return node.methods

    def _sorted_classes(self, nodes: list[ClassInfo]) -> list[ClassInfo]:
        return sorted(nodes, key=_class_sort_key) if self._opts.sort else list(nodes)

    def _sorted_methods(self, methods: list[MethodInfo]) -> list[MethodInfo]:
        return sorted(methods, key=_method_sort_key) if self._opts.sort else list(methods)


# ---------------------------------------------------------------------------
# Formatter protocol  (pass 2: format-specific)
# ---------------------------------------------------------------------------

class Formatter(ABC):
    """
    Base class for pass-2 formatters.
    Receives the list of _RawLine objects produced by TreeCollector and
    converts them to a final output string.
    """

    def __init__(self, opts: RenderOptions) -> None:
        self._opts = opts

    @abstractmethod
    def format_tree(self, raw: list[_RawLine]) -> str:
        """Format a collected tree (forest or flat list) into a final string."""

    @abstractmethod
    def format_orphan_header(self) -> str:
        """Return the section header for the orphans block."""

    @abstractmethod
    def format_document(self, body: str) -> str:
        """
        Wrap body content in any required outer structure.
        For text this is a no-op; for HTML it adds <html>/<head>/<body>.
        """

    def _col_widths(self, class_lines: list[_RawLine]) -> list[int]:
        """Compute per-annotation column widths across all class lines."""
        n      = len(self._opts.annotations)
        widths = [0] * n
        for r in class_lines:
            for i, val in enumerate(r.ann_values):
                widths[i] = max(widths[i], len(val))
        return widths


# ---------------------------------------------------------------------------
# Text formatter
# ---------------------------------------------------------------------------

class TextFormatter(Formatter):
    """Renders _RawLine objects as a plain-text, space-padded table."""

    def format_tree(self, raw: list[_RawLine]) -> str:
        if not raw:
            return ""
        if not self._opts.annotations:
            return self._format_no_columns(raw)
        return self._format_with_columns(raw)

    def format_orphan_header(self) -> str:
        return "\n── Orphans (no parent, no children) ──"

    def format_document(self, body: str) -> str:
        return body

    def _format_no_columns(self, raw: list[_RawLine]) -> str:
        return "\n".join(f"{r.prefix}{self._line_label(r)}" for r in raw)

    def _format_with_columns(self, raw: list[_RawLine]) -> str:
        class_lines = [r for r in raw if not r.is_method]
        name_width  = max(len(r.prefix) + len(self._line_label(r)) for r in class_lines)
        col_widths  = self._col_widths(class_lines)
        return "\n".join(
            self._format_line(r, name_width, col_widths) for r in raw
        )

    def _format_line(
        self, r: _RawLine, name_width: int, col_widths: list[int]
    ) -> str:
        label = self._line_label(r)
        base  = f"{r.prefix}{label}"
        if r.is_method or not r.ann_values:
            return base
        gap = " " * (name_width - len(base))
        n   = len(col_widths)
        ann = "  ".join(
            v.ljust(col_widths[i]) if i < n - 1 else v
            for i, v in enumerate(r.ann_values)
        )
        return f"{base}{gap}  {ann}"

    @staticmethod
    def _line_label(r: _RawLine) -> str:
        if r.is_method:
            return r.method.signature()           # type: ignore[union-attr]
        return r.class_node.label()               # type: ignore[union-attr]


# ---------------------------------------------------------------------------
# HTML formatter
# ---------------------------------------------------------------------------

# CSS class names — all prefixed ct- to avoid collisions
_CSS = {
    "box":     "ct-box",     # box-drawing characters
    "class":   "ct-class",   # class name
    "mixin":   "ct-mixin",   # mixin marker  <+Foo>
    "method":  "ct-method",  # method name
    "params":  "ct-params",  # method parameter list
    "deco":    "ct-deco",    # decorator tags  [cls]
    "module":  "ct-module",  # module annotation
    "lineno":  "ct-lineno",  # line-number annotation
    "section": "ct-section", # orphan section header
    "row":     "ct-row",     # <tr> for every line
    "mrow":    "ct-mrow",    # <tr> for method lines
}

# Annotation key → CSS class
_ANN_CSS: dict[str, str] = {
    _ANN_MODULE: _CSS["module"],
    _ANN_LINENO: _CSS["lineno"],
}

_CSS_STRUCTURE = """\
/* classtree — layout (theme-independent) */
body        { font-family: monospace; padding: 1em 2em;
              background: var(--ct-bg); color: var(--ct-fg); }
table.ct    { border-collapse: collapse; }
table.ct td { padding: 0; vertical-align: top; white-space: pre; }
td.ct-ann   { padding-left: 1.5em; }
.ct-box     { color: var(--ct-box); }
.ct-class   { color: var(--ct-class); font-weight: bold; }
.ct-mixin   { color: var(--ct-mixin); font-style: italic; }
.ct-method  { color: var(--ct-method); }
.ct-params  { color: var(--ct-params); }
.ct-deco    { color: var(--ct-deco); }
.ct-module  { color: var(--ct-module); }
.ct-lineno  { color: var(--ct-lineno); }
.ct-section { color: var(--ct-section); font-weight: bold; margin-top: 1em; }
tr.ct-mrow  { opacity: 0.80; }
@media print {
  body { background: none !important; color: #000 !important; }
}
"""

# Light theme (default): print-safe, white background, Emacs-inspired.
#   Classes → deep green  (Emacs font-lock-type-face)
#   Methods → deep blue   (Emacs font-lock-function-name-face)
#   All colours WCAG AA compliant on white.
_CSS_THEME_LIGHT = """\
/* classtree — light theme (print-safe, Emacs-inspired) */
:root {
  --ct-bg:      #ffffff;   /* white — no background ink on print  */
  --ct-fg:      #1a1a1a;   /* near-black body text              */
  --ct-box:     #999999;   /* muted grey connectors             */
  --ct-class:   #2a7a2a;   /* deep green   (type face)          */
  --ct-mixin:   #888888;   /* grey — clearly secondary            */
  --ct-method:  #00519e;   /* deep blue    (function face)      */
  --ct-params:  #7a3e9d;   /* muted purple — distinct from blue  */
  --ct-deco:    #a0522d;   /* sienna brown — decorator tags      */
  --ct-module:  #8b6914;   /* warm ochre — annotation column     */
  --ct-lineno:  #aaaaaa;   /* light grey — least important       */
  --ct-section: #c0392b;   /* clear red — orphan header          */
}
"""

# Dark theme: opt-in via --theme dark.  Emacs modus-vivendi palette.
_CSS_THEME_DARK = """\
/* classtree — dark theme (Emacs modus-vivendi) */
:root {
  --ct-bg:      #1e1e2e;
  --ct-fg:      #cdd6f4;
  --ct-box:     #585b70;
  --ct-class:   #89b4fa;   /* blue-ish — modus-vivendi type     */
  --ct-mixin:   #a6adc8;
  --ct-method:  #a6e3a1;   /* green    — modus-vivendi function */
  --ct-params:  #cba6f7;
  --ct-deco:    #f38ba8;
  --ct-module:  #f9e2af;
  --ct-lineno:  #585b70;
  --ct-section: #fab387;
}
"""

_THEMES: dict[str, str] = {
    "light": _CSS_THEME_LIGHT,
    "dark":  _CSS_THEME_DARK,
}


def build_inline_css(theme: str) -> str:
    """Return the complete inline CSS for the given theme name."""
    theme_vars = _THEMES.get(theme, _CSS_THEME_LIGHT)
    return theme_vars + _CSS_STRUCTURE


def _e(text: str) -> str:
    """HTML-escape a plain string."""
    return html_mod.escape(text)


def _span(css_class: str, content: str) -> str:
    return f'<span class="{css_class}">{content}</span>'


class HtmlFormatter(Formatter):
    """
    Renders _RawLine objects as an HTML table that preserves the ASCII-art
    look while using real columns and semantic CSS classes for colouring.

    Each output line becomes a <tr>.  The tree column is a single <td>;
    each annotation gets its own <td class="ct-ann">.
    """

    def __init__(self, opts: RenderOptions, css_mode: CssMode) -> None:
        super().__init__(opts)
        self._css_mode = css_mode

    def format_tree(self, raw: list[_RawLine]) -> str:
        if not raw:
            return ""
        rows = [self._render_row(r) for r in raw]
        return '<table class="ct">\n' + "\n".join(rows) + "\n</table>"

    def format_orphan_header(self) -> str:
        return f'<p class="{_CSS["section"]}">── Orphans (no parent, no children) ──</p>'

    def format_document(self, body: str) -> str:
        return "\n".join([
            "<!DOCTYPE html>",
            '<html lang="en">',
            "<head>",
            '<meta charset="utf-8">',
            "<title>classtree</title>",
            self._css_mode.head_fragment(),
            "</head>",
            "<body>",
            body,
            "</body>",
            "</html>",
        ])

    def _render_row(self, r: _RawLine) -> str:
        row_class = _CSS["mrow"] if r.is_method else _CSS["row"]
        tree_cell = self._tree_cell(r)
        ann_cells = self._ann_cells(r)
        return f'  <tr class="{row_class}">{tree_cell}{"".join(ann_cells)}</tr>'

    def _tree_cell(self, r: _RawLine) -> str:
        box    = _span(_CSS["box"], _e(r.prefix))
        label  = self._method_html(r.method) if r.is_method else self._class_html(r.class_node)
        return f"<td>{box}{label}</td>"

    def _ann_cells(self, r: _RawLine) -> list[str]:
        if r.is_method:
            return [f'<td class="ct-ann"></td>' for _ in self._opts.annotations]
        cells: list[str] = []
        # pair each annotation key with its value (may be absent if list shorter)
        for i, ann_key in enumerate(self._opts.annotations):
            val     = r.ann_values[i] if i < len(r.ann_values) else ""
            css_cls = _ANN_CSS.get(ann_key, "")
            content = _span(css_cls, _e(val)) if (val and css_cls) else _e(val)
            cells.append(f'<td class="ct-ann">{content}</td>')
        return cells

    @staticmethod
    def _class_html(node: ClassInfo) -> str:           # type: ignore[return]
        name_span = _span(_CSS["class"], _e(node.name))
        if node.mixin_bases:
            mixin_text = "  &lt;+" + ", ".join(
                _e(b.name) for b in node.mixin_bases
            ) + "&gt;"
            return name_span + _span(_CSS["mixin"], mixin_text)
        return name_span

    @staticmethod
    def _method_html(m: MethodInfo) -> str:            # type: ignore[return]
        name   = _span(_CSS["method"], _e(m.name))
        params = _span(_CSS["params"], _e(m.params))
        result = f"{name}({params})"
        if m.decorators:
            tags = _span(_CSS["deco"], _e(f"  [{', '.join(m.decorators)}]"))
            result += tags
        return result


# ---------------------------------------------------------------------------
# CSS mode  (strategy for how CSS is delivered)
# ---------------------------------------------------------------------------

class CssMode(ABC):
    """Strategy: how the CSS reaches the browser."""

    @abstractmethod
    def head_fragment(self) -> str:
        """Return the HTML fragment to insert inside <head>."""

    @abstractmethod
    def prepare(self) -> None:
        """Perform any side-effects needed before rendering (e.g. write file)."""


class InlineCssMode(CssMode):
    def __init__(self, theme: str) -> None:
        self._theme = theme

    def head_fragment(self) -> str:
        return f"<style>\n{build_inline_css(self._theme)}</style>"

    def prepare(self) -> None:
        pass


class ExternalCssMode(CssMode):
    def __init__(self, css_path: Path) -> None:
        self._path = css_path

    def head_fragment(self) -> str:
        return f'<link rel="stylesheet" href="{_e(str(self._path))}">'

    def prepare(self) -> None:
        if not self._path.exists():
            print(
                f"[warning] External CSS file not found: {self._path}",
                file=sys.stderr,
            )


class GeneratedCssMode(CssMode):
    def __init__(self, css_path: Path, theme: str) -> None:
        self._path  = css_path
        self._theme = theme

    def head_fragment(self) -> str:
        return f'<link rel="stylesheet" href="{_e(str(self._path))}">'

    def prepare(self) -> None:
        self._path.write_text(build_inline_css(self._theme), encoding="utf-8")
        print(f"[info] CSS written to {self._path}", file=sys.stderr)


def parse_css_mode(value: str) -> CssMode:
    """
    Parse the --css argument string into a CssMode instance.
    Theme is injected later (after --theme is parsed) via inject_theme().

    Accepted forms:
      inline               → InlineCssMode
      external:<path>      → ExternalCssMode
      generate:<path>      → GeneratedCssMode
    """
    if value == "inline":
        return InlineCssMode(theme="light")   # placeholder; overridden later
    if ":" in value:
        kind, _, path_str = value.partition(":")
        path = Path(path_str)
        if kind == "external":
            return ExternalCssMode(path)
        if kind == "generate":
            return GeneratedCssMode(path, theme="light")  # placeholder
    raise argparse.ArgumentTypeError(
        f"Invalid --css value: '{value}'. "
        "Expected: inline | external:<path> | generate:<path>"
    )


def inject_theme(css_mode: CssMode, theme: str) -> None:
    """Set the theme on css modes that embed CSS (inline / generate)."""
    if isinstance(css_mode, (InlineCssMode, GeneratedCssMode)):
        css_mode._theme = theme


# ---------------------------------------------------------------------------
# Renderer  (orchestrates collector + formatter)
# ---------------------------------------------------------------------------

class TreeRenderer:
    """
    Orchestrates pass 1 (TreeCollector) and pass 2 (Formatter).
    Knows about the two-section structure (main tree + optional orphans)
    but delegates all format-specific work to the Formatter.
    """

    def __init__(self, opts: RenderOptions, formatter: Formatter) -> None:
        self._opts      = opts
        self._collector = TreeCollector(opts)
        self._formatter = formatter

    def render(self, roots: list[ClassInfo], orphans: list[ClassInfo] | None) -> str:
        parts: list[str] = []
        parts.append(self._formatter.format_tree(self._collector.collect_forest(roots)))
        if orphans:
            parts.append(self._formatter.format_orphan_header())
            parts.append(self._formatter.format_tree(self._collector.collect_list(orphans)))
        body = "\n".join(parts)
        return self._formatter.format_document(body)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

class _AnnotationAction(argparse.Action):
    """
    Appends a fixed annotation key to the shared 'annotations' list each time
    the flag appears, preserving CLI insertion order.
    Duplicates are silently ignored.
    nargs=0 prevents argparse from consuming the next token as a value.
    """

    def __init__(self, *args, **kwargs) -> None:
        kwargs["nargs"] = 0
        super().__init__(*args, **kwargs)

    def __call__(
        self,
        parser:        argparse.ArgumentParser,
        namespace:     argparse.Namespace,
        values:        object,
        option_string: str | None = None,
    ) -> None:
        current: list[str] = getattr(namespace, self.dest, None) or []
        if self.const not in current:
            current.append(self.const)
        setattr(namespace, self.dest, current)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="classtree",
        description="Print a static ASCII class-hierarchy tree for a Python package.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Root directory (package) or single .py file to scan.",
    )
    parser.add_argument(
        "--root", "-r",
        metavar="CLASS",
        default=None,
        help="Show only the subtree rooted at CLASS.",
    )
    parser.add_argument(
        "--show-modules", "-m",
        dest="annotations",
        action=_AnnotationAction,
        const=_ANN_MODULE,
        default=[],
        help="Add a module annotation column.",
    )
    parser.add_argument(
        "--show-lineno", "-l",
        dest="annotations",
        action=_AnnotationAction,
        const=_ANN_LINENO,
        help="Add a line-number annotation column.",
    )
    parser.add_argument(
        "--show-methods", "-M",
        action="store_true",
        help="Show methods for each class in compact form.",
    )
    parser.add_argument(
        "--hide-hidden", "-H",
        action="store_true",
        help="Hide classes and methods whose names start with '_'.",
    )
    parser.add_argument(
        "--orphans", "-o",
        action="store_true",
        help="Also list classes with no resolved parent and no children.",
    )
    parser.add_argument(
        "--no-sort",
        action="store_true",
        help="Preserve source-file order instead of sorting.",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Emit HTML output instead of plain text.",
    )
    parser.add_argument(
        "--css",
        metavar="MODE",
        default="inline",
        type=parse_css_mode,
        help=(
            "CSS delivery mode (only used with --html): "
            "inline (default) | external:<path> | generate:<path>"
        ),
    )
    parser.add_argument(
        "--theme",
        choices=["light", "dark"],
        default="light",
        help="Colour theme for --html output (default: light)."
    )
    return parser


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

class Application:
    """Wires together scanning, forest-building, rendering, and output."""

    def __init__(self, args: argparse.Namespace) -> None:
        self._args = args

    def run(self) -> None:
        path     = self._resolve_path()
        classes  = self._scan(path)
        forest   = self._build_forest(classes)
        roots    = self._find_roots(forest)
        orphans  = self._collect_orphans(forest)
        renderer = self._make_renderer()
        self._emit(renderer, roots, orphans)
        self._print_summary(classes, roots)

    def _resolve_path(self) -> Path:
        path = self._args.path.resolve()
        if not path.exists():
            print(f"[error] Path does not exist: {path}", file=sys.stderr)
            sys.exit(1)
        return path

    def _scan(self, path: Path) -> list[ClassInfo]:
        classes = SourceScanner(path).scan()
        if not classes:
            print("[warning] No classes found.", file=sys.stderr)
            sys.exit(0)
        if self._args.hide_hidden:
            classes = [c for c in classes if not c.name.startswith("_")]
        return classes

    def _build_forest(self, classes: list[ClassInfo]) -> HierarchyForest:
        return HierarchyForest(classes)

    def _find_roots(self, forest: HierarchyForest) -> list[ClassInfo]:
        try:
            return forest.roots(filter_root=self._args.root)
        except ValueError as exc:
            print(f"[error] {exc}", file=sys.stderr)
            sys.exit(1)

    def _collect_orphans(self, forest: HierarchyForest) -> list[ClassInfo] | None:
        if not self._args.orphans:
            return None
        orphans = forest.orphans()
        return orphans if orphans else None

    def _make_renderer(self) -> TreeRenderer:
        opts      = self._build_render_opts()
        formatter = self._build_formatter(opts)
        return TreeRenderer(opts, formatter)

    def _build_render_opts(self) -> RenderOptions:
        return RenderOptions(
            annotations  = self._args.annotations,
            show_methods = self._args.show_methods,
            hide_hidden  = self._args.hide_hidden,
            sort         = not self._args.no_sort,
        )

    def _build_formatter(self, opts: RenderOptions) -> Formatter:
        if self._args.html:
            css_mode = self._args.css
            inject_theme(css_mode, self._args.theme)
            css_mode.prepare()
            return HtmlFormatter(opts, css_mode)
        return TextFormatter(opts)

    def _emit(
        self,
        renderer: TreeRenderer,
        roots: list[ClassInfo],
        orphans: list[ClassInfo] | None,
    ) -> None:
        print(renderer.render(roots, orphans))

    def _print_summary(
        self, classes: list[ClassInfo], roots: list[ClassInfo]
    ) -> None:
        print(
            f"\n  {len(classes)} classes scanned  |  {len(roots)} tree root(s)",
            file=sys.stderr,
        )


def main() -> None:
    args = build_arg_parser().parse_args()
    Application(args).run()


if __name__ == "__main__":
    main()
