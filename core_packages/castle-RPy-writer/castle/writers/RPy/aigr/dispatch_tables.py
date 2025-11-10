# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from castle  import aigr
from castle.aigr import AIGR, ID

from castle.aigr_extra.scaffolding._scaffolder import _Scaffolder


@dataclass
class _DispatchTable(AIGR):
    """A DispatchTable is a mapping between *triggers*on a specific port (like an `Event`), and the (event)Handler that handle it.

    This information is available in the (general) AIGR, in  ComponentImplementation.handlers. But that isn't convenient for
    code-generation. Therefore it is collectred in this (temporally/local) `_DispatchTable` structures (and sub-classes).
    """

    _ : KW_ONLY
    comp        :ID
    port        :ID
    map         :PTH.Optional[dict] = dc_field(default_factory= lambda: dict())  # general map -- see subclasses for definitions
    parentTable :PTH.Optional[ID]=None

ProtocolName = str                                # Alias for aigr.Protocol.name
EventName    = str                                # Alias for aigr.Event.name
HandlerName  = str                                # Alias for aigr.(Event)Handler.name

@dataclass
class EventDispatchTable(_DispatchTable):
    """The DispatchTable with EventHandler; maps from (name of) Protocol.Event to (name of) EventHandler"""

    _ : KW_ONLY
    map: dict[PTH.Tuple[ProtocolName, EventName], HandlerName] # port is the same for all.


class DispatchTable_Scaffolder(_Scaffolder):
    _nodeCls:type = _DispatchTable
    ...
class EventDispatchTable_Scaffolder(DispatchTable_Scaffolder):
    _nodeCls:type = EventDispatchTable
    ...

def Build_EventDispatchTable(comp :aigr.ComponentImplementation, port_name :ID) ->EventDispatchTable_Scaffolder:
    handlders = [ h for h in comp.handlers if isinstance(h, aigr.EventHandler) and h.port == port_name]

    table = EventDispatchTable(comp=PTH.cast(ID, comp.name), port=port_name,
                                   map={(h.protocol, h.event): h.name for h in handlders},
                                   parentTable=None) #XXX
    logger.warning('HARD_CODED: Build_EventDispatchTable(... parentTable=None) for: %s', table)
    return EventDispatchTable_Scaffolder(node=table)

