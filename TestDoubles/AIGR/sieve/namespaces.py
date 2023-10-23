# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import  Source_NS, GENERATED

start_sieve  = Source_NS('start_sieve',  source=GENERATED)
slow_start   = Source_NS('slow_start',   source=GENERATED)
simple_sieve = Source_NS('simple_sieve', source=GENERATED)


from . import protocols

start_sieve.register(protocols.StartSieve)
slow_start.register(protocols.SlowStart)
simple_sieve.register(protocols.SlowStart_1)
simple_sieve.register(protocols.SimpleSieve)

from ..base import base
