# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin._debug``.
# Debug mixin and helper utilities (RPython-compatible).

import typing as PTH

isV3: bool
"""True when running on CPython 3; False under RPython/PyPy2."""
isRP: bool
"""True when running under RPython (not Python 3)."""

class DebugMixIn:
    """Mixin that adds human-readable ``repr()`` output to RPy runtime objects.

    Subclasses should:

    1. Set :attr:`_debug_label` to a human-readable identifier (or call
       :meth:`_set_label`).
    2. Override :meth:`_debug_attr_` to return the key attributes as a string.

    Usage
    -----
    ::

        class MyObj(DebugMixIn):
            _debug_label = "my_obj"
            def _debug_attr_(self, name_only=True):
                return f"x={self.x}"

        repr(MyObj())   # -> 'MyObj[_label=my_obj]()'
    """

    _debug_label: PTH.ClassVar[str]
    """Class-level human-readable label (default ``"NotSet"``)."""

    def _debug_(self, name_only: bool = True) -> str:
        """Return a compact debug string for this object.

        When *name_only* is ``True`` (default) only the class name and label
        are shown; when ``False`` the full attribute string from
        :meth:`_debug_attr_` is appended.
        """
        ...

    def _set_label(self, name: str) -> None:
        """Set the instance-level :attr:`_debug_label`."""
        ...

    def _debug_attr_(self, name_only: bool = True) -> str:
        """Return object attributes as a string (override in subclasses)."""
        ...

    def __repr__(self) -> str: ...

    def _debug_name(self) -> str:
        """Return a short name string for use in nested debug output."""
        ...

    def _class_name(self) -> str:
        """Return ``type(self).__name__``."""
        ...


def _obj_name(obj: PTH.Any) -> str:
    """Return ``obj._debug_name()`` or ``"None"`` when *obj* is falsy."""
    ...

def file_stem(filepath: str) -> str:
    """Return the stem (name without extension) of *filepath*.

    Implemented without ``pathlib`` or ``os.path.split`` for RPython
    compatibility.
    """
    ...

def handler_name(h: PTH.Any) -> str:
    """Return the ``__name__`` of a handler function, or ``"NIL"`` if None."""
    ...
