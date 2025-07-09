# (C) Albert Mietus, 2024, 2025 Part of Castle/CCastle project #XXX OLDXXX

""" This file models the ABSTRACT machinery, as an facade/interface -- not how it works.

For example: Sending an event from one component to another is represented by ``machinery.sendEvent()``. One can compare
this with the ``Call`` expression, and the ``VoidCall`` statements (which act only *inside* a component.

-- Albert, 9/Jul/2025 """

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass, KW_ONLY
#from dataclasses import field as dc_field

import typing as PTH                                                                                  # Python TypeHints

from .. import AIGR, Port, Event, Argument, Protocol
from ..statements import _statement
from .. import todo

@dataclass
class _machinery(AIGR):
    _: KW_ONLY

@dataclass
class _send_proto(_machinery, _statement):
    _: KW_ONLY
    outport : AIGR # ID | Parts | ...

@dataclass
class sendStream(_send_proto, todo.mark_Dataclass): ...
@dataclass
class sendData(_send_proto, todo.mark_Dataclass): ...

@dataclass
class sendEvent(_send_proto):
    _: KW_ONLY
    event: AIGR # ID | Parts | ...
    arguments: PTH.Sequence[Argument]

@dataclass
class connection(_machinery):
    _: KW_ONLY
    outport: Port
    inport: Port
