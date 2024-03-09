# (C) Albert Mietus, 2023. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .namednodes import NamedNode

__all__:PTH.List[str] = [] # Manually import what you need!

@dataclass
class TypedParameter(AIGR):
    """A parameter is a variable in a function/callable **definition**.
       It acts as placeholder and has no specific value. In Castle, it always has a Type."""
    name: str # XXX ToDo str or  ID?
    type: type

@dataclass
class Argument(AIGR):
    """An argument is a value passed during function/callable **invocation**.
       In Castle, we support both positional and named arguments. Hence, an argument can have a name."""
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None # XXX ToDo str or  ID?


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


