# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from castle.aigr import AIGR, ID

@dataclass
class _DispatchTable(AIGR):
    _: KW_ONLY
    # XXX One day, we will find the following  by the AIRG-as-tree
    _comp : ID                             ### ./../../@name 	ComponentImplementation-ID
    _port : ID                             ### ./../@name 		Port-ID
    _parentTable : PTH.Optional[ID]=None   ### ???  <zie whiteboard>


@dataclass
class EventDispatchTable(_DispatchTable):

    _: KW_ONLY
    map: PTH.Optional[dict[ID, str]] = dc_field(default_factory= lambda: dict())
