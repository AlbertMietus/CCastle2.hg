# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

"""Only the  ComponentInterface (CC_B_ComponentInterface) is tested in the test-file.

The other parts of `castle.writers.CC2Cpy.Component` are tested elsewhere,
see: ./test_3*py
"""


import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from . import common
from castle.writers.CC2Cpy.CC_B_ComponentInterface import CC_B_ComponentInterface
from castle.writers.CC2Cpy.CCbase import *

@pytest.fixture
def emptyComp():
    return common.emptyComp()

@pytest.fixture
def demo2Comp():
    return common.demo2Comp()

@pytest.fixture
def subComp(demo2Comp):
    return common.subComp(demo2Comp)


def test_0a_name(emptyComp, demo2Comp):
    assert emptyComp.name == 'empty'
    assert demo2Comp.name == 'demo2Comp'

def test_0b_based_on(subComp, demo2Comp):
    logging.debug(subComp)
    logging.debug(demo2Comp)
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
    assert CCompare(common.ref_emptyComp, emptyComp.render(), log_all=True)
    assert CCompare(common.ref_emptyComp, emptyComp.render_Fill_Interface())

def test_2b_render_whitespace(emptyComp):
    # prepending a/o indenting with whitespace has no effect
    assert CCompare(common.ref_emptyComp, emptyComp.render(prepend="\t\t", indent=""))
    assert CCompare(common.ref_emptyComp, emptyComp.render_Fill_Interface(prepend=" ", indent="\t\t\t"))

def test_2c_render_sub(subComp):
    assert CCompare(common.ref_subComp, subComp.render())

def test_2d_render_withPorts(demo2Comp):
    assert CCompare(common.ref_demo2Comp, demo2Comp.render())


def test_3a_indent_empty(emptyComp):
    verify_indents(common.ref_emptyComp, emptyComp.render)

def test_3b_indent_demo(demo2Comp):
    verify_indents(common.ref_demo2Comp, demo2Comp.render)

def test_3c_indent_sub(subComp):
    verify_indents(common.ref_subComp, subComp.render)
