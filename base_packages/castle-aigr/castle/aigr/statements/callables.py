# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from ..namespaces import _hasScope

from . import _statement, NamedNode

from .compounds import Body
if PTH.TYPE_CHECKING:                                                                                # pragma: no cover
    from .. import TypedParameter, ReturnType
    from .. import ID


@dataclass
class _callable(_hasScope, _statement):
    """A callable is like a function, but more generic; this includes methods, (event)handlers, etc.

    Most callable(s) have a name, but not all -- therefor it's not a NamedNode
    """

    _ : KW_ONLY
    parameters : tuple[TypedParameter, ...]       = dc_field(default_factory=tuple)
    body       : PTH.Optional[Body]               = dc_field(default_factory=Body)
    returns    : PTH.Optional[ReturnType]         = None


@dataclass
class _Named_callable(NamedNode, _callable): pass

@dataclass
class Method(_Named_callable): pass

@dataclass
class Initializer(Method): """A special Method to __init__ the class"""

class _handlers(_Named_callable): pass

@dataclass
class EventHandler(_handlers):
    """An Eventhandler-callable is activated when the specified protocol-event, is received on the given port.

    As CastleCode allows 'default' for all three parts, None is also valid (but not default).

    Like all Named-handlers, it has a name(*), some parameters and a body. It returns typical nothing (None).
    The 'name' however, is special: it is a blend of the protocol, the event and the port. It is advices to use
    ``mangle_event_handler()`` to compute it.
    That file :ref:`castle.aigr_extra.blend.mangle` is also the  correct specification.

    .. warning:: The protocol/event/port are IDs with `Ref` context (empty or with path to real objects. Not those objects themself!
    """

    _ : KW_ONLY
    protocol  : ID
    event     : ID
    port      : ID                        #XXX move to _handlers


