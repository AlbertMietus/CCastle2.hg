# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" XXX ToDo: Test, Refactor, Split & Doc"""

from __future__ import annotations
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR
from .protocols import Protocol
from .base.names import ID
from .nodes import NamedNode

__all__ = ['PortDirection', 'Port', 'ComponentInterface']


class PortDirection(Enum):
    """Ports always have a direction; most port are ``Out`` (sending)  or ``In``(receiving)``.

    More options are (will become) possible, like master/slave and bidir (=bidirectional)"""

    Unknown = 0
    In      = 1
    Out     = 2
    Bidir   = 3 # Not supported yet
    Bidirectional = Bidir
    Master  = 4 # Not supported yet
    Slave   = 5 # Not supported yet

PortType = PTH.Union[Protocol, type]


@dataclass
class Port(AIGR): # Note: not a NamedNode, as it does not live in a NS (but in a Component)
    """.. note ::

          * ``Port``s do *not* inherit
          * A `Port` has a type, like Event -- basically a protocol
"""
    _kids = AIGR._kids + ('name', 'direction', 'type')

    name: str
    _: KW_ONLY
    direction: PortDirection
    type: PortType


@dataclass
class ComponentInterface(NamedNode):
    _kids = NamedNode._kids + ('based_on', 'ports')

    _: KW_ONLY
    based_on: PTH.Optional[ComponentInterface]=dc_field(default_factory= lambda: baseComponent)  #type: ignore[has-type]
    ports: PTH.Sequence[Port]=()


_rootComponent=ComponentInterface(ID("RootComponent"), based_on=None, ports=())   # The base of the baseComponent
baseComponent=ComponentInterface(ID("Component"), based_on=_rootComponent, ports=())   #XXX Add base-ports

