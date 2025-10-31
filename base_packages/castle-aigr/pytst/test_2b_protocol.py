# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Protocol, ProtocolKind
from castle.aigr import Event, EventProtocol
from castle.aigr import TypedParameter
from castle.aigr import types
from castle.aigr import types

from castle.aigr_extra.scaffolding import ScaffolderEventProtocol

@pytest.fixture
def emptyProtocol():
    return EventProtocol("EMPTY", events=[], based_on=None)

@pytest.fixture
def emptyProtocol_baseNotSet():
    return Protocol("VeryEmpty", kind=ProtocolKind.Unknown)

@pytest.fixture
def anEvent():
    return Event("input", typedParameters=[TypedParameter(name='event', type=types.int)])

@pytest.fixture
def simpleSieve(anEvent):
    return EventProtocol("SimpleSieve", events=[anEvent])



def test_1_isEvent(emptyProtocol, simpleSieve):
    assert emptyProtocol.kind == ProtocolKind.Event
    assert simpleSieve.kind == ProtocolKind.Event

#base/rootProtocol is gone -- protocol.based_on is a ID/RefID now
#def test_2a_based_onRoot(emptyProtocol):
#    from castle.aigr.protocols import _RootProtocol # Only available when imported
#    emptyProtocol.based_on is _RootProtocol
#def test_2b_based_onRoot_notSet(emptyProtocol_baseNotSet):
#    from castle.aigr.protocols import _RootProtocol # Only available when imported
#    emptyProtocol_baseNotSet.based_on is _RootProtocol

def test_2c_NoBase_isNone(emptyProtocol, emptyProtocol_baseNotSet):
    assert emptyProtocol.based_on is None
    assert emptyProtocol_baseNotSet.based_on is None


def test_3a_eventIndex_empty(emptyProtocol, anEvent):
    emptyProtocol = ScaffolderEventProtocol(emptyProtocol)
    assert emptyProtocol._noEvents() == 0, "check, not a test"
    try:
        emptyProtocol.eventIndex(anEvent)
        assert False, f"{anEvent} shouldn't be in the emptyProtocol"                    # pragma: no cover
    except ValueError: pass


def test_3b_eventIndex_simple(simpleSieve, anEvent):
    simpleSieve = ScaffolderEventProtocol(simpleSieve)
    assert simpleSieve._noEvents() == 1
    assert simpleSieve.eventIndex(anEvent) == 0, f"`anEvent` should be eventIndex==0, but isn;t...T\n {anEvent}\n{simpleSieve.events}"


def test_3c_eventIndex_inherited():
    e0 = Event("E0")
    e1 = Event("E1")
    e2 = Event("E2")
    p0 = EventProtocol("P0", events=[e0])
    p1 = EventProtocol("P1", events=[e1,e2], based_on=p0)

    p0 = ScaffolderEventProtocol(p0)
    p1 = ScaffolderEventProtocol(p1)

    assert p1._noEvents() == 3
    assert p1.eventIndex(e2) == 2


def test_protocol_with_Noparms(emptyProtocol):
    assert emptyProtocol.typedParameters == ()


def test_protocol_with_aParm():
    e = EventProtocol("With_a_parm", events=[], based_on=None,
                          typedParameters=[TypedParameter(name='p', type=types.float)])
    assert len(e.typedParameters) ==1
    assert e.typedParameters[0].name == 'p'
    assert e.typedParameters[0].type == types.float


def test_protocol_with_4Parms():
    e = EventProtocol("With_4_Parms", events=[], based_on=None,
                          typedParameters=(
                              TypedParameter(name='p0', type=types.float ),
                              TypedParameter(name='p1', type=types.int ),
                              TypedParameter(name='p2', type=types.string ),
                              TypedParameter(name='p3', type=None ),
                              ))
    assert len(e.typedParameters) == 4
    assert (e.typedParameters[0].name, e.typedParameters[0].type) == ('p0', types.float)
    assert (e.typedParameters[1].name, e.typedParameters[1].type) == ('p1', types.int)
    assert (e.typedParameters[2].name, e.typedParameters[2].type) == ('p2', types.string)
    assert (e.typedParameters[3].name, e.typedParameters[3].type) == ('p3', None)


#Note: for more complicated cases, see :file:`test_2c_WrappedProtocols.py`

