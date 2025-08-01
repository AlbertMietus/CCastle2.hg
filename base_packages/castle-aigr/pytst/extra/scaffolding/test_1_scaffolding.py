# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from castle.aigr_extra.scaffolding.scaffolder import _Scaffolder
from castle.aigr_extra.scaffolding import ScaffolderNode

class Dummy(aigr.AIGR):    pass
class FakeNode(aigr.AIGRNode):
    def return_42(self):
        return 42 # Just a marker

@pytest.fixture
def fake():
    return FakeNode()

@pytest.fixture
def wrapped_fake(fake):
    return ScaffolderNode(FakeNode())


def test_0a__nodeCls():
    """These setting are also functionally testen below"""
    assert _Scaffolder._nodeCls == aigr.AIGR
    assert ScaffolderNode._nodeCls == aigr.AIGRNode

def test_0b__repr(wrapped_fake):
    assert "<Scaffolder" in repr(wrapped_fake)
    assert 'FakeNode' in repr(wrapped_fake)

def test_1a_CantMake_scaffolder():
    d = Dummy()
    try:
        _Scaffolder(d)
        assert False, "shouldn't be here"                    # pragma: no cover
    except TypeError: pass

def test_1b_Cant_Scaffold_nonNode():
    d = Dummy()
    try:
        ScaffolderNode(d)
        assert False, "shouldn't be here"                   # pragma: no cover
    except TypeError: pass


def test_2a_Scaffold_Node(fake, wrapped_fake):
    assert wrapped_fake.node == fake, "A ScaffolderNode holds the node"

def test_2b_Scaffold_WrapsNode_delegate(wrapped_fake):
    assert wrapped_fake.return_42() == 42

def test_3a_SetParent_withNode_isA_Node(wrapped_fake):
    top_node = FakeNode()
    wrapped_fake.set_parent(top_node)
    assert wrapped_fake.parent == top_node
    assert wrapped_fake.node.parent == top_node

def test_3b_SetParent_withScaffolder_isA_Node(wrapped_fake):
    top_node = FakeNode()
    top_wrap = ScaffolderNode(top_node)
    wrapped_fake.set_parent(top_wrap)
    assert wrapped_fake.parent == top_node
    assert wrapped_fake.node.parent == top_node

