# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.aigr import AIGRNode

from .fixtures import a_bundler
from .fixtures import forceYes_bundler, forceNo_bundler



class MockNode(AIGRNode):pass

@pytest.mark.skip(reason="ADR00002")
def test_0_realbundler(a_bundler):
    shall = a_bundler.shallBundle(MockNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"

def test_0_Yes(forceYes_bundler):
    shall = forceYes_bundler.shallBundle(MockNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"
    assert shall is True

def test_0_No(forceNo_bundler):
    shall = forceNo_bundler.shallBundle(MockNode())
    assert shall in (True, False, None), f"Not expexcted: {shall=}"
    assert shall is False
    

    
