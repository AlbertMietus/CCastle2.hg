# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
Test the supporting types (Enum, dataclasses ect) for  CC_B_ComponentInterface, and ...

The more relevant test of Component(s) can be found in test_3b_* and test_3c_*"""

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import *


def test_1a_CC_PortDirection():
    # Test the (int) value -- needed for the generated C code
    assert CC_PortDirection.Unknown.value == 0
    assert CC_PortDirection.In.value      == 1
    assert CC_PortDirection.Out.value     == 2
    assert CC_PortDirection.BiDir.value   == 3
    assert CC_PortDirection.Master.value  == 4
    assert CC_PortDirection.Slave.value   == 5

    # Test the long-name & short-name are the same
    assert CC_PortDirection.Unknown == CC_PortDirection.CC_B_PortDirectionIs_UNKNOWN
    assert CC_PortDirection.In      == CC_PortDirection.CC_B_PortDirectionIs_in
    assert CC_PortDirection.Out     == CC_PortDirection.CC_B_PortDirectionIs_out
    assert CC_PortDirection.BiDir   == CC_PortDirection.CC_B_PortDirectionIs_bidirect
    assert CC_PortDirection.Master  == CC_PortDirection.CC_B_PortDirectionIs_master
    assert CC_PortDirection.Slave   == CC_PortDirection.CC_B_PortDirectionIs_slave

def test_1b_portray_PortDirection():
    assert CCompare('CC_B_PortDirectionIs_UNKNOWN',   CC_PortDirection.Unknown.portray_name())
    assert CCompare('CC_B_PortDirectionIs_in',        CC_PortDirection.In.portray_name())
    assert CCompare('CC_B_PortDirectionIs_out',       CC_PortDirection.Out.portray_name())
    assert CCompare('CC_B_PortDirectionIs_bidirect',  CC_PortDirection.BiDir.portray_name())
    assert CCompare('CC_B_PortDirectionIs_master',    CC_PortDirection.Master.portray_name())
    assert CCompare('CC_B_PortDirectionIs_slave',     CC_PortDirection.Slave.portray_name())


def test_2a1_Port_defaults():
    n, t = "defaults", int
    p1 = CC_Port(name=n, type=t) # Only direction is optional
    assert p1.name == n
    assert p1.type is t
    assert p1.direction == CC_PortDirection.Unknown

def test_2a1_Port_full():
    n, t = "full", float
    d=CC_PortDirection.In
    inp = CC_Port(name=n, type=t, direction=d)
    assert inp.name == n
    assert inp.type is t
    assert inp.direction == d


def test_2b1_portray_Port_name():
    port = CC_Port(name="aPort", type="no_relevant")
    assert CCompare('aPort', port.portray_name())

def test_2b2a_portray_Port_NoType():
    port = CC_Port(name="=NoName", type=None)
    assert CCompare('NULL', port.portray_typePtr())

def test_2b2b_portray_Port_strtype():
    port = CC_Port(name="=NoName", type="textType")
    assert CCompare('&cc_P_textType', port.portray_typePtr())

def test_2b2b_portray_Port_inttype():
    port = CC_Port(name="=NoName", type=int)
    assert CCompare('&cc_P_int', port.portray_typePtr())

def test_2b2d_portray_Port_floattype():
    port = CC_Port(name="=NoName", type=float)
    assert CCompare('&cc_P_float', port.portray_typePtr())

from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol

def test_2b2c_portray_Port_Protocol():
    proto = CC_EventProtocol("JustAProtocol", events=[], based_on=None)
    port  = CC_Port(name="=NoName", type=proto)
    # Note: When a Port's type is a Protocol, than the port's  portray_type is both
    ## the string 'cc_P_<xxxx>', and
    ## the portray_name of that protocol.
    ## We check both for now.
    assert CCompare('&cc_P_JustAProtocol',  port.portray_typePtr())
    assert CCompare('&'+proto.portray_name(),  port.portray_typePtr())


