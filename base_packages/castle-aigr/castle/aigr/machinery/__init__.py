# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass, KW_ONLY
#from dataclasses import field as dc_field

import typing as PTH                                                                                  # Python TypeHints

from .. import AIGR, Port, Event, Argument, Protocol
from ..develop import ToDo

@dataclass
class machinery(AIGR):
    _: KW_ONLY
    delegate : implementation = None

implementation : PTH.TypeAlias = PTH.Optional[type[machinery]]

@dataclass
class send_proto(machinery):
    _: KW_ONLY
    outport : Port

@dataclass
class sendStream(send_proto, ToDo): ...
@dataclass
class sendData(send_proto, ToDo): ...

@dataclass
class sendEvent(send_proto):
    event: Event
    arguments: PTH.Sequence[Argument]

@dataclass
class connection(machinery):
    _: KW_ONLY
    outport: Port
    inport: Port

@dataclass
class DispatchTable(machinery):
    _: KW_ONLY
    handlers : PTH.Sequence[Handlers] # XXX Handlers not yet defined

@dataclass
class eDispatchTable(DispatchTable):
    _: KW_ONLY
