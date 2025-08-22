# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass, KW_ONLY
import typing as PTH                                       # Python TypeHints

@dataclass
class AIGR: # Abstract Intermediate Graph Representation
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)

@dataclass
class AIGRNode(AIGR):
    """An AIGRNode is always part of a tree-alike graph, and so has one parent.

    It also has (many) childeren, to be found via the data-field. Only the main-parent is generic."""

    _: KW_ONLY
    parent: PTH.Optional[AIGR] = None
