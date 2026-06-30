# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.aid``.
# Hand-maintained "manual autodoc" companion to aid.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from . import AIGRNode as AIGRNode
from .base.names import ID as ID
from .base import types as types
from .nodes import NamedNode as NamedNode

@dataclass
class TypedParameter(NamedNode):
    """A named, typed *parameter* in a callable **definition** (a formal argument).

    It behaves like a local variable inside the body. Build one with a name
    (plain ``str`` is auto-wrapped into an :class:`ID`) and an AIGR ``type``::

        TypedParameter("n", types.int)
    """
    name: ID | str
    type: types._types
    def __post_init__(self) -> None: ...

@dataclass
class Argument(AIGRNode):
    """A value passed at a callable **invocation** (an actual argument).

    Supports positional and named arguments: pass just ``value`` for positional,
    or also ``name=`` for a keyword argument (a ``str`` name is wrapped into an
    :class:`ID`).
    """
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str] = ...
    def __post_init__(self) -> None: ...

ArgumentList = list[Argument]
"""A list of :class:`Argument` (call-site arguments)."""
TypedParameterList = tuple[TypedParameter, ...]
"""An immutable tuple of :class:`TypedParameter` (definition parameters)."""
OptionalArgumentList = PTH.Optional[ArgumentList]
OptionalTypedParameterList = PTH.Optional[TypedParameterList]

@dataclass
class ReturnType(AIGRNode):
    """The return type of a callable -- an AIGR ``type`` wrapped as a node/attr."""
    _: KW_ONLY
    type: types._types
