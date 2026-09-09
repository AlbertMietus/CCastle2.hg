# (C) Albert Mietus, 2026. Part of Castle/CCastle project

"""Test finding the methods -- prefix and default"""

import logging; logger = logging.getLogger(__name__)
import pytest
import inspect

from castle.monorail.base.dispatch import MRO_Dispatch_Mixin


class OuterNode():
    """Nested (node) classes are strange and rare, but monorail visitors should work"""
    class InnerNode():
        pass

class OtherOuterNode():
    class InnerNode():
        "This InnerNode  should have another visitor the the InnerNode above!!"

class NestedVisitorSpy(MRO_Dispatch_Mixin):
    _prefixes =('foo',)
    @staticmethod
    def _sharedSpy(node):
        """ All visitor in this class call this code, returning the qualname of the node and the name of the visitor"""
        method_name = inspect.currentframe().f_back.f_code.co_name
        qualname = type(node).__qualname__
        logger.info("Visitor: %s is called for %s -- returning %s", method_name, node, qualname)
        return qualname, method_name

    def foo_OuterNode(self, node):
        return self._sharedSpy(node)
    def foo_InnerNode(self, node):
        return self._sharedSpy(node)
    def foo_OuterNode_InnerNode(self,node):
        return self._sharedSpy(node)
    def foo_OtherOuterNode_InnerNode(self,node):
        return self._sharedSpy(node)


@pytest.fixture
def visitor():
    return NestedVisitorSpy()


def test_NestedNode_Outer(visitor):
    node = OuterNode()
    method = visitor.dispatch_find_method_by_mro(node, 'foo')
    nodeName, visitorsName = method(node)
    assert  nodeName == "OuterNode"
    assert  visitorsName == "foo_OuterNode"

def test_NestedNode_Inner(visitor):
    node = OuterNode.InnerNode()
    method  = visitor.dispatch_find_method_by_mro(node, 'foo')
    nodeName, visitorsName = method(node)
    assert  nodeName == "OuterNode.InnerNode"
    assert  visitorsName == "foo_OuterNode_InnerNode"

def test_OtherOuterNode_Inner(visitor):
    node = OtherOuterNode.InnerNode()
    method  = visitor.dispatch_find_method_by_mro(node, 'foo')
    nodeName, visitorsName = method(node)
    assert  nodeName == "OtherOuterNode.InnerNode"
    assert  visitorsName == "foo_OtherOuterNode_InnerNode"


    
