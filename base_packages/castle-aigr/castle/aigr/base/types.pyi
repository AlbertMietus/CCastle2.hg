# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.base.types``.
# Hand-maintained "manual autodoc" companion to types.py.

from dataclasses import dataclass
from .AIGR import AIGR as AIGR

@dataclass
class _types(AIGR):
    """An AIGR *type*: a unique object that represents a Castle type.

    A type is identified by its name (``represents``) together with its
    ``_types`` subclass, so a built-in ``int`` can never clash with a
    user-defined type of the same name. Compare/pass the ready-made singletons
    below (``int``, ``float``, ``string``, ``boolean``) rather than constructing
    new ones for built-ins.
    """
    represents: str
    """The (string) name of the type this object stands for."""

class _buildin(_types):
    """An AIGR type for a Castle *built-in* type."""

class _Number(AIGR):
    """Mixin marking numeric types."""

class _buildinNumber(_buildin, _Number):
    """A built-in *numeric* type (e.g. ``int``, ``float``)."""

class _user(_types):
    """An AIGR type for a *user-defined* type."""

int: _buildinNumber
"""The built-in integer type singleton."""
float: _buildinNumber
"""The built-in floating-point type singleton."""
string: _buildin
"""The built-in string type singleton."""
boolean: _buildin
"""The built-in boolean type singleton."""
