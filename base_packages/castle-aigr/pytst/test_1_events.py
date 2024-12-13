# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from castle.aigr import Event
from castle.aigr import TypedParameter
from castle.aigr import types

def test_0_Event_empty():
    e = Event("leeg_event")
    assert e.name                 == 'leeg_event'
    assert e.return_type          is None
    assert len(e.typedParameters) == 0

def test_1_Event_small():
    e = Event("demo_int", typedParameters=[TypedParameter(name='p1', type=types.float )])
    assert e.return_type             is None
    assert len(e.typedParameters)    == 1
    assert e.typedParameters[0].name == 'p1'
    assert e.typedParameters[0].type == types.float

def test_2_Event_retunInt():
    e = Event("an_event", return_type=types.int)
    assert e.return_type == types.int
