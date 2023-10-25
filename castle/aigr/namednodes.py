# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from __future__ import annotations

__all__ = ['NameError', 'NamedNode']

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

from . import AIGR


class NameError(AttributeError):pass

class ID(str): pass #XXX for now and ID is a string, but that can be changed


@dataclass
class NamedNode(AIGR):
    name       :ID
    _: KW_ONLY
    # type(_ns) is NamedNode, but that leads to a cycle in imports, to use te more generic AIGR
    _ns        :PTH.Optional[AIGR]=dc_field(init=None, default=None)  #type: ignore[call-overload]


    def register_in_NS(self, ns: AIGR): #same: type(ns) is NameSpace, but ...
        self._ns = ns

    @property
    def ns(self):
        return self._ns

