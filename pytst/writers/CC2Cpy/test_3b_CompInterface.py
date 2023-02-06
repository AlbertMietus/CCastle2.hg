# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

"""Only the  ComponentInterface (CC_B_ComponentInterface) is tested in the test-file.

The other parts of `castle.writers.CC2Cpy.Component` are tested elsewhere,
see: ./test_3*py
"""


import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentInterface

@pytest.fixture
def emptyComp():
    return CC_B_ComponentInterface('empty')

ref_emptyComp="""\
struct CC_B_ComponentInterface cc_CI_empty = {
 .name          = "empty",
 .inherit_from  = NULL,
 .length        = 0,
 .ports = {
 },
} ;
"""


from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol

@pytest.fixture
def demo2Comp():
    jap = CC_EventProtocol("JustAProtocol", events=[], based_on=None)
    return CC_B_ComponentInterface('demo2Comp', ports =[
        CC_Port(name='no_1', type=None, direction=CC_PortDirection.In),
        CC_Port(name='jap2', type=jap)])

ref_demo2Comp="""\
struct CC_B_ComponentInterface cc_CI_demo2Comp = {
 .name          = "demo2Comp",
 .inherit_from  = NULL,
 .length        = 2,
 .ports = {
  {
   .portNo    =  0,
   .protocol  =  NULL,
   .direction =  CC_B_PortDirectionIs_in,
   .name      = "no_1",
   .part_of   = &cc_CI_demo2Comp },
  {
   .portNo    =  1,
   .protocol  = &cc_P_JustAProtocol,
   .direction =  CC_B_PortDirectionIs_UNKNOWN,
   .name      = "jap2",
   .part_of   = &cc_CI_demo2Comp },
  },
} ;
"""



@pytest.fixture
def subComp(demo2Comp):
    return CC_B_ComponentInterface('sub', based_on=demo2Comp)

ref_subComp="""\
struct CC_B_ComponentInterface cc_CI_sub = {
 .name          = "sub",
 .inherit_from  = &cc_CI_demo2Comp,
 .length        = 0,
 .ports = {
 },
} ;
"""

def test_0a_name(emptyComp, demo2Comp):
    assert emptyComp.name == 'empty'
    assert demo2Comp.name == 'demo2Comp'

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


def test_2a_render_basic(emptyComp):
    assert CCompare(ref_emptyComp, emptyComp.render(), log_all=True)
    assert CCompare(ref_emptyComp, emptyComp.render_struct())

def test_2b_render_whitespace(emptyComp):
    # prepending a/o indenting with whitespace has no effect
    assert CCompare(ref_emptyComp, emptyComp.render(prepend="\t\t", indent=""))
    assert CCompare(ref_emptyComp, emptyComp.render_struct(prepend=" ", indent="\t\t\t"))

def test_2c_render_sub(subComp):
    assert CCompare(ref_subComp, subComp.render())

def test_2d_render_withPorts(demo2Comp):
    assert CCompare(ref_demo2Comp, demo2Comp.render())
