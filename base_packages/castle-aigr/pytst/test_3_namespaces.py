# (C) Albert Mietus, 2023-2025 Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from random import randint

from castle.aigr import NamedSpace, Source_NS, Scope
from castle.aigr import NamedNode
from castle.aigr import errors
from . import DummyNode, a_node

@pytest.fixture
def aNS(a_node):
    ns = NamedSpace("aNS")
    ns.register(a_node)
    return ns

@pytest.fixture
def top():
    top = NamedSpace('top')
    return top

@pytest.fixture
def sub(top):
    sub = NamedSpace('sub')
    top.register(sub)
    return sub

@pytest.fixture
def sourceNS(a_node):
    ns = Source_NS("sourceNS", source="dummy")
    ns.register(a_node)
    return ns

@pytest.fixture
def aScope(top, a_node):
    scope_ns = Scope(outer_ns=top)
    scope_ns.register(a_node)
    return scope_ns


def test_1_NS_stored(a_node, aNS):
    name = a_node.name
    assert aNS.getID(name) is a_node
    assert aNS.findNode(name) is a_node


def test_2_NS_find_vs_get_when_not_registered(aNS):
    assert aNS.findNode("Deze Bestaat Niet") is None
    try:
        aNS.getID("Deze Bestaat Niet")
        assert False, """`aNS.getID("Deze Bestaat Niet")` should raise an error"""
    except errors.NameError: pass


def test_3_sourceNS_combi(a_node, sourceNS):
    "The functionality as shown in _NS1 & _NS2 should also work with Source_NS"
    name = a_node.name
    assert sourceNS.getID(name) is a_node
    assert sourceNS.findNode(name) is a_node

    assert sourceNS.findNode("Deze Bestaat Niet") is None
    try:
        sourceNS.getID("Deze Bestaat Niet")
        assert False, """`sourceNS.getID("Deze Bestaat Niet")` should raise an error"""
    except errors.NameError: pass


def test_4_sameName_is_replaced(aNS):
    logger.warning("""NOTICE: This test will issue the warning 'astle.aigr.namespaces:namespaces.py:42' You should ignore it""")
    name='TriggerWarning'
    one = DummyNode(name, dummy='one')
    two = DummyNode(name, dummy='one')
    aNS.register(one);    assert aNS.getID(name) is one         #No test, just verify

    aNS.register(two)
    assert aNS.getID(name) is two         #The test


def test_5a_ns_in_ns():
    "when we import a NS, we get a NS in a NS ..."
    top = NamedSpace('top')
    sub = NamedSpace('sub')
    elm = DummyNode('elm', dummy="with.dotted.Name")
    top.register(sub)
    sub.register(elm)

    assert top.getID('sub') is sub
    assert sub.getID('elm') is elm
    assert top.search(dottedName="sub.elm") is elm


def test_5b_seach_1level(aNS,a_node):
    name = a_node.name
    assert (aNS.search(name) is a_node) and (aNS.getID(name) is a_node), "search should find that what getID returns"


def test_5c_seachNotFound_1(top):
    assert top.search("Deze bestaat niet") is None

def test_5d_seachNotFound_sub(top, sub):
    assert top.search("top.Deze.bestaat.niet") is None

#def test_6_registered_is_2ways(): Not usefull

def test_7_alias(aNS):
    node=DummyNode("aliased")
    alias="anOtherName"
    aNS.register(node, asName=alias)
    assert aNS.findNode(name=alias) is node,    f"it should be registered with the given alias: {alias}"
    assert aNS.findNode(name=node.name) is None, f"The realname should not be registered"


def test_byType_None(aNS):
    d = aNS.find_byType(type(None)) # There should be  None's in aNS
    assert isinstance(d, dict)
    assert len(d)==0

def test_byType_Dummy(aNS, a_node):
    d = aNS.find_byType(DummyNode)
    assert len(d)==1
    assert a_node.name in d
    assert d[a_node.name] is a_node # note: this assumed no aliasses are used ('asName')

def test_byType_NS(top, sub, sourceNS):
    top.register(sourceNS) # Note: sub is already 'in; top

    d = top.find_byType(NamedSpace)
    assert len(d) == 2 # sub, sourceNS
    assert d['sub'] is sub
    assert d['sourceNS'] is sourceNS

def test_find_in_outer_NS(aNS):
    a_node=aNS.findNode('a_node')
    localNS = NamedSpace('local', outer_ns=aNS)
    assert getattr(localNS._dict, 'a_node', 'NotLocal') == 'NotLocal', "a_node shouldn't be in localNS"
    assert localNS.findNode('a_node') is a_node


def test_Scope_is_a_NS(aScope, a_node):
    assert aScope.findNode('a_node') is a_node

def test_subScope_has_an_outerNS(aScope):
    assert aScope.outer_ns.name ==  'top'

def test_Subscope_find_inOuter(aScope, a_node):
    outer = aScope.outer_ns
    outer.register(a_node); assert outer.findNode('a_node') is a_node, "a_node is in the outer namespace"
    assert aScope.findNode('a_node') is a_node, "Nodes can be found in outer namespace too"


@pytest.mark.skip("Todo: Unite `.search()` and `.find()` [& `.getID()] -- see comment in `aigr/namespaces.py`")
def test_ToDo_Unite():
    assert False
