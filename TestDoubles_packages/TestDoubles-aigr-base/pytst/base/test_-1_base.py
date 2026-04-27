# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Test the 'basic' (base) AIGR TestDoubles"""

import pytest

import castle.aigr as aigr
#from castle.aigr.protocols import baseProtocol #baseProtocol is GONE
from castle.aigr.tools.scaffolding import ScaffolderNameSpace
#from castle.TESTDOUBLES.aigr.base import base as base_NS


#def test_0_baseProtocol_exist():
#    assert isinstance(baseProtocol, aigr.Protocol)

#def test_0_baseNS_exist():
#    assert isinstance(base_NS, aigr.NamedSpace)
#    assert str(base_NS.name) == 'base'

#def test_1_baseNS_has_Protocol():
#    baseNS_protocol = ScaffolderNameSpace(base_NS).getID('Protocol')
#    assert isinstance(baseNS_protocol, aigr.Protocol)

#def test_1b_protocol_in_baseNS_is_baseProtocol():
#    baseNS_protocol = ScaffolderNameSpace(base_NS).getID('Protocol')
#    assert baseNS_protocol is baseProtocol

def test_NeverFail():
    'Just a test to make sure this file is not empty'
    assert True

