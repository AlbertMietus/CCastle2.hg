# (C) Albert Mietus, 2023. Part of Castle/CCastle project
from __future__ import annotations
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .protocols import Protocol
from .aid import TypedParameter                                                                      # Castle/AIGR types

__all__ = ['PortDirection', 'Port', 'ComponentInterface']

class PortDirection(Enum):
    """Ports always have a direction; most port are ``Out`` (sending)  or ``In``(receiving)``.

    More options are (will become) possible, like master/slave and bidir(ectional)"""

    Unknown = 0
    In      = 1
    Out     = 2
    Bidir   = 3 # Not supported yet
    Bidirectional = Bidir
    Master  = 4 # Not supported yet
    Slave   = 5 # Not supported yet

PortType = PTH.Union[ Protocol, type]

@dataclass
class Port(AIGR):
    """.. note ::

          * ``Port``s do *not* inherit
          * A `Port` has a type, like Event -- basically a protocol
"""
    name: str
    _: KW_ONLY
    direction: PortDirection
    type: PortType


@dataclass
class ComponentInterface(AIGR):
    name: str
    _: KW_ONLY
    based_on: PTH.Optional[ComponentInterface]=dc_field(default_factory= lambda: baseComponent)
    ports: PTH.Sequence[Port]=()


baseComponent=ComponentInterface("Component", based_on=None, ports=())   #XXX Add base-ports
