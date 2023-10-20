# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from __future__ import annotations
from dataclasses import dataclass



class AIGR: # Abstract Intermediate Graph Representation
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)



@dataclass
class _Marker:
    msg :str=""

from .events import *
from .protocols import *
from .interfaces import *
from .namespaces import *
from .namednodes import *
