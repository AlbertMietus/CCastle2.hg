# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.support.stack``.
# Hand-maintained companion to stack.py.
#
# NOTE: castle.readers.support.__init__.py has a known import bug:
#   from .support import Stack   # WRONG -- should be: from .stack import Stack
# See doc/CodeAI-analysis/ToDo/readers-support-Stack.rst.
# Until the bug is fixed, import Stack directly from this module:
#   from castle.readers.support.stack import Stack

import typing as PTH

_T = PTH.TypeVar("_T")


class Stack(PTH.Generic[_T]):
    """A simple generic LIFO stack.

    Used internally by the Castle reader support layer.

    **Import note**: ``castle.readers.support.__init__.py`` contains a known
    bug (it imports from ``.support`` instead of ``.stack``).  Until that bug
    is fixed, import this class directly::

        from castle.readers.support.stack import Stack

    Basic usage::

        stack: Stack[str] = Stack()
        stack.push("hello")
        stack.push("world")
        top = stack.peek()         # "world" -- does not pop
        val = stack.pop()          # "world" -- removes it
        assert not stack.is_empty()
        assert stack.size() == 1   # or: len(stack) == 1
    """

    stack: list[_T]
    """The underlying list; index ``-1`` is the top."""

    def __init__(self) -> None: ...

    def push(self, item: _T) -> None:
        """Push *item* onto the top of the stack."""
        ...

    def pop(self) -> _T:
        """Remove and return the top item.

        :raises IndexError: if the stack is empty.
        """
        ...

    def peek(self) -> _T:
        """Return the top item without removing it.

        :raises IndexError: if the stack is empty.
        """
        ...

    def is_empty(self) -> bool:
        """Return ``True`` iff the stack contains no items."""
        ...

    def size(self) -> int:
        """Return the number of items on the stack."""
        ...

    def __len__(self) -> int:
        """Alias for :meth:`size`; enables ``len(stack)``."""
        ...
