# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from dataclasses import dataclass

from castle.writers import RPy
from castle.aigr import Event, Protocol
from castle.aigr.types import TypedParameter

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


def test_template_0_NoEvent(EventIndexes):
    out=EventIndexes.render(protocol=MockProtocol("NoEventsMOCK"), events=[])
    logger.info("NoEvent\n%s", out)
    assert not 'CC_P' in out

def test_template_1_event(EventIndexes):
    out=EventIndexes.render(protocol=MockProtocol("MOCK"),
            events=[MockEvent("input", indexNo=-7, typedParameters=[TypedParameter(name='event', type=int)])])
    logger.info(out)


#def test_template_2_SomeEvent(EventIndexes):


@pytest.mark.skip("more tests are needed")
def test_99():
    pass
