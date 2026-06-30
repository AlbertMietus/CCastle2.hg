# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.todo``.
# Hand-maintained "manual autodoc" companion to todo.py.

import typing as PTH
from dataclasses import dataclass

@dataclass
class mark_Dataclass:
    """Marker base for a (data)class that is not implemented yet.

    Subclassing it makes any attempt to *instantiate* fail with
    ``NotImplementedError`` -- a deliberate guard for placeholder nodes.
    """
    def __post_init__(self, *t: PTH.Any, **d: PTH.Any) -> None: ...

class Typing:
    """Placeholder marking a type that still has to be designed."""
    def __new__(cls, *t: PTH.Any, **d: PTH.Any) -> PTH.Any: ...
