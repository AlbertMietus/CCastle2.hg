# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
Test the supporting types (Enum, dataclasses ect) for  CC_B_ComponentInterface, and ...

The more relevant test of Protocol can be found in test_3b_* and test_3c_*"""

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

@pytest.mark.skip(reason="Is rendering needed?")
def test_1b_render_PortDirection(): pass

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


@pytest.mark.skip(reason="Is rendering needed?")
def test_2z_render_Port(): pass
    



@pytest.mark.skip(reason="More basic-testse are needed")
def test_more(): pass
