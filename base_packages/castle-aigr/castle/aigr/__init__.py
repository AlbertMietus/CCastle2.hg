# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass
from typing import ClassVar



@dataclass
class AIGR: # Abstract Intermediate Graph Representation
    _kids : ClassVar[tuple[str,...]] = tuple() # All subclasses should set this to be able to walk the tree (as class variable)
    def __new__(cls, *args, **kwargs):
        if cls == AIGR:
            raise NotImplementedError(f"Instantiate a subclass of {cls}, not the `Abstract Intermediate Graph Representation`` itself")
        return super().__new__(cls)




from .base import *
from .aid import *
from .events import *
from .protocols import *
from .interfaces import *
from .namespaces import *
from .nodes import *

from .statements import *
from .expressions import *
