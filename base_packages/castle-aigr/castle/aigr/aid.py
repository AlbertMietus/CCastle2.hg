# (C) Albert Mietus, 2023.2024. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR, AIGRNode
from castle.aigr import ID, types
from castle import aigr

from .nodes import NamedNode
""" XXX ToDo: refactor, rename & relocate ..."""


@dataclass
class TypedParameter(NamedNode):
    """A parameter is a placeholder in a function/callable **definition**.
       It acts as variable inside the body In Castle, it always has a name and a Type."""
    name  : ID
    type  : types._types # An AIGR-type

    def __post_init__(self):
        if not isinstance(self.name, ID):
            self.name = ID(self.name, context=aigr.Def())


@dataclass
class Argument(AIGRNode):
    """An argument is a value passed during function/callable **invocation**.
       In Castle, we support both positional and named arguments. Hence, an argument can have a name."""
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None # XXX ToDo str or ID?

    def __post_init__(self):
        if self.name and not isinstance(self.name, ID):
            self.name = ID(self.name, context=aigr.Def())




