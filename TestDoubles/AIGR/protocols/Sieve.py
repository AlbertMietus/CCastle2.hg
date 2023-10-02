# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr.types import TypedParameter
from castle.aigr import EventProtocol, Event

import pytest

StartSieve = EventProtocol('StartSieve',
                               events=[
                                   Event(name='runTo',  return_type=None, typedParameters=(TypedParameter(name='max', type=int),)),
                                   Event(name='newMax', return_type=None, typedParameters=(TypedParameter(name='max', type=int),))])


SlowStart = EventProtocol('SlowStart',
                              typedParameters=(TypedParameter(name='queue_max', type=int),),
                              events=[
                                   Event(name='setMax', return_type=None, typedParameters=(TypedParameter(name='queue_max', type=int),))],
                              )


