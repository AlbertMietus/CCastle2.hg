# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import EventProtocol, Event
from castle.aigr.protocols import ProtocolWrapper
from castle.aigr.aid import TypedParameter, Argument


StartSieve = EventProtocol('StartSieve',
                              events=(
                                   Event(name='runTo',  return_type=None, typedParameters=(TypedParameter(name='max', type=int),)),
                                   Event(name='newMax', return_type=None, typedParameters=(TypedParameter(name='max', type=int),))))

SlowStart = EventProtocol('SlowStart',
                              typedParameters=(TypedParameter(name='queue_max', type=int),),
                              events=(
                                   Event(name='setMax', return_type=None, typedParameters=(TypedParameter(name='queue_max', type=int),)),))

SlowStart_1 = ProtocolWrapper("SlowStart_1",
                              based_on=SlowStart,
                              #arguments=(Argument(name=queue_max, value=1),))
                              arguments=(Argument(value=1),))

SimpleSieve = EventProtocol('SimpleSieve',
                              based_on=SlowStart_1,
                              events=(
                                   Event(name='input', return_type=None, typedParameters=(TypedParameter(name='try', type=int),)),))


