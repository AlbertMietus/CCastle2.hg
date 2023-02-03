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

def test_0a_name(emptyComp, demo2Comp):
    assert emptyComp.name == 'empty'
    assert demo2Comp.name == 'demo2'

def test_0b_based_on(subComp, demo2Comp):
    assert demo2Comp.based_on == ()
    assert subComp.based_on[0] is demo2Comp

def test_1a_NoOfPorts(emptyComp, demo2Comp):
    assert emptyComp.no_of_ports() == 0
    assert demo2Comp.no_of_ports() == 2

def test_1b_NoOfPorts_variants(subComp):
    assert subComp.no_of_ports() == 0                              # inherited=False, mine=True
    assert subComp.no_of_ports(inherited=False, mine=False) == 0
    assert subComp.no_of_ports(inherited=False, mine=True)  == 0
    assert subComp.no_of_ports(inherited=True,  mine=False) == 2
    assert subComp.no_of_ports(inherited=True,  mine=True)  == 2

def test_1c_MorePorts():
    p1 = CC_B_ComponentInterface('p1', ports =  CC_Port(name='no_1', type=None))
    p2 = CC_B_ComponentInterface('p2', ports = [CC_Port(name='no_2', type=None), CC_Port(name='no_3', type=None)])
    pa = CC_B_ComponentInterface('pa', ports =  CC_Port(name='no_4', type=None))
    pb = CC_B_ComponentInterface('pb', based_on = pa)
    p  = CC_B_ComponentInterface('p',  based_on = (p1,p2,pb))

    assert p.no_of_ports(inherited=True, mine=True) == 4


ref_emptyComp="""\
struct CC_B_ComponentInterface cc_CI_Empty = {
 .name          = "empty",
 .inherit_from  = &cc_CI_Component,
 .length        = 0,
 .ports = {
 }
} ;
"""

ref_subComp="""\
struct CC_B_ComponentInterface cc_CI_sub = {
 .name          = "sub",
 .inherit_from  = &cc_CI_demo2,
 .length        = 0,
 .ports = {
 }
} ;
"""

def test_render(emptyComp):
    CCompare(ref_emptyComp, emptyComp.render())
    CCompare(ref_emptyComp, emptyComp.render_struct())

def test_render_whitespace(emptyComp):
    # prepending a/o indenting with whitespace has no effect
    CCompare(ref_emptyComp, emptyComp.render(prepend="\t\t", indent=""))
    CCompare(ref_emptyComp, emptyComp.render_struct(prepend=" ", indent="\t\t\t"))


def test_render_sub(subComp):
    CCompare(ref_subComp, subComp.render())

@pytest.mark.skip(reason="More CompInterface-tests are needed")
def test_more(): pass

    
