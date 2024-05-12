# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR, NamedNode

if PTH.TYPE_CHECKING:
    from .. import Body, ComponentInterface, TypedParameter

@dataclass
class _callable(_statement):
    """A callable is like a function, but more generic; this includes methods, (event)handlers, etc.

    Most callable(s) have a name, but not all -- therefor it's not a NamedNode
    """
    _kids = _statement._kids + ('parameters', 'body')

    _ : KW_ONLY
    parameters : tuple[TypedParameter, ...]       = dc_field(default_factory=tuple)
    body       : PTH.Optional[Body]               = None
    returns    : PTH.Optional[PTH.Any]            = None # XXX ToDo

@dataclass
class _Named_callable(NamedNode, _callable):
    _kids = NamedNode._kids + tuple(k for k in _callable._kids if not k in NamedNode._kids)


@dataclass
class Method(_Named_callable):
    #_kids = _Named_callable
    pass
