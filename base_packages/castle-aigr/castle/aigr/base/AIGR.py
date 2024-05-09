# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass
import typing as PTH                                       # Python TypeHints


@dataclass
class AIGR: # Abstract Intermediate Graph Representation
    _kids : PTH.ClassVar[tuple[str,...]] = tuple() # All subclasses should set this to be able to walk the tree (as class variable)
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)

