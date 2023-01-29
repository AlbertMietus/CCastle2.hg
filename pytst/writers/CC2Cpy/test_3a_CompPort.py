# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
Test the supporting types (Enum, dataclasses ect) for  CC_B_ComponentInterface, and ...

The more relevant test of Protocol can be found in test_3b_* and test_3c_*"""

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import *
from castle.writers.CC2Cpy.Component import CC_PortDirection # Not public XXX

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
def test_1b_PortRender(): pass



@pytest.mark.skip(reason="More basic-testse are needed")
def test_more(): pass
