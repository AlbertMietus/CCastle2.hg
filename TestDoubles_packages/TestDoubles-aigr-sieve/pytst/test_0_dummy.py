# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
"""Check that the  AIGR TestDoubles  'the sieve' are available
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
   See 'test_1... (and more) for in-depth tests"
"""


import pytest

import castle.aigr as aigr
from castle.TESTDOUBLES.aigr.sieve import protocols
from castle.TESTDOUBLES.aigr.base  import Protocol as base_Protocol


def test_0_Oke():
    return

def test_1_all_sieveProtocols():
    for p in (protocols.StartSieve, protocols.SlowStart, protocols.SimpleSieve):
        assert isinstance(p, aigr.EventProtocol)

    for p in (protocols.SlowStart_1,):
        assert isinstance(p, aigr.protocols.ProtocolWrapper) # ProtocolWrapper isn't exported

def test_2_baseProtocol():
    assert isinstance(base_Protocol, aigr.Protocol)
