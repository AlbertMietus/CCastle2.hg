# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR
from ..nodes import NamedNode
from .compounds import Body
from castle.aigr import types
from ..namespaces import _hasScope

if PTH.TYPE_CHECKING:                                                                                # pragma: no cover
    from .. import ComponentInterface, TypedParameter



@dataclass
class ComponentImplementation(_hasScope, _statement, NamedNode):
    """The implementation of a component (keyword: 'implement')

    .. note :: Although a Component( Implementation) uses '{' ... '}' that is not a ``Body``, but a `namespace` --see _hasScope
    """
    _: KW_ONLY

    interface  : PTH.Optional[ComponentInterface] = None
    parameters : tuple[TypedParameter, ...]       = dc_field(default_factory=tuple)

## Method, Eventhandler, etc  are defined in :file:`callables.py`

@dataclass
class VariableDefintion(_statement, NamedNode):
    """Define/Declare a variable, usually in a component
    """
    _: KW_ONLY

    type   : types # An AIGR-type
    value  : PTH.Optional[AIGR]=None
