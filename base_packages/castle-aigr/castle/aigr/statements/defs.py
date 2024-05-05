# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR
from ..nodes import NamedNode

if PTH.TYPE_CHECKING:
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

