# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentInterface


@pytest.fixture
def emptyComp():
    return CC_B_ComponentInterface('empty')

@pytest.fixture
def demo2Comp():
    return CC_B_ComponentInterface('demo2', ports =[
        CC_Port(name='no_1', type=None),
        CC_Port(name='no_2', type=None)])

@pytest.fixture
def subComp(demo2Comp):
    return CC_B_ComponentInterface('sub', based_on=demo2Comp)

def test_0_name(emptyComp, demo2Comp):
    assert emptyComp.name == 'empty'
    assert demo2Comp.name == 'demo2'

def test_0_based_on(subComp, demo2Comp):
    assert demo2Comp.based_on == ()
    assert subComp.based_on[0] is demo2Comp

def test_1_NoOfPorts(emptyComp, demo2Comp):
    assert emptyComp.no_of_ports() == 0
    assert demo2Comp.no_of_ports() == 2

def test_1_NoOfPorts_variants(subComp):
    assert subComp.no_of_ports() == 0                              # inherited=False, mine=True

    assert subComp.no_of_ports(inherited=False, mine=False) == 0
    assert subComp.no_of_ports(inherited=False, mine=True)  == 0
    assert subComp.no_of_ports(inherited=True,  mine=False) == 2
    assert subComp.no_of_ports(inherited=True,  mine=True)  == 2

@pytest.mark.skip(reason="More CompInterface-tests are needed")
def test_more(): pass

    
