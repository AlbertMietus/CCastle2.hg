# (C) Albert Mietus, 2023. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .nodes import NamedNode


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




