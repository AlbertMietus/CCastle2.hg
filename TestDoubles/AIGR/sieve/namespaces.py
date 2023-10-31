# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import NameSpace, Source_NS, GENERATED, ID

start_sieve  = Source_NS(ID('start_sieve'),  source=GENERATED)
slow_start   = Source_NS(ID('slow_start'),   source=GENERATED)
simple_sieve = Source_NS(ID('simple_sieve'), source=GENERATED)


from . import protocols

start_sieve.register(protocols.StartSieve)
slow_start.register(protocols.SlowStart)
simple_sieve.register(protocols.SlowStart_1)
simple_sieve.register(protocols.SimpleSieve)

from ..base import base
for all in (start_sieve, slow_start, simple_sieve): all.register(base)


top = NameSpace(ID('TheSieve'))
top.register(start_sieve)
top.register(slow_start)
top.register(simple_sieve)
top.register(base)
