# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.protocols``.
# Hand-maintained "manual autodoc" companion to protocols.py.

import typing as PTH
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from .events import Event as Event
from .base.names import ID as ID
from .aid import TypedParameter as TypedParameter
from .nodes import NamedNode as NamedNode, Specialise as Specialise

logger: PTH.Any

__all__ = ['ProtocolKind', 'Protocol', 'EventProtocol']

class ProtocolKind(Enum):
    """The kind of a :class:`Protocol` (event/data/stream), stored as a small enum."""
    Unknown = 0
    Event = 1
    Data = 2
    Stream = 3
    _unset = -1

@dataclass
class Protocol(NamedNode):
    """Base class for protocols -- use a concrete subclass (currently :class:`EventProtocol`).

    A protocol has a ``kind``, an optional ``based_on`` reference (an
    ``ID.Ref`` to the protocol/specialisation it extends) and optional
    ``typedParameters``.
    """
    _: KW_ONLY
    kind: ProtocolKind
    based_on: PTH.Optional[ID.Ref[Protocol | Specialise]] = ...
    typedParameters: PTH.Optional[PTH.Sequence[TypedParameter]] = ...

@dataclass
class DataProtocol(Protocol):
    """A data protocol (placeholder -- not yet implemented; not exported)."""

@dataclass
class StreamProtocol(Protocol):
    """A stream protocol (placeholder -- not yet implemented; not exported)."""

@dataclass
class EventProtocol(Protocol):
    """A protocol that is, essentially, a set of :class:`Event`.

    Only the *new* events are recorded in ``events``; inherited events come from
    the ``based_on`` protocol and are not copied. ``kind`` defaults to
    ``ProtocolKind.Event``::

        EventProtocol("Clock", events=(Event("tick"),))
    """
    _: KW_ONLY
    kind: ProtocolKind = ...
    events: PTH.Sequence[Event]
