# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.statements.defs``.
# Hand-maintained "manual autodoc" companion to defs.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from . import _statement as _statement, AIGR as AIGR
from ..nodes import NamedNode as NamedNode
from ..base import types as types
from ..namespaces import _hasScope as _hasScope
from ..interfaces import ComponentInterface as ComponentInterface
from ..aid import TypedParameter as TypedParameter
from .callables import _handlers as _handlers

@dataclass
class ComponentImplementation(_hasScope, _statement, NamedNode):
    """The implementation of a component (Castle keyword ``implement``).

    Links to its ``interface`` (a :class:`ComponentInterface`), its
    ``parameters`` and the list of ``handlers`` (registered one by one). Its
    ``{ ... }`` is a *namespace/scope* (``_hasScope``), not a plain ``Body``.
    """
    _: KW_ONLY
    interface: PTH.Optional[ComponentInterface] = ...
    parameters: tuple[TypedParameter, ...] = ...
    handlers: list[_handlers] = ...

@dataclass
class VariableDefintion(_statement, NamedNode):
    """Define/declare a variable (usually inside a component).

    Has an AIGR ``type`` and an optional initial ``value`` (an AIGR node).
    (Note: the class name keeps the source spelling ``VariableDefintion``.)
    """
    _: KW_ONLY
    type: types._types
    value: PTH.Optional[AIGR] = ...
