# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""

import pytest

import castle.aigr as aigr
from castle.TESTDOUBLES.aigr.sieve import protocols
from . import verify_Protocol


def test_0_all_sieveProtocols_exist():
    for p in (protocols.StartSieve, protocols.SlowStart, protocols.SimpleSieve):
        assert isinstance(p, aigr.EventProtocol)

    for p in (protocols.SlowStart_1,):
        assert isinstance(p, aigr.protocols.ProtocolWrapper) # ProtocolWrapper isn't exported

def test_1_StartSieve():
    p = protocols.StartSieve
    verify_Protocol(p, name="StartSieve", event_names=('runTo', 'newMax'))

def test_1_SlowStart():
    p = protocols.SlowStart
    verify_Protocol(p, name="SlowStart", event_names=['setMax'])


def test_2_SimpleSieve():
    p = protocols.SimpleSieve
    verify_Protocol(p, name="SimpleSieve", base=protocols.SlowStart_1, event_names=['input'])

def test_2_SlowStart_1():
    from castle.aigr.protocols import ProtocolWrapper
    p = protocols.SlowStart_1
    verify_Protocol(p, name="SlowStart_1", cls=ProtocolWrapper, base=protocols.SlowStart, event_names=['setMax'])



