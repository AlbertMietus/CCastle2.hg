# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.renderer``.
#
# Intentional dead code NOT stubbed (per intentional-dead-code.rst):
# - XXX_OLD_visit_Call: dead method kept for reference; excluded from public API.
# - _render_args: WIP method (contains ``assert False``); stubbed as private
#   because it IS called by visit_Call and is part of the class interface.

import typing as PTH
from castle import aigr
from castle.monorail.base.visitors import Visitor
from castle.writers.RPy.aid import Block, TextBlock
from .walker import Walker
from .machinery import Machinery
from .portray import Portray
from .idref import IDRef

class Renderer(Visitor):
    """The main RPy code-generation orchestrator.

    ``Renderer`` is the top-level entry point for the RPy back-end.  Call
    :meth:`render` with an AIGR node (typically an :class:`RPy_unit`) and get
    back a string of runnable Python code.

    It owns four single-purpose helpers, each injected via ``__init__``:

    * :attr:`walker`   -- tree traversal (which children to descend)
    * :attr:`machinery` -- event-dispatch-table strategy (pluggable backend)
    * :attr:`portray`  -- AIGR name -> RPy name translation
    * :attr:`idref`    -- ID-with-reference -> RPy name resolution

    All helpers have sensible defaults, so ``Renderer()`` with no arguments
    is the common case.

    Usage
    -----
    ::

        from castle.writers.RPy.writer.renderer import Renderer
        from castle.writers.RPy.transformers import Source2RPy
        from castle.writers.RPy.aigr.units import ScaffolderUnit

        unit = Source2RPy(source_ns)
        code = Renderer().render(unit)   # -> str of Python code
        print(code)

    Or via ScaffolderUnit for file output::

        su = ScaffolderUnit(unit)
        su.write_out(inDir="build/")    # renders + saves
    """

    walker: Walker
    """Tree-traversal helper (default: ``Walker()``)."""
    machinery: Machinery
    """Dispatch-table rendering strategy (default: ``Machinery()`` -> ``M_DC_chained_dict``)."""
    portray: Portray
    """Name-translation helper (default: ``Portray(self)``)."""
    idref: IDRef
    """Reference-resolution helper (default: ``IDRef(self)``)."""

    def __init__(
        self,
        walker: PTH.Optional[Walker] = ...,
        machinery: PTH.Optional[Machinery] = ...,
        portray: PTH.Optional[Portray] = ...,
        idref: PTH.Optional[IDRef] = ...,
        **kw: PTH.Any,
    ) -> None:
        """Initialise the renderer, injecting helpers.

        All helpers default to their standard implementations.  Pass custom
        instances to override behaviour (e.g. for testing or specialised output).
        """
        ...

    # --- Public API ---

    def render(self, node: aigr.AIGR) -> str:
        """Render *node* to a string of Python code.

        This is **the main entry point**.  It calls ``visit(node)`` which
        dispatches to the appropriate ``visit_*`` handler; the resulting
        :class:`Block` is converted to ``str``.

        Parameters
        ----------
        node:
            Any AIGR node.  In normal use this is an :class:`RPy_unit`
            (produced by :func:`Source2RPy`).

        Returns
        -------
        str
            Complete, runnable RPy Python source text.
        """
        ...

    def render_subNodes(self, node: PTH.Any) -> PTH.Optional[Block]:
        """Ask the :attr:`walker` for *node*'s children and render each one.

        Returns a :class:`Block` containing the rendered children, or
        ``None`` if there are no children.
        """
        ...

    # --- visit_* handlers ---

    def visit_ComponentInterface(self, node: PTH.Any) -> TextBlock:
        """Render a ``CC_B_ComponentInterface(...)`` construction with ports."""
        ...

    def visit_ComponentImplementation(self, node: PTH.Any) -> TextBlock:
        """Render the generated Python class and its ``__init__`` method."""
        ...

    def depart_ComponentImplementation(self, node: PTH.Any) -> TextBlock:
        """Emit the component-class metadata and dispatch tables (post-children)."""
        ...

    def visit_Method(self, node: PTH.Any) -> TextBlock:
        """Render a ``def <name>(self, ...)`` method."""
        ...

    def visit_Initializer(self, node: PTH.Any) -> TextBlock:
        """Render a ``def _castle_init(self, ...)`` initializer."""
        ...

    def visit_EventHandler(self, node: PTH.Any) -> TextBlock:
        """Render an event-handler method definition."""
        ...

    def visit_Body(self, node: PTH.Any) -> TextBlock:
        """Render a statement body (delegates to render_subNodes)."""
        ...

    def visit_VoidCall(self, node: PTH.Any) -> TextBlock:
        """Render a void call statement (delegates to render_subNodes)."""
        ...

    def visit_Call(self, node: PTH.Any) -> TextBlock:
        """Render a function/method call expression: ``<callable>(<args>)``."""
        ...

    def visit__literal(self, node: PTH.Any) -> TextBlock:
        """Render a literal constant (string triple-quoted; numbers as-is)."""
        ...

    def visit_fString(self, node: PTH.Any) -> TextBlock:
        """Render an f-string as a ``%``-style format string."""
        ...

    def visit_ID(self, node: PTH.Any) -> TextBlock:
        """Render an ID, delegating to :attr:`idref` when a Ref context is present."""
        ...

    def visit_RPy_unit(self, node: PTH.Any) -> TextBlock:
        """Render the top-level unit: emit the file header then all top-level nodes."""
        ...

    def visit_Become(self, node: PTH.Any) -> TextBlock:
        """Render a single assignment statement: ``<lhs> = <rhs>``."""
        ...

    def visit_EventProtocol(self, node: PTH.Any) -> TextBlock:
        """Render a ``CC_B_Protocol(name=..., kind=..., events=[])`` construction."""
        ...

    def visit_EventOverPort(self, node: PTH.Any) -> TextBlock:
        """Render an event-over-port send (delegated to :attr:`machinery`)."""
        ...

    def visit_EventToSub(self, node: PTH.Any) -> TextBlock:
        """Render an event-to-sub-component send (delegated to :attr:`machinery`)."""
        ...

    # --- Protected helpers ---

    def _render_def(
        self,
        node: PTH.Any,
        callDef_name: PTH.Optional[str] = ...,
    ) -> Block:
        """Emit ``def <name>(self, param, ...):`` for a callable node."""
        ...

    def _render_callable(self, node: PTH.Any) -> TextBlock:
        """Resolve and render the callable part of a Call node.

        Prepends ``'self.'`` when the callable refers to a Method.
        Only ``ID``-valued callables are supported; others raise
        ``NotImplementedError``.
        """
        ...

    def _render_args(self, node: PTH.Any) -> TextBlock:
        """Render the argument list for a Call node.

        WIP: currently raises ``AssertionError("Need the new Bundler")``.
        See intentional-dead-code.rst.
        """
        ...

    def _render_ComponentClass(self, node: PTH.Any) -> TextBlock:
        """Emit the ``cc_C_<Name> = buildin.CC_B_ComponentClass(...)`` line."""
        ...

    def _DispatchTables(self, node: PTH.Any) -> TextBlock:
        """Render all dispatch tables for *node*'s handlers."""
        ...

    def _EventDispatchTables(self, node: PTH.Any) -> TextBlock:
        """Build and render one dispatch table per unique port in *node*'s handlers."""
        ...

    def _file_header(self, node: PTH.Any) -> TextBlock:
        """Emit the standard import header for a generated RPy file."""
        ...
