# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from __future__ import annotations

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

from . import AIGR, ID
from . import Argument


class NameError(AttributeError):pass


@dataclass
class NamedNode(AIGR):
    name       : ID|str
    _: KW_ONLY
    # type(_ns) is NamedNode, but that leads to a imports-cycle. So, use te more generic AIGR
    _ns        :PTH.Optional[AIGR]=dc_field(init=None, default=None)  #type: ignore[call-overload]

    def __post_init__(self):
        if not isinstance(self.name, ID):
            self.name = ID(self.name)

    def register_in_NS(self, ns: AIGR): #same: type(ns) is NameSpace, but ...
        self._ns = ns

    @property
    def ns(self):
        return self._ns

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
