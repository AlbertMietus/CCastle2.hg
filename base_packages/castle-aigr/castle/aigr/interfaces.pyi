# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.interfaces``.
# Hand-maintained "manual autodoc" companion to interfaces.py.

import typing as PTH
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from .protocols import Protocol as Protocol
from .base.names import ID as ID
from .nodes import NamedNode as NamedNode, Specialise as Specialise

__all__ = ['PortDirection', 'Port', 'ComponentInterface']

class PortDirection(Enum):
    """Direction of a :class:`Port`.

    Usually ``In`` (receiving) or ``Out`` (sending). ``Bidir`` and
    master/slave variants are reserved for future use.
    """
    Unknown = 0
    In = 1
    Out = 2
    Bidir = 3
    Bidirectional = Bidir
    BiDirectional = Bidir
    Master = 4
    Slave = 5

PortType = PTH.Union[Protocol, type]
"""What a :class:`Port` is typed by -- a :class:`Protocol` (or a raw ``type``)."""

@dataclass
class Port(NamedNode):
    """A named connection point of a component, with a ``direction`` and a ``type``.

    A port does *not* inherit; its type is typically an event protocol. The
    port's ``ID`` is registered in the owning component's interface namespace::

        Port("clk", direction=PortDirection.In, type=clock_protocol)
    """
    _: KW_ONLY
    direction: PortDirection
    type: PortType

@dataclass
class ComponentInterface(NamedNode):
    """The *interface* of a component: the protocol it extends and its ports.

    ``based_on`` is an optional ``ID.Ref`` to the protocol/specialisation it
    builds on; ``ports`` is a sequence of ``ID.Ref`` to its :class:`Port`
    nodes (stored in the component's namespace).
    """
    _: KW_ONLY
    based_on: PTH.Optional[ID.Ref[Protocol | Specialise]] = ...
    ports: PTH.Sequence[ID.Ref[Port]] = ...
