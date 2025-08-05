# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" XXX ToDo: Test, Refactor, Split & Doc"""

from __future__ import annotations

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

from . import ID
from . import AIGRNode
from . import Argument


@dataclass
class NamedNode(AIGRNode):
    name       : ID|str

    def __post_init__(self):
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

    def __getattr__(self, name):
        """delegate "everything" to `.`based_on``!
        Kind of inherit, but not to superclass (Protocol), but to the instance (a Protocol) that is wrapped"""

        return getattr(self.based_on, name)
