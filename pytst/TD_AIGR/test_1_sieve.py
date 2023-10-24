# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Test AIGR representation of the TheSieve protocols
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""

import pytest

import castle.aigr as aigr
from TestDoubles.AIGR.sieve import protocols
from TestDoubles.AIGR.base import Protocol  as base_Protocol


def verify_Protocol(p, name, event_names, base=None, no_events=None, cls=None):
    if base is None:
        base=base_Protocol
    if no_events is None:
        no_events = len(event_names)
    if cls is None:
        cls = aigr.EventProtocol

    assert isinstance(p, cls)
    assert p.name == name
    assert p.based_on is base
    assert p._noEvents() == no_events
    for no, name in enumerate(event_names):
        assert p.events[no].name == name



def test_StartSieve():
    p = protocols.StartSieve
    verify_Protocol(p, name="StartSieve", event_names=('runTo', 'newMax'))

def test_SlowStart():
    p = protocols.SlowStart
    verify_Protocol(p, name="SlowStart", event_names=['setMax'])

def test_SlowStart_1():
    from castle.aigr.protocols import ProtocolWrapper
    p = protocols.SlowStart_1
    verify_Protocol(p, name="SlowStart_1", cls=ProtocolWrapper, base=protocols.SlowStart, event_names=['setMax'])

def test_SimpleSieve():
    p = protocols.SimpleSieve
    verify_Protocol(p, name="SimpleSieve", base=protocols.SlowStart_1, event_names=['input'])



