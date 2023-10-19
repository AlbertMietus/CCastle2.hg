# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from __future__ import annotations

from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
import typing as PTH                                                                                  # Python TypeHints

class AIGR: # Abstract Intermediate Graph Representation
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)

@dataclass
class NamedNode(AIGR):
    name       :str
    _: KW_ONLY
    _ns        :PTH.Optional[NameSpace]=dc_field(init=None, default=None)  #type: ignore[call-overload]

class NameError(AttributeError):pass

class _Marker: pass

from .events import *
from .protocols import *
from .interfaces import *
from .namespaces import *
