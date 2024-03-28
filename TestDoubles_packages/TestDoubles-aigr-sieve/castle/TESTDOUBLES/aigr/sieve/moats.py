# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This manual crafted AIGR (a TestDoubles) is for the "base version" of the Sieve [#1]_.
   It does NOT uses SlowStart -- nor does solve the Heisenbug [2]_

   .. [#1] http://docideas.mietus.nl/en/default/CCastle/4.Blog/1.TheSieve.html
   .. [#2] http://docideas.mietus.nl/en/default/CCastle/4.Blog/2.Heisenbug.html
"""

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
SieveMoat = ComponentInterface(name=ID("Sieve"),
                                   ports=(
                                       Port(name='try',     direction=PortDirection.In,  type=protocols.SimpleSieve),
                                       Port(name='coprime', direction=PortDirection.Out, type=protocols.SimpleSieve),
                                       ))


# component Finder : Component {
#   port SimpleSieve<in>:newPrime;
#   port SimpleSieve<out>:found;
# }
FinderMoat = ComponentInterface(name=ID("Finder"),
                                    ports=(
                                        Port(name='newPrime', direction=PortDirection.In,  type=protocols.SimpleSieve),
                                        Port(name='found',    direction=PortDirection.Out, type=protocols.SimpleSieve),
                                       ))




