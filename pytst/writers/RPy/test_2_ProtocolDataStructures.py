# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Event, EventProtocol
from castle.aigr.types import TypedParameter

from . import T_ProtocolDataStructures
from . import MockEvent
from . import T_Protocol
from . import assert_marker

@pytest.mark.skip("XXX ToDo:: The MockProtocol should go")
def test_ToDo(): pass


def test_0(T_ProtocolDataStructures):
    p1=EventProtocol(name="DEMO", events=(MockEvent(name="e1", indexNo=101), MockEvent(name="e2", indexNo=102)))
    logger.debug(p1)

    out = T_ProtocolDataStructures.render(protocols=[p1])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert False, out
