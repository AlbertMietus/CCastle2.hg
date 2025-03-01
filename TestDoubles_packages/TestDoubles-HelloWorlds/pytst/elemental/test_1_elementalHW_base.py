# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler

from . import elemental, HW
from . import dummy

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

def test_4a_HW_has_outer_ns(HW, elemental, dummy):
    "The HW ComponentImplementation, has an outer_ns: the file/SOURCE_NS: that is: elemental)"
    elemental.register(dummy)
    assert HW.findNode('dummy') is dummy, "This dummy node should be in the scope of HW"

def test_4b_HW_outer_nss(HW,  dummy):
    "The callables in HW have HW as outer_ns"
    HW.register(dummy)
    for name in ('HelloWorld', mangle_event_handler(protocol='Power', event='powerOn', port='power')):
        callable=HW.findNode(name); assert callable
        assert callable.findNode('dummy') is dummy, f"This dummy node should be in the scope of {name}"

