# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Test the correct handling of mistakes, in using the Visitor class."""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle.monorail.base import visitors

class FakeNode(): pass
MockFake_Marker:str = "MockFake_Maker"

class SpyVisitor(visitors.Visitor):
    def __init__(self):
        logger.info("SpyVisitor.__init__() is called")
        super().__init__()
        self.spy :str = ""

    def Mock_FakeNode(self, node:PTH.Any) ->str:
        self.spy  = f"visit_FakeNode"
        logger.info("SpyVisitor.Mock_FakeNode is called for %s", node)
        return MockFake_Marker

@pytest.fixture
def visitor():
    return SpyVisitor()

def test_1_UnknownPrefix_Mock(visitor):
    dummy = FakeNode()
    m = visitor._visitor(dummy, prefix='Mock')
    assert m is MockFake_Marker
    assert visitor.spy == "visit_FakeNode"

def test_1_NoMethod(visitor):
    dummy = None
    m = visitor._visitor(dummy, prefix='ReallyRealyNot')
    assert m is None
    assert visitor.spy == '', "No Spy Method should have been called."




