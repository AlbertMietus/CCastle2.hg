# (C) Albert Mietus, 2024, 2025 Part of Castle/CCastle project #XXX OLDXXX

""" This file models the ABSTRACT machinery, as an facade/interface -- not how it works.

For example: Sending an event from one component to another is represented by ``machinery.sendEvent()``. One can compare
this with the ``Call`` expression, and the ``VoidCall`` statements (which act only *inside* a component.

-- Albert, 9/Jul/2025 """

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass, KW_ONLY
#from dataclasses import field as dc_field

import typing as PTH                                                                                  # Python TypeHints

from .. import ID
from .. import AIGR, Port, Event, Argument, ComponentInterface
from ..statements import _statement
from .. import todo

@dataclass
class _machinery(AIGR):
    _: KW_ONLY

@dataclass
class _send_proto(_machinery, _statement):
    _: KW_ONLY
    comp    :ID.Ref[ComponentInterface] # the sending component

@dataclass
class _send_ToSub(_send_proto):
    _: KW_ONLY
    receiver :ID.Ref[ComponentInterface] # a sub-component; (no connection)

@dataclass
class _send_OverPort(_send_proto):
    _: KW_ONLY
    outport :ID.Ref[Port]

@dataclass
class _sendEvent(_machinery):
    _: KW_ONLY
    event      :ID.Ref[Event]
    arguments  :PTH.Sequence[Argument]
@dataclass
class _sendStream(todo.mark_Dataclass): ...
@dataclass
class _sendData(todo.mark_Dataclass): ...


@dataclass
class EventToSub(_send_ToSub, _sendEvent):
    "Send an event to a sub-component"

@dataclass
class EventOverPort(_send_OverPort, _sendEvent):
    "Send an event over an outport (to another component)"

@dataclass
class connection(_machinery):
    _: KW_ONLY
    outport: Port # ToDo: ID.Ref[Port]?
    inport: Port  # ToDo: ID.Ref[Port]?

