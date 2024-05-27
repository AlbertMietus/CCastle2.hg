# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
from dataclasses import dataclass, KW_ONLY
#from dataclasses import field as dc_field

import typing as PTH                                                                                  # Python TypeHints

from .. import AIGR, Port, Event, Argument, Protocol

from .. import todo

@dataclass
class machinery(AIGR):
    _: KW_ONLY
    delegate : implementation = None

implementation : PTH.TypeAlias = PTH.Optional[type[machinery]] # pragma: no mutate

@dataclass
class send_proto(machinery):
    _: KW_ONLY
    outport : AIGR # ID | Parts| ...

@dataclass
class sendStream(send_proto, todo.mark_Dataclass): ...
@dataclass
class sendData(send_proto, todo.mark_Dataclass): ...

@dataclass
class sendEvent(send_proto):
    _: KW_ONLY
    event: AIGR # ID | Parts| ...
    arguments: PTH.Sequence[Argument]

@dataclass
class connection(machinery):
    _: KW_ONLY
    outport: Port
    inport: Port

@dataclass
class DispatchTable(machinery):
    _: KW_ONLY
    handlers : PTH.Sequence[Handler] # XXX Handlers not yet defined
Handler = todo.Typing #XXX Weet nog niet waar/wanneer (Event)Handlers in de AIGR komen

@dataclass
class eDispatchTable(DispatchTable):
    _: KW_ONLY
