# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.aid.block``.

import typing as PTH

TextBlock = PTH.Optional[str | "Block"]
"""Convenience alias: the result type of every ``visit_*`` / ``depart_*`` method.

A ``Block`` (indented tree of lines), a plain ``str``, or ``None`` (empty output).
"""

class Block:
    """Indented, tree-structured text buffer used throughout the RPy renderer.

    A ``Block`` holds a list of strings and nested child ``Block`` objects.
    When converted to ``str`` (via :meth:`__str__` / :meth:`toStr`), each nested
    child is indented by :attr:`_indent` relative to its parent.

    Usage
    -----
    ::

        from castle.writers.RPy.aid import Block

        txt = Block("class Foo(Base):")
        body = Block("def __init__(self): pass")
        txt.sub(body)
        print(txt)        # -> 'class Foo(Base):\\n    def __init__(self): pass\\n'

        txt += "extra_line"   # append (no indenting of the string itself)

    The ``+=`` operator appends without extra indentation; :meth:`sub` appends a
    child block that will be indented when rendered.
    """

    _txt: PTH.List[str | "Block"]
    """Internal list of lines (str) and sub-blocks."""
    _indent: str
    """Prefix string prepended to every sub-block line (default: four spaces)."""

    def __init__(
        self,
        text: PTH.Optional[str | PTH.Sequence[str] | "Block"] = None,
        indent: PTH.Optional[str] = None,
    ) -> None:
        """Create a Block, optionally pre-filled with *text*.

        Parameters
        ----------
        text:
            Initial content.  A ``str`` is split on newlines; a sequence of
            strings or a ``Block`` is extended as-is.  ``None`` creates an
            empty block.
        indent:
            Override the default four-space indentation for child blocks.
        """
        ...

    def __iadd__(self, text: PTH.Any) -> "Block":
        """Append *text* to this block (no extra indentation).

        Accepts ``str``, ``Sequence[str]``, ``Block``, or ``None`` (no-op).
        Returns ``self`` for chaining.
        """
        ...

    def sub(self, block: PTH.Optional["Block"]) -> "Block":
        """Append *block* as an indented child.

        The child will be rendered with one extra level of :attr:`_indent`.
        ``None`` is silently ignored.  Returns ``self`` for chaining.
        """
        ...

    def toStr(self, prefix: str = "", end: str = "\n") -> str:
        """Render the block tree to a string.

        Parameters
        ----------
        prefix:
            String prepended to *every* line (used recursively).
        end:
            Line separator (default newline).
        """
        ...

    def __str__(self) -> str:
        """Return the fully rendered text (calls :meth:`toStr` with defaults)."""
        ...

    def set_indent(self, indent: PTH.Optional[str] = None) -> None:
        """Change the indentation prefix for sub-blocks of this block.

        ``None`` resets to the default (four spaces).
        """
        ...
