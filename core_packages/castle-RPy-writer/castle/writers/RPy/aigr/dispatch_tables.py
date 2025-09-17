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
    code-generation. Therefore it is collectred in this (temporally/local) structure: the DispatchTable (and sub-classes).
    """

    _ : KW_ONLY
    comp        :ID
    port        :ID
    parentTable :PTH.Optional[ID]=None


@dataclass
class EventDispatchTable(_DispatchTable):

    _: KW_ONLY
    map  :PTH.Optional[dict[ID, str]] = dc_field(default_factory= lambda: dict())


class DispatchTable_Scaffolder(_Scaffolder):
    _nodeCls:type = _DispatchTable
    ...
class EventDispatchTable_Scaffolder(DispatchTable_Scaffolder):
    _nodeCls:type = EventDispatchTable
    ...

def Build_EventDispatchTable(comp :aigr.ComponentImplementation, port :aigr.Port) ->EventDispatchTable_Scaffolder:
    handlders = [ h for h in comp.handlers if isinstance(h, aigr.EventHandler) and h.port == port.name ]

    table = EventDispatchTable(comp=comp.name, port=port.name,
                                   map={h.name: h for h in handlders}) # XXX parentTable?)
    return EventDispatchTable_Scaffolder(node=table)

