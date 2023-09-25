# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr.types import TypedParameter

from castle.aigr import EventProtocol
from . import T_EventIndexes
from . import MockEvent
from . import T_Protocol
from . import assert_marker


EventIndex_PreFix = "CC_P_"               #Keep in sync with implementation


@pytest.mark.skip("XXX ToDo:: The MockEvent should go")
def test_ToDo(): pass


def test_template_0_NoEvent(T_EventIndexes):
    p = EventProtocol("NoEventsMOCK", events=[])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 0)
    assert_marker('=', out, 0)


def test_template_1_event(T_EventIndexes):
    p = EventProtocol("MOCK", events=[MockEvent("input", indexNo=-7, typedParameters=[TypedParameter(name='event', type=int)])])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 1)
    assert_marker('=', out, 1)


def test_template_2_SomeEvent(T_EventIndexes):
    p = EventProtocol("MOCK", events=\
                          [ MockEvent("one",  indexNo=1),
                            MockEvent("two",  indexNo=2),
                            MockEvent("three",indexNo=3),
                            MockEvent("four", indexNo=4)])
    out=T_EventIndexes.render(protocol=p, events=p.events)
    logger.debug("out::\n%s", out)

    assert_marker(EventIndex_PreFix, out, 4)
    assert_marker('=', out, 4)


def test_EventIndexes_In_protocol(T_Protocol):
    out=T_Protocol.render(protocols=[EventProtocol(name="MOCK", events=[MockEvent("input", indexNo=-7)])])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert True, "No assert (not maintainable) only check it runs"

