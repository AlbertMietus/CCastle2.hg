# (C) Albert Mietus, 2024. Part of Castle/CCastle project

"""Verify multiple statements has kids :-)"""

import pytest
from .. import Dummy, verifyKids
from castle.aigr import statements

@pytest.fixture
def DummyName():
    return Dummy("This will work for kids-test")

def test_kids_VoidCall(DummyName):
    s = statements.VoidCall(DummyName)
    verifyKids(s)

def test_kids_EventHandler(DummyName):
    # None means `default` in CastleCode. which is **untypical** -- But fine for this test
    s = statements.EventHandler(DummyName, protocol=None, event=None, port=None )
    verifyKids(s)


