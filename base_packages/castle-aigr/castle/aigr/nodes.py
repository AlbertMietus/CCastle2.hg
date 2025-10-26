# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" XXX ToDo: Test, Refactor, Split & Doc"""

from __future__ import annotations

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

from . import ID
from . import AIGR, AIGRNode

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .aid import Argument

@dataclass
class NamedNode(AIGRNode):
    #name   :PTH.Optional[ID|str]=dc_field(default_factory=lambda: None)
    name    :ID|str
    _: KW_ONLY
    parent  :PTH.Optional[AIGR]=None

    def __post_init__(self):
        if self.name is None:
            logger.critical("NamedNode: name is None, this is not allowed")
        if not isinstance(self.name, ID):
            self.name = ID(self.name)

@dataclass
class Specialise(NamedNode):
    """XXX: Doc, Move to ..."""

    _: KW_ONLY
    based_on:  NamedNode
    arguments: PTH.Sequence[Argument]

    def __post_init__(self):
        if not self.name: # or self.name == "":
            self.name = f"Specialised version of {self.based_on.name}({self.arguments})"
