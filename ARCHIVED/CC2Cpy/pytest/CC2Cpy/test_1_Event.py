# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from . import * # CCompare

from castle.writers.CC2Cpy.Event import * #CC_Event

def test_0_Event_empty():
    e = CC_Event("leeg_event")
    assert e.name                 == 'leeg_event'
    assert e.return_type          is None
    assert len(e.typedParameters) == 0

def test_1_Event_small():
    e = CC_Event("demo_int", typedParameters=[CC_TypedParameter(name='p1', type=float )])
    assert e.return_type             is None
    assert len(e.typedParameters)    == 1
    assert e.typedParameters[0].name == 'p1'
    assert e.typedParameters[0].type == float

def test_2_Event_retunInt():
    e = CC_Event("an_event", return_type=int)
    assert e.return_type == int
