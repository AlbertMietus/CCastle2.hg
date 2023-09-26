# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Protocol, ProtocolKind
from castle.aigr import Event, EventProtocol
from castle.aigr.types import TypedParameter

@pytest.fixture
def emptyProtocol():
    return EventProtocol("EMPTY", events=[], based_on=None)

@pytest.fixture
def anEvent():
    return Event("input", typedParameters=[TypedParameter(name='event', type=int)])

@pytest.fixture
def simpleSieve(anEvent):
    return EventProtocol("SimpleSieve", events=[anEvent])

def test_1_isEvent(emptyProtocol, simpleSieve):
    assert emptyProtocol.kind == ProtocolKind.Event
    assert simpleSieve.kind == ProtocolKind.Event

import castle.aigr.protocols
def test_2_based_onRoot(emptyProtocol):
    emptyProtocol.based_on is castle.aigr.protocols._RootProtocol


def test_3a_eventIndex_empty(emptyProtocol, anEvent):
    assert emptyProtocol._noEvents() == 0
    try:
        emptyProtocol.eventIndex(anEvent)
        assert False, f"{anEvent} shouldn't be in the emptyProtocol"                    # pragma: no cover
    except ValueError: pass

def test_3b_eventIndex_simple(simpleSieve, anEvent):
    assert simpleSieve._noEvents() == 1
    assert simpleSieve.eventIndex(anEvent) == 0, f"`anEvent` should be eventIndex==0, but isn;t...T\n {anEvent}\n{simpleSieve.events}"

def test_3c_eventIndex_inherited():
    e0 = Event("E0")
    e1 = Event("E1")
    e2 = Event("E2")
    p0 = EventProtocol("P0", events=[e0])
    p1 = EventProtocol("P1", events=[e1,e2], based_on=p0)

    assert p1._noEvents() == 3
    assert p1.eventIndex(e2) == 2


