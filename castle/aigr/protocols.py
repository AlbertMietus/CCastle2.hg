# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" This file is based (a fork) on `../writers/CC2Cpy/Protocol.py`,
  - the rendering part is removed
  - the prefixed are gone
  - better
TODO: update the CC2Cpy parts to use this generic AIGR layer
"""

from enum import Enum
from dataclasses import dataclass, KW_ONLY
from . import AIGR
from .events import Event

__all__ = ['ProtocolKind', 'Protocol', 'EventProtocol']
# DataProtocol, StreamProtocol are added eventually


class ProtocolKind(Enum):
    """There are several kinds (types) of protocols.

       This can be modeled by subclassing (in langueas that support it), or
       by using a low-int (aka a enum) and save that in the struct"""
    Unknown  = 0
    Event    = 1
    Data     = 2
    Stream   = 3


Protocol: TypeAlias = 'Protocol'            # forward reference                                      # pragma: no mutate
@dataclass
class Protocol(AIGR):
    """ .. note:: Use one of the subclasses -- Only Event is defined yet
        .. todo:: Design: What is the `kind` self and the inherited ones are not the same?
                  overriding ProtocolKind.Unknown is always allowed
    """
    _BASE: ClassVar=None                                                                             # pragma: no mutate

    name: str
    kind: ProtocolKind
    based_on: Optional[Protocol]=dc_field(default_factory= lambda :Protocol._BASE)


@dataclass
class _RootProtocol(Protocol):
    """This is the base protocol; it exist as we can't instantiate Protocol"""

baseProtocol = _RootProtocol("Protocol", kind=ProtocolKind.Unknown, based_on=None)                   # pragma: no mutate
Protocol._BASE=baseProtocol

@dataclass                                                                                           # pragma: no mutate
class DataProtocol(Protocol): pass ### XXX ToDo (not exported)
@dataclass                                                                                           # pragma: no mutate
class StreamProtocol(Protocol): pass ### XXX ToDo (not exported)


@dataclass                                                                                           # pragma: no mutate
class EventProtocol(Protocol):
    """An event-based protocol is basically a set of events.

    This recorded as an dyn-array of the new event; there is no need to copy the inherited ones
    """
    _: KW_ONLY
    kind: ProtocolKind = ProtocolKind.Event
    events: Sequence[Event]

