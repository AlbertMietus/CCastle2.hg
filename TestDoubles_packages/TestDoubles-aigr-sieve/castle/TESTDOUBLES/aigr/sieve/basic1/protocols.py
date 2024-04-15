# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import EventProtocol, Event, ID
from castle.aigr import TypedParameter, Argument, Specialise

import typing as PTH                                                                                 # Python TypeHints

"""protocol StartSieve : EventProtocol {
     runTo(int:max);
     newMax(int:max);
   }"""
StartSieve = EventProtocol(ID('StartSieve'),
                              events=(
                                   Event(name=ID('runTo'),  return_type=None, typedParameters=(TypedParameter(name='max', type=int),)),
                                   Event(name=ID('newMax'), return_type=None, typedParameters=(TypedParameter(name='max', type=int),))))

"""protocol SimpleSieve : EventProtocol {
     input(int:try);
   }"""
SimpleSieve = EventProtocol(ID('SimpleSieve'),
                              events=(
                                   Event(name=ID('input'), return_type=None, typedParameters=(TypedParameter(name='try', type=int),)),))


