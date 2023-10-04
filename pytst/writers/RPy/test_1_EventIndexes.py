# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr.aid import TypedParameter

from castle.aigr import EventProtocol, Event
from . import T_EventIndexes
from . import T_Protocol
from . import assert_marker


EventIndex_PreFix = "CC_P_"               #Keep in sync with implementation


def test_template_0_NoEvent(T_EventIndexes):
    p = EventProtocol("NoEventsMOCK", events=[])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 0)
    assert_marker('=', out, 0)


def test_template_1_event(T_EventIndexes):
    p = EventProtocol("MOCK", events=[Event("input", typedParameters=[TypedParameter(name='event', type=int)])])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 1)
    assert_marker('= 0', out)


def test_template_2_SomeEvent(T_EventIndexes):
    p = EventProtocol("MOCK", events= [Event("one"), Event("two"), Event("three"), Event("four")])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 4)
    assert_marker('= 0', out)
    assert_marker('= 1', out)
    assert_marker('= 2', out)
    assert_marker('= 3', out)



def test_EventIndexes_In_protocol(T_Protocol):
    out=T_Protocol.render(protocols=[EventProtocol(name="MOCK", events=[Event("input")])])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert True, "No assert (not maintainable) only check it runs"

