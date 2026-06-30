# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for the ``castle.aigr.machinery`` package.
# Hand-maintained "manual autodoc" companion to machinery/__init__.py.
#
# This models the ABSTRACT machinery as an interface/facade -- *what* happens
# (e.g. sending an event between components), not *how*. Compare ``EventOverPort``
# with the intra-component ``Call`` expression / ``VoidCall`` statement.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from .. import ID as ID, AIGR as AIGR, Port as Port, Event as Event, Argument as Argument, ComponentInterface as ComponentInterface
from ..statements import _statement as _statement
from .. import todo as todo

@dataclass
class _machinery(AIGR):
    """Base of the abstract machinery nodes."""
    _: KW_ONLY

@dataclass
class _send_proto(_machinery, _statement):
    """Base for 'send' machinery, from the sending component ``comp``."""
    _: KW_ONLY
    comp: ID.Ref[ComponentInterface]

@dataclass
class _send_ToSub(_send_proto):
    """A send aimed at a sub-component ``receiver`` (no port connection)."""
    _: KW_ONLY
    receiver: ID.Ref[ComponentInterface]

@dataclass
class _send_OverPort(_send_proto):
    """A send that leaves through an ``outport``."""
    _: KW_ONLY
    outport: ID.Ref[Port]

@dataclass
class _sendEvent(_machinery):
    """A send carrying an ``event`` reference and its ``arguments``."""
    _: KW_ONLY
    event: ID.Ref[Event]
    arguments: PTH.Sequence[Argument]

@dataclass
class _sendStream(todo.mark_Dataclass):
    """Stream send (not implemented yet)."""

@dataclass
class _sendData(todo.mark_Dataclass):
    """Data send (not implemented yet)."""

@dataclass
class EventToSub(_send_ToSub, _sendEvent):
    """Send an event to a named sub-component."""

@dataclass
class EventOverPort(_send_OverPort, _sendEvent):
    """Send an event over an outport (to another, connected component)."""

@dataclass
class connection(_machinery):
    """A wire connecting an ``outport`` to an ``inport``."""
    _: KW_ONLY
    outport: Port
    inport: Port
