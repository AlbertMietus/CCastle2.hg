# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from dataclasses import dataclass

from castle.writers import RPy
from castle.aigr import Event, Protocol
from castle.aigr.types import TypedParameter

EventIndex_PreFix = "CC_P_"               #Keep in sync with implementation
#from . import *

@dataclass
class MockEvent(Event):
    indexNo: int

@dataclass
class MockProtocol():
    name: str

@pytest.fixture
def EventIndexes():
    return RPy.Template("EventIndexes.jinja2")

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


#def test_template_2_SomeEvent(EventIndexes):


@pytest.mark.skip("more tests are needed")
def test_99():
    pass
