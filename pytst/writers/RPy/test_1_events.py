# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from castle.aigr.types import TypedParameter
from . import T_EventIndexes as EventIndexes
from . import MockEvent, MockProtocol

EventIndex_PreFix = "CC_P_"               #Keep in sync with implementation


def assert_markers(marker, txt, need):
    lines = txt.splitlines()
    c = sum(1 if (marker in line) else 0 for line in lines)
    assert c == need, f"Needed {need} lines with '{marker}'-markers, found {c} -- in {len(lines)} lines"



def test_template_0_NoEvent(EventIndexes):
    out=EventIndexes.render(protocol=MockProtocol("NoEventsMOCK"), events=[])
    logger.debug("out::\n%s", out)

    assert_markers(EventIndex_PreFix, out, 0)
    assert_markers('=', out, 0)


def test_template_1_event(EventIndexes):
    out=EventIndexes.render(protocol=MockProtocol("MOCK"),
                            events=[MockEvent("input", indexNo=-7, typedParameters=[TypedParameter(name='event', type=int)])])
    logger.debug("out::\n%s", out)

    assert_markers(EventIndex_PreFix, out, 1)
    assert_markers('=', out, 1)


def test_template_2_SomeEvent(EventIndexes):
    out=EventIndexes.render(protocol=MockProtocol("MOCK"),
                            events=[
                                MockEvent("one",  indexNo=1),
                                MockEvent("two",  indexNo=2),
                                MockEvent("three",indexNo=3),
                                MockEvent("four", indexNo=4)])
    logger.debug("out::\n%s", out)

    assert_markers(EventIndex_PreFix, out, 4)
    assert_markers('=', out, 4)

#def test_IndexInProtocol():
    
@pytest.mark.skip("more tests are needed")
def test_99():
    pass
