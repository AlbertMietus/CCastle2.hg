# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.monorail.base.visitors import Visitor

class FakeA(): pass
class FakeB(): pass

class Spy(Visitor):
    def visit_FakeA(self, node):
        return 'A'
    def visit_FakeB(self, node):
        return 'B'

@pytest.fixture
def spy():
    return Spy()

def test_dispatch_as_usual(spy):
    assert 'A' == spy.visit(FakeA())
    assert 'B' == spy.visit(FakeB())

def test_dispatchOn_A_returns_A(spy):
    assert 'A' == spy.visit(FakeB(), dispatch_on=FakeA())

def test_dispatchOn_ignoresNode(spy):
    assert 'A' == spy.visit("Dummy", dispatch_on=FakeA())
    assert 'A' == spy.visit(None, dispatch_on=FakeA())
    assert 'A' == spy.visit(FakeB(), dispatch_on=FakeA())
    assert 'A' == spy.visit(FakeA(), dispatch_on=FakeA())

