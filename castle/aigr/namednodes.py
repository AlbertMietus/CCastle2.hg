# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from __future__ import annotations

__all__ = ['NameError', 'NamedNode']

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

from . import AIGR



class NameError(AttributeError):pass

@dataclass
class NamedNode(AIGR):
    name       :str
    _: KW_ONLY
    _ns        :PTH.Optional[NameSpace]=dc_field(init=None, default=None)  #type: ignore[call-overload]

    def register_in_NS(self, ns):
        self._ns = ns

    @property
    def ns(self):
        return self._ns

