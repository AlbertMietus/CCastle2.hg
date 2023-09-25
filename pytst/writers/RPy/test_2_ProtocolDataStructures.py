# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Event, EventProtocol
from castle.aigr.types import TypedParameter

from . import T_ProtocolDataStructures
from . import MockEvent
from . import T_Protocol
from . import assert_marker

protoData_PreFix = "cc_P_"               #Keep in sync with implementation

@pytest.mark.skip("XXX ToDo:: The MockProtocol should go")
def test_ToDo(): pass

@pytest.fixture
def p_1e():
    "Protocol with 1 event"
    p = EventProtocol(name="P1", events=(MockEvent(name="e1", indexNo=101),))
    logger.debug("%s", p)
    return p

@pytest.fixture
def p_2e_1i(p_1e):
    "Protocol with 2 events, and 1 inherited; so 3 in total"
    p = EventProtocol(name="P2", events=(MockEvent(name="e2", indexNo=102), MockEvent(name="e3", indexNo=103)), based_on=p_1e)
    logger.debug("%s", p)
    return p

##
## assert_marker(.. `need`) CALCULATION
##	1*p  (protocol dataclasses assignment
##  2*e  (each event: 1 [ <P-name>...append ] + 1 part_of=<P-name>
##  The  inherited events dont' count

def test_0(T_ProtocolDataStructures, p_1e):
    out = T_ProtocolDataStructures.render(protocols=[p_1e])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)

    assert_marker(protoData_PreFix + 'P1', out, 1+2*1)


def test_0n(T_ProtocolDataStructures, p_1e, p_2e_1i):
    out = T_ProtocolDataStructures.render(protocols=[p_1e, p_2e_1i])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)

    assert_marker(protoData_PreFix + 'P2', out, 1+2*2)
    
