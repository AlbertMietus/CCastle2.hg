# (C) Albert Mietus, 2023, 2024. Part of Castle/CCastle project

""" This manual crafted AIGR TestDoubles represent the component-interfaces for basic-1 variant of 'The Sieve'

   .. see also:: :file:`./__init__.py` for a general intro
"""

__all__= ['GeneratorMoat', 'SieveMoat', 'FinderMoat']

from castle.aigr.aid import TypedParameter
from castle.aigr import ComponentInterface, ID
from castle.aigr import Port, PortDirection

from . import protocols


# component Generator : Component {
#   port StartSieve<in>:controll;
#   port SimpleSieve<out>:outlet;
# }
GeneratorMoat = ComponentInterface(name=ID("Generator"),
                                    ports=(
                                        Port(name='controll', direction=PortDirection.In,  type=protocols.StartSieve),
                                        Port(name='outlet',   direction=PortDirection.Out, type=protocols.SimpleSieve),
                                        ))


# component Sieve(onPrime:int) : Component {
#   port SimpleSieve<in>:try;
#   port SimpleSieve<out>:coprime;
# }
port_try     = Port(name='try',     direction=PortDirection.In,  type=protocols.SimpleSieve)
port_coprime = Port(name='coprime', direction=PortDirection.Out, type=protocols.SimpleSieve)
SieveMoat = ComponentInterface(name=ID("Sieve"), ports=(port_try, port_coprime))


# component Finder : Component {
#   port SimpleSieve<in>:newPrime;
#   port SimpleSieve<out>:found;
# }
FinderMoat = ComponentInterface(name=ID("Finder"),
                                    ports=(
                                        Port(name='newPrime', direction=PortDirection.In,  type=protocols.SimpleSieve),
                                        Port(name='found',    direction=PortDirection.Out, type=protocols.SimpleSieve),
                                       ))




