# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

from . import elemental, HW
from . import dummy

EH_NAME = mangle_event_handler(protocol='std', event='invoke', port='std')

def test_0():
    logger.info("Reading `Hello_World` is a test in itself")

def test_1_HW_in_file(elemental):
    comp = ScaffolderNameSpace(elemental).findNode('Elemental_HelloWorld')
    assert comp, f"`Elemental_HelloWorld` should be in file/SOURCE_NS, but isn't -- comp={comp}, elemental={elemental}"
    assert isinstance(comp, aigr.ComponentImplementation)

def test_2a_HW_has_1_callable(HW):
    for name in ('HelloWorld',):
        node = ScaffolderNameSpace(HW).findNode(name)
        assert node is not None,  f"Can't find '{name}' in <{HW.__class__.__name__}.{HW.name}> -- The only name are:{HW._ns.keys()}"
        assert name == node.name , f"Name {name} not in node"

@pytest.mark.skip("Can work; to search an EH ::use DispatchTable")
def test_2b_HW_has_1_eventHandler(HW):
    for name in (EH_NAME,):
        #node = HW.findNode(name)  #Search DispatchTable
        #assert node,  f"Can't find '{name}':{type(name)} in {type(HW)}: [[{', '.join('%s:%s' % (k, type(k)) for k in HW._ns.keys())}]]"
        #assert node.name == name, f"Name of {node} is not '{name}'"
        #assert isinstance(node, aigr.EventHandler)
        assert False, "Can't work"

def test_3a_HelloWorld_parms(HW):
    name = 'HelloWorld'
    method = ScaffolderNameSpace(HW).findNode(name)
    p = 'label'
    assert ScaffolderNameSpace(method).findNode(p), f"parm: {p} not found in {name} method"

@pytest.mark.skip("Can work; to search an EH ::use DispatchTable")
def test_3b__parms(HW):
    name = EH_NAME
    p = 'max'
    #eventhandler = HW.findNode(EH_NAME) #Search DispatchTable
    #assert eventhandler.findNode(p), f"parm: {p} not found in '{EH_NAME}'"
    #eventhandler = HW.findNode(name)
    #assert eventhandler.findNode(p), f"parm: {p} not found in '{name}'"
    assert False

def test_4a_HW_has_outer_ns(HW, elemental, dummy):
    "The HW ComponentImplementation, has an outer_ns: the file/SOURCE_NS: that is: elemental)"
    ScaffolderNameSpace(elemental).register(dummy)
    assert ScaffolderNameSpace(HW).findNode('dummy') is dummy, "This dummy node should be in the scope of HW"

def test_4b_HW_outer_nss(HW,  dummy):
    "The callables in HW have HW as outer_ns"
    ScaffolderNameSpace(HW).register(dummy)
    for name in ('HelloWorld',):
        callable=ScaffolderNameSpace(HW).findNode(name); assert callable
        assert ScaffolderNameSpace(callable).findNode('dummy') is dummy, f"This dummy node should be in the scope of {name}"

