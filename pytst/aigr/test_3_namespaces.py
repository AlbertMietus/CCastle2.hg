# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from random import randint

from castle.aigr import NameSpace, Source_NS

from castle.aigr.namespaces import NamedNode ## May be moved ip
from castle.aigr.namespaces import NameError

@dataclass
class DummyNode(NamedNode):
    name       :str
    _: KW_ONLY
    dummy      :PTH.Any=None

@pytest.fixture
def a_node():
    return DummyNode("a_node", dummy=randint(42,2023))

@pytest.fixture
def aNS(a_node):
    ns = NameSpace("aNS")
    ns.register(a_node)
    return ns

@pytest.fixture
def sourceNS(a_node):
    ns = Source_NS("sourceNS", source="dummy")
    ns.register(a_node)
    return ns


def test_1_NS_stored(a_node, aNS):
    name = a_node.name
    assert aNS.getID(name) is a_node
    assert aNS.findNode(name) is a_node


def test_2_NS_find_vs_get_when_not_registered(aNS):
    assert aNS.findNode("Deze Bestaat Niet") is None
    try:
        aNS.getID("Deze Bestaat Niet")
        assert False, """`aNS.getID("Deze Bestaat Niet")` should raise an error"""
    except NameError: pass

def test_3_sourceNS_combi(a_node, sourceNS):
    "The functionality as shown in _NS1 & _NS2 should also work with Source_NS"
    name = a_node.name
    assert sourceNS.getID(name) is a_node
    assert sourceNS.findNode(name) is a_node

    assert sourceNS.findNode("Deze Bestaat Niet") is None
    try:
        sourceNS.getID("Deze Bestaat Niet")
        assert False, """`sourceNS.getID("Deze Bestaat Niet")` should raise an error"""
    except NameError: pass

def test_4_sameName_is_replaced(aNS):
    logger.warning("""NOTICE: This test will issue the warning 'astle.aigr.namespaces:namespaces.py:42' You should ignore it""")
    name='TriggerWarning'
    one = DummyNode(name, dummy='one')
    two = DummyNode(name, dummy='one')
    aNS.register(one);    assert aNS.getID(name) is one         #No test, just verify

    aNS.register(two)
    assert aNS.getID(name) is two         #The test

def NSsearch(ns, dottedName):
    "This functionality should be moved to namespace"

    parts = dottedName.split('.')
    travarse, elm = parts[:-1], parts[-1]

    for name in travarse:
        next_ns = ns.findNode(name)
        if isinstance(next_ns, NameSpace):
            ns = next_ns
        else:
            return None # no found or no namespace
    return ns.findNode(elm)

 
def test_5a_ns_in_ns_with_NSsearch():
    "when we import a NS, we get a NS in a NS ..."
    top = NameSpace('top')
    sub = NameSpace('sub')
    elm = DummyNode('elm', dummy="with.dotted.Name")
    top.register(sub)
    sub.register(elm)

    assert top.getID('sub') is sub
    assert sub.getID('elm') is elm
    assert NSsearch(top, dottedName="sub.elm") is elm

def test_5b_ns_in_ns():
    "when we import a NS, we get a NS in a NS ..."
    top = NameSpace('top')
    sub = NameSpace('sub')
    elm = DummyNode('elm', dummy="with.dotted.Name")
    top.register(sub)
    sub.register(elm)

    assert top.getID('sub') is sub
    assert sub.getID('elm') is elm
    assert top.search(dottedName="sub.elm") is elm

   
