# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" See ./ReadMe.rst"""

from __future__ import annotations

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import AIGR
from .events import Event
from .base.names import ID
from .aid import TypedParameter, Argument # XXXX                                                            # Castle/AIGR types
from .nodes import NamedNode, Specialise



__all__ = ['ProtocolKind', 'Protocol', 'EventProtocol']
# DataProtocol, StreamProtocol are added/implemented later
# Do Not Export: _RootProtocol


class ProtocolKind(Enum):
    """There are several kinds (types) of protocols.

       This can be modeled by subclassing (in langueas that support it), or
       by using a low-int (aka a enum) and save that in the struct"""
    Unknown  = 0
    Event    = 1
    Data     = 2
    Stream   = 3
    _unset  = -1

@dataclass
class Protocol(NamedNode):
    """ .. note:: Use one of the subclasses -- Only Event is defined yet
        .. todo:: Design: What is the `kind` self and the inherited ones are not the same?
                  overriding ProtocolKind.Unknown is always allowed
    """
    _BASE: PTH.ClassVar=None                                                                        # pragma: no mutate

    _: KW_ONLY
    kind             :ProtocolKind
    based_on         :PTH.Optional[Protocol|Specialise]=dc_field(default_factory= lambda :Protocol._BASE)      # pragma: no mutate
    typedParameters  :PTH.Optional[PTH.Sequence[TypedParameter]]=()


@dataclass                                                                                          # pragma: no mutate
class _RootProtocol(Protocol):
    """This is the base protocol; it exist as we can't instantiate Protocol"""

baseProtocol = _RootProtocol(name=ID("Protocol"), kind=ProtocolKind.Unknown, based_on=None)                  # pragma: no mutate
Protocol._BASE=baseProtocol

@dataclass                                                                                          # pragma: no mutate
class DataProtocol(Protocol): pass ### XXX ToDo (not exported)
@dataclass                                                                                          # pragma: no mutate
class StreamProtocol(Protocol): pass ### XXX ToDo (not exported)


@dataclass                                                                                          # pragma: no mutate
class EventProtocol(Protocol):
    """An event-based protocol is basically a set of events.

    This recorded as an dyn-array of the new event; there is no need to copy the inherited."""
    _: KW_ONLY
    kind: ProtocolKind = ProtocolKind.Event
    events: PTH.Sequence[Event]


