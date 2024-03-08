# (C) Albert Mietus, 2023. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .namednodes import NamedNode

__all__ = [] # Manually import what you need!

@dataclass
class TypedParameter(AIGR):
    """This is many a helper class/struct to combine a parameter: a name and an type"""
    name: str
    type: type

@dataclass
class Argument(AIGR):
    """This is many a helper class/struct to combine a argument: a value and optional a name"""
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None


@dataclass
class Specialise(NamedNode):
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


