# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import EventProtocol, Event, ID
from castle.aigr.aid import TypedParameter, Argument, Specialise


StartSieve = EventProtocol(ID('StartSieve'),
                              events=(
                                   Event(name=ID('runTo'),  return_type=None, typedParameters=(TypedParameter(name='max', type=int),)),
                                   Event(name=ID('newMax'), return_type=None, typedParameters=(TypedParameter(name='max', type=int),))))


SlowStart = EventProtocol(ID('SlowStart'),
                              typedParameters=(TypedParameter(name='queue_max', type=int),),
                              events=(
                                   Event(name=ID('setMax'), return_type=None, typedParameters=(TypedParameter(name='queue_max', type=int),)),))

SlowStart_1 = Specialise(ID("SlowStart_1"),
                              based_on=SlowStart,
                              #OR: arguments=(Argument(name=queue_max, value=1),))
                              arguments=(Argument(value=1),))

SimpleSieve = EventProtocol(ID('SimpleSieve'),
                              based_on=SlowStart_1,
                              events=(
                                   Event(name=ID('input'), return_type=None, typedParameters=(TypedParameter(name='try', type=int),)),))


