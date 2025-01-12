# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World


@pytest.fixture
def elemental():
    return Hello_World

@pytest.fixture
def HW(elemental):
    comp = elemental.findNode('Elemental_HelloWorld')
    assert isinstance(comp, aigr.ComponentImplementation)
    return  comp


def test_0():
    logger.info("Reading `Hello_World` is a test in itself")

def test_1_HW_in_file(elemental):
    comp = elemental.findNode('Elemental_HelloWorld')
    assert comp, f"`Elemental_HelloWorld` should be in file/SOURCE_NS, but isn't -- comp={comp}, elemental={elemental}"
    assert isinstance(comp, aigr.ComponentImplementation)

def test_2_HW_has_2_callables(HW):
    for name in ('HelloWorld', mangle_event_handler(protocol='Power', event='powerOn', port='power')):
        node = HW.findNode(name)
        assert node,  f"Can't find '{name}' in {HW}"
        assert node.name == name, f"Name of f is not '{name}'"

def test_3a_HelloWorld_parms(HW):
    name = 'HelloWorld'
    method = HW.findNode(name)
    p = 'label'
    assert method.findNode(p), f"parm: {p} not found in {name} method"

def test_3b__parms(HW):
    name = mangle_event_handler(protocol='Power', event='powerOn', port='power')
    p = 'max'
    eventhandler = HW.findNode(name)
    assert eventhandler.findNode(p), f"parm: {p} not found in '{name}'"

