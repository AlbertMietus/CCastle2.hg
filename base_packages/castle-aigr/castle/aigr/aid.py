# (C) Albert Mietus, 2023.2024. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from . import  AIGRNode
from castle.aigr import ID, types

from .nodes import NamedNode
""" XXX ToDo: refactor, rename & relocate ..."""


@dataclass
class TypedParameter(NamedNode):
    """A parameter is a placeholder in a function/callable **definition**.
       It acts as variable inside the body In Castle, it always has a name and a Type."""
    name  : ID|str
    type  : types._types # An AIGR-type

    def __post_init__(self):
        if not isinstance(self.name, ID):
            self.name = ID.Def(self.name)


@dataclass
class Argument(AIGRNode):
    """An argument is a value passed during function/callable **invocation**.
       In Castle, we support both positional and named arguments. Hence, an argument can have a name.

       .. note::  like amost everywhere:

          `value` is not an Python value, but a CCastle-value in transit to an value in
          the target-language (like RPython, C/C++, or assembly). And so, typical the string
          representation of it, in an envolpe to hold type and other info. """

    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None # XXX ToDo str or ID?

    def __post_init__(self):
        if self.name and not isinstance(self.name, ID):
            self.name = ID.Def(self.name)

ArgumentList               = list[Argument]
TypedParameterList         = tuple[TypedParameter, ...]

OptionalArgumentList       = PTH.Optional[ArgumentList]
OptionalTypedParameterList = PTH.Optional[TypedParameterList]

@dataclass
class ReturnType(AIGRNode):
    """The returntype of a callable -- basically a type, but wrapped in an AIGRNode (so its an attr)"""
    _: KW_ONLY
    type  : types._types # An AIGR-type

