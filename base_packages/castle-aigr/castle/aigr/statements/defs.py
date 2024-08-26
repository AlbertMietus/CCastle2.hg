# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR
from ..nodes import NamedNode

if PTH.TYPE_CHECKING:                                                                                # pragma: no cover
    from .. import Body, ComponentInterface, TypedParameter

@dataclass
class ComponentImplementation(_statement, NamedNode):
    """The implementation of a component (keyword: 'implement'
    """
    _kids = _statement._kids + ('interface', 'parameters', 'body')
    _: KW_ONLY

    interface  : PTH.Optional[ComponentInterface] = None
    parameters : tuple[TypedParameter, ...]       = dc_field(default_factory=tuple)
    body       : PTH.Optional[Body]               = None

## Method, Eventhandler, etc  are defined in :file:`callables.py`

@dataclass
class VariableDefintion(_statement, NamedNode):
    """Define/Declare a variable, usually in a component
    """
    _kids = _statement._kids + ('name',) + ('type', 'value')
    _: KW_ONLY

    type   : type                                  # XXX ToDo: Really `type`? A python type?
    value  : PTH.Optional[AIGR]=None
