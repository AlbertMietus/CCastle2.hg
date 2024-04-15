# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Test the 'basic' (base) AIGR TestDoubles"""

import pytest

import castle.aigr as aigr
from castle.aigr.protocols import baseProtocol
from castle.TESTDOUBLES.aigr.base import base as base_NS

def test_0_baseProtocol_exist():
    assert isinstance(baseProtocol, aigr.Protocol)

def test_0_baseNS_exist():
    assert isinstance(base_NS, aigr.NameSpace)
    assert str(base_NS.name) == 'base'

def test_1_baseNS_has_Protocol():
    baseNS_protocol = base_NS.getID('Protocol')
    assert isinstance(baseNS_protocol, aigr.Protocol)

def test_1b_protocol_in_baseNS_is_baseProtocol():
    baseNS_protocol = base_NS.getID('Protocol')
    assert baseNS_protocol is baseProtocol


