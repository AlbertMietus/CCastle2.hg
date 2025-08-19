# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

#from .dispatch_tables import _DispatchTable

from castle import aigr
from castle.aigr import ID

###
### DispatchTable(s)
### ---------------
### Isn't that a implementation detail, for a writer?
### Now we scaffolding-register all (event)Handers, and put them in .handers in ComponentImplementation.
### That list has all info: Each eventhandler knows about it protocol/event and port.
### The writer can use that directly, or creata a local DispatchTable fist.

#@dataclass
#class EventDispatchTable(_DispatchTable):
#    """An EventDispatchTable is, like any _DispatchTable, a mapping from incoming events (within a protocol) to a Eventhandler."""
#
#    _: KW_ONLY
#    map: PTH.Optional[dict[ID, str]] = dc_field(default_factory= lambda: dict())



# LocalWords:  EventHandler  EventDispatchTable
