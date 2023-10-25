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
def top():
    top = NameSpace('top')
    return top

@pytest.fixture
def sub(top):
    sub = NameSpace('sub')
    top.register(sub)
    return sub

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


def test_5a_ns_in_ns():
    "when we import a NS, we get a NS in a NS ..."
    top = NameSpace('top')
    sub = NameSpace('sub')
    elm = DummyNode('elm', dummy="with.dotted.Name")
    top.register(sub)
    sub.register(elm)

    assert top.getID('sub') is sub
    assert sub.getID('elm') is elm
    assert top.search(dottedName="sub.elm") is elm


def test_5b_seach_1level(aNS,a_node):
    name = a_node.name
    assert (aNS.search(name) is a_node) and (aNS.getID(name) is a_node), "serach should find that what getID returns"


def test_5c_seachNotFound_1(top):
    assert top.search("Deze bestaat niet") is None

def test_5d_seachNotFound_sub(top, sub):
    assert top.search("top.Deze.bestaat.niet") is None

def test_6a_registered_is_2ways(aNS, a_node):
    """When a NamedNode is registered in a NameSpace, it should a backlink (`ns property) to the NS again"""
    assert a_node.ns is aNS

def test_6b_registered_is_2ways_once(aNS, a_node):
    """Currently, a NamedNode can be registered in multiple namespaces, but the backlink is always the last
       XXX ToDo: is that the intent? For now test as is"""
    name = a_node.name
    other = NameSpace('other')
    other.register(a_node)

    assert (aNS.getID(name) is a_node) and (other.getID(name) is a_node),  "A NamedNode can be registered in two NS'ses ..."
    assert a_node.ns is other, " ...but Only the last NS is remembered"

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

    d = top.find_byType(NameSpace)
    assert len(d) == 2 # sub, sourceNS
    assert d['sub'] is sub
    assert d['sourceNS'] is sourceNS



@pytest.mark.skip("Todo: Unite `.search()` and `.find()` [& `.getID()] -- see comment in `aigr/namespaces.py`")
def test_ToDo_Unite():
    assert False
