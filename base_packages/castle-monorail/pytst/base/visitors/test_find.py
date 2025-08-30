# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Test finding the methods -- prefix and default"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.monorail.base.dispatch import MRO_Dispatch_Mixin


class FakeNode(): pass

class MockVisitor(MRO_Dispatch_Mixin):
    _prefixes = ('just_a_prefix', "another_prefix",)
    def just_a_prefix_FakeNode(self, node):
        logger.info("MockVisitor.just_a_prefix_FakeNode is called for %s", node)
        return "just_a_prefix_FakeNode"
    def another_prefix_FakeNode(self, node):
        logger.info("MockVisitor.another_prefix_FakeNode is called for %s", node)
        return "another_prefix_FakeNode"

class Sub_Mock(MockVisitor):
    def just_a_prefix_FakeNode(self, node):
        logger.info("Sub_Mock.just_a_prefix_FakeNode is called for %s", node)
        return "Sub_Mock.just_a_prefix_FakeNode"

@pytest.fixture
def visitor():
    return MockVisitor()

@pytest.fixture
def sub_visitor():
    return Sub_Mock()

@pytest.fixture
def dummy():
    return FakeNode()

def test_1_known_prefix(visitor):
    assert visitor.dispatch_check_prefix('just_a_prefix'), "Can't find known prefix"
    assert visitor.dispatch_check_prefix('another_prefix'), "Can't find the other prefix"

def test_2_find_method(visitor, dummy):
    method = visitor.dispatch_find_method_by_mro(dummy, 'just_a_prefix')
    assert method is not None
    assert method(dummy) == "just_a_prefix_FakeNode"

def test_2_findright_method(sub_visitor, dummy):
    method = sub_visitor.dispatch_find_method_by_mro(dummy, 'just_a_prefix')
    assert method is not None
    assert method(dummy) == "Sub_Mock.just_a_prefix_FakeNode", "Should find the method in the subclass"
    assert sub_visitor.dispatch_find_method_by_mro(dummy, 'another_prefix')(dummy) == "another_prefix_FakeNode", "Should find the method in the superclass"
