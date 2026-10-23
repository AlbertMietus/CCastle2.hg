# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.aigr import AIGRNode
from castle.aigr.statements.callables import _handlers
#from castle.aigr import EventHandler # is a _handlers
from castle.aigr import Method, Initializer, Call

# As basedpyright doesn't understand pytest-fixtures ..
# pyright: reportUnusedImport=false
from .fixtures import a_bundler, the_bundler
from .fixtures import forceYes_bundler, forceNo_bundler

class DummyNode(AIGRNode):pass
class MockNamed(DummyNode):
    def __init__(self):
        super().__init__("dummy")         #type: ignore

class DummyHandler(MockNamed,      _handlers)   : pass
class DummyMethod(MockNamed,       Method)      : pass
class DummyInitializer(MockNamed,  Initializer) : pass

class DummyCall(DummyNode,  Call):
    def __init__(self):
        super().__init__(callable=None)         #type: ignore


def test_0_realbundler(a_bundler):
    shall = a_bundler.shallBundle(DummyNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"
    assert shall is None

def test_0_Yes(forceYes_bundler):
    shall = forceYes_bundler.shallBundle(DummyNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"
    assert shall is True

def test_0_No(forceNo_bundler):
    shall = forceNo_bundler.shallBundle(DummyNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"
    assert shall is False

###
### (1x) The implementation side
###

def test_11__handlers_shallBundle(the_bundler): # EventHandler etc
    verify_4cls(DummyHandler, True, the_bundler)

def test_12__Method_shallNotBundle(the_bundler):
    verify_4cls(DummyMethod, False, the_bundler)

def test_12__Init_shallNotBundle(the_bundler): # sub class of Method
    verify_4cls(DummyInitializer, False, the_bundler)


###
### (2x) The calling side
###

def test_21__call_shallBundle(the_bundler): # Call & Part
    verify_4cls( DummyCall, False, the_bundler)



def verify_4cls(cls, expected, test_bundler):
    node = cls()
    got = test_bundler.shallBundle(node)
    assert got is expected, f"{expected=} for class: {cls.__name__}::({cls.__bases__[-1].__name__})    but {got=}: {cls.__module__ + "::"+ cls.__name__}"

