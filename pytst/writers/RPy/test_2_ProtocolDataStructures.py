# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import EventProtocol, Event
from castle.aigr.types import TypedParameter

from . import T_ProtocolDataStructures
from . import T_Protocol
from . import assert_marker

protoData_PreFix = "cc_P_"               #Keep in sync with implementation


@pytest.fixture
def p_1e():
    "Protocol with 1 event"
    p = EventProtocol(name="P1", events=(Event(name="e1"),))
    logger.debug("%s", p)
    return p

@pytest.fixture
def p_2e_1i(p_1e):
    "Protocol with 2 events, and 1 inherited; so 3 in total"
    p = EventProtocol(name="P2", events=(Event(name="e2"), Event(name="e3")), based_on=p_1e)
    logger.debug("%s", p)
    return p

##
## assert_marker(.. `need`) CALCULATION
##	1*p  (protocol dataclasses assignment
##  2*e  (each event: 1 [ <P-name>...append ] + 1 part_of=<P-name>
##  The  inherited events dont' count

def test_simpleProto_rendering(T_ProtocolDataStructures, p_1e):
    "a simple protocol: no inheritance, 1 event"
    out = T_ProtocolDataStructures.render(protocols=[p_1e])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)

    assert_marker(protoData_PreFix + 'P1', out, 1+2*1)



def test_subProcotol_rendering(T_ProtocolDataStructures, p_1e, p_2e_1i):
    """This protocol inherits the above one, and add two events. So it should have 2 events (not 3!!)
       Only this second protocol in rendered"""
    out = T_ProtocolDataStructures.render(protocols=[p_2e_1i])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)

    assert_marker(protoData_PreFix + 'P2', out, 1+2*2)
    assert_marker(protoData_PreFix + 'P1', out, 1, "Need one ref to inherited protocol") #



def test_2Procotol_rendering(T_ProtocolDataStructures, p_1e, p_2e_1i):
    "Same as above, but now render both protocols"
    out = T_ProtocolDataStructures.render(protocols=[p_1e, p_2e_1i])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)

    assert_marker(protoData_PreFix + 'P2', out, 1+2*2)


def test_protocol_with_NoParms_a(T_ProtocolDataStructures):
    "An (event) protocol without parameters does not render the parameter line"
    out = T_ProtocolDataStructures.render(protocols=[EventProtocol(name="NoParms_", events=[])])
    assert 'parameters' not in out

def test_protocol_with_NoParms_b(T_ProtocolDataStructures):
    out = T_ProtocolDataStructures.render(protocols=[EventProtocol(name="NoParms",
                                                                   events=[],
                                                                   typedParameters=[])])
    assert 'parameters' not in out

def test_protocol_with_1parm(T_ProtocolDataStructures):
    out = T_ProtocolDataStructures.render(protocols=[EventProtocol(name="With_1_Parm",
                                                                       events=[],
                                                                       typedParameters=[TypedParameter(name='a_parm', type="A_Type")])])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert 'parameters=' in out
    assert False, "check rendering"

def test_protocol_with_parms(T_ProtocolDataStructures):
    out = T_ProtocolDataStructures.render(protocols=[EventProtocol(name="WithParms",
                                                                       events=[],
                                                                       typedParameters=[
                                                                           TypedParameter(name='a_parm', type="A_Type"),
                                                                           TypedParameter(name='b_parm', type=int),
                                                                           TypedParameter(name='c_parm', type=float),
                                                                           TypedParameter(name='1', type=int)
                                                                           ])])
    logger.debug("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert 'parameters=' in out
    assert False, "check rendering"



def test_ProtocolDataStructures_in_protocol(T_Protocol, p_1e, p_2e_1i):
    out = T_Protocol.render(protocols=[p_1e, p_2e_1i])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert True, "No assert (not maintainable) only check it runs"
