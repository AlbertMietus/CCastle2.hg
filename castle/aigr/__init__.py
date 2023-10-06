# (C) Albert Mietus, 2023. Part of Castle/CCastle project


class AIGR: # Abstract Intermediate Graph Representation
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)


class _Marker: pass

from .events import *
from .protocols import *
from .interfaces import *
