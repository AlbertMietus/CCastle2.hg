# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import pytest

import castle.aigr as aigr
from castle.aigr.protocols import baseProtocol as ref_baseProtocol

from TestDoubles.AIGR import base

@pytest.fixture
def base_NS():
    return base.base

def test_1a_baseNS(base_NS):
    assert isinstance(base_NS, aigr.NameSpace)

def test_1b_base_has_Protocol(base_NS):
    base_Protocol = base_NS.getID('Protocol')
    assert isinstance(base_Protocol, aigr.Protocol)

def test_1b_base_is_Protocol(base_NS):
    base_Protocol = base_NS.getID('Protocol')
    assert base_Protocol is  ref_baseProtocol

