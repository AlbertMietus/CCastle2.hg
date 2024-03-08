# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" See ./ReadMe.rst"""

from __future__ import annotations
import typing as PTH                                                                                 # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .events import Event
from .aid import TypedParameter, Argument                                                            # Castle/AIGR types
from .namednodes import NamedNode, ID



__all__ = ['ProtocolKind', 'Protocol', 'EventProtocol']
# DataProtocol, StreamProtocol are added/implemented later
# Do Not Export: _RootProtocol
# How about:  ProtocolWrapper?

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
    based_on         :PTH.Optional[Protocol]=dc_field(default_factory= lambda :Protocol._BASE)      # pragma: no mutate
    typedParameters  :PTH.Optional[PTH.Sequence[TypedParameter]]=()


@dataclass                                                                                          # pragma: no mutate
class _RootProtocol(Protocol):
    """This is the base protocol; it exist as we can't instantiate Protocol"""

baseProtocol = _RootProtocol(ID("Protocol"), kind=ProtocolKind.Unknown, based_on=None)                  # pragma: no mutate
Protocol._BASE=baseProtocol

@dataclass                                                                                          # pragma: no mutate
class DataProtocol(Protocol): pass ### XXX ToDo (not exported)
@dataclass                                                                                          # pragma: no mutate
class StreamProtocol(Protocol): pass ### XXX ToDo (not exported)

@dataclass                                                                                          # pragma: no mutate
class ProtocolWrapper(Protocol):
    _: KW_ONLY
    kind : ProtocolKind=ProtocolKind._unset
    arguments: PTH.Sequence[Argument]

    def __post_init__(self):
        if self.kind is ProtocolKind._unset:
            self.kind = self.based_on.kind
        if self.name == "":
            self.name = f"Wrapper for {self.based_on.name}({self.arguments})" ###

# GAM: When based_on is a Protocol, delegate to self.based_on isn;t needed. When move to generic wrappper, it is ?
#    def __getattr__(self, name):                                        ### XXX move to Wrapper Base?
#        """delegate "everything" to `.`based_on``!
#        Kind of inherit, but not to superclass (Protocol), but to the instance (a Protocol) that is wrapped"""
#
#        return getattr(self.based_on, name)


@dataclass                                                                                          # pragma: no mutate
class EventProtocol(Protocol):
    """An event-based protocol is basically a set of events.

    This recorded as an dyn-array of the new event; there is no need to copy the inherited ones
    """
    _: KW_ONLY
    kind: ProtocolKind = ProtocolKind.Event
    events: PTH.Sequence[Event]
    #redefine EventProtocol always inherit from an EventProtocol (or Wrapper)
    based_on: EventProtocol|ProtocolWrapper = dc_field(default_factory= lambda :Protocol._BASE)

    def _noEvents(self):
        inherited = self.based_on._noEvents() if isinstance(self.based_on, EventProtocol) else 0
        return inherited + len(self.events)

    def eventIndex(self, event: Event) -> int:
        try:
            return self.based_on.eventIndex(event)
        except ValueError: # not inherited
            inherited_events = self.based_on._noEvents()
        except AttributeError: # self.based_on === None
            inherited_events = 0
        # `event` not inherited: search locally and number of inherited events
        return self.events.index(event) + inherited_events
