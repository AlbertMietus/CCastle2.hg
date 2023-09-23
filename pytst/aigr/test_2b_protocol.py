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
def simpleSieve():
    return EventProtocol("SimpleSieve", events=[Event("input", typedParameters=[TypedParameter(name='event', type=int)])])


def test_1_isEvent(emptyProtocol, simpleSieve):
    assert emptyProtocol.kind == ProtocolKind.Event
    assert simpleSieve.kind == ProtocolKind.Event

import castle.aigr.protocols
def test_2_based_onRoot(emptyProtocol):
    emptyProtocol.based_on is castle.aigr.protocols._RootProtocol

@pytest.mark.skip('To Do: read/mix/inherit protocols/events')
def test99_events_mix():
    a = EventProtocol("A", events=[Event("a1")])
    b = EventProtocol("B", events=[Event("b2"),Event("b3")], based_on=a)

    assert False, "Need to design reading & inheriting protocols and mixing events first"


