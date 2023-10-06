# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr.aid import TypedParameter
from castle.aigr import ComponentInterface
from castle.aigr import Port, PortDirection

from . import protocols

SieveMoat = ComponentInterface(name="Sieve",
                                   ports=(
                                       Port(name='try',     direction=PortDirection.In,  type=protocols.SimpleSieve),
                                       Port(name='coprime', direction=PortDirection.Out, type=protocols.SimpleSieve),
                                       ))

