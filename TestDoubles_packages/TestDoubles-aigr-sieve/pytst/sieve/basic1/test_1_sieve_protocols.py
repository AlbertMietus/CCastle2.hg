# (C) Albert Mietus, 2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the BASIC1 Sieve protocols
   documented in :
       *  .../TestDoubles_packages/TestDoubles-aigr-sieve/doc/basic1-import.puml
       *  http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""
import logging; logger = logging.getLogger(__name__)

import pytest
from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols as sieve_protocols

from castle import aigr
from castle.TESTDOUBLES.aigr.base  import Protocol as base_Protocol



def test_0_all_sieveProtocols_exist():
    for p in (sieve_protocols.StartSieve, sieve_protocols.SimpleSieve):
        assert isinstance(p, aigr.EventProtocol)

def test_1a_StartSieve():
    p = sieve_protocols.StartSieve
    verify_Protocol(p, name="StartSieve", event_names=('runTo', 'newMax'))

def test_1b_SimpleSieve():
    p = sieve_protocols.SimpleSieve
    verify_Protocol(p, name="SimpleSieve", event_names=['input'])


def test_2a_runTo_Event():
    p = sieve_protocols.StartSieve
    e = p.events[0]
    verify_Event(e, name="runTo", return_type=None, parameters=[('max', int)])

def test_2b_newMax_Event():
    p = sieve_protocols.StartSieve
    e = p.events[1]
    verify_Event(e, name="newMax", return_type=None, parameters=[('max', int)])

def test_2c_input_Event():
    p = sieve_protocols.SimpleSieve
    e = p.events[0]
    verify_Event(e, name="input", return_type=None, parameters=[('try', int)])





def verify_Protocol(p, name, event_names,  base=None):
    if base is None: base=base_Protocol

    assert isinstance(p, aigr.EventProtocol)
    assert str(p.name) == name,  f"{p.name} reported but expected: {name}"
    assert p.based_on is base
    for no, name in enumerate(event_names):
        assert str(p.events[no].name) == name, f"{p.name} (own/local) event no={no}: {p.events[no].name}, expected: {name}"
    assert p._noEvents() == len(event_names), f"{p.name} reports {p._noEvents()} events, but expected: {len(event_names)} event(s)"

def verify_Event(e, name, return_type, parameters):
    assert isinstance(e,aigr.Event)
    assert str(e.name) == name
    assert e.return_type == return_type
    for no, (name, type) in enumerate(parameters):
        assert str(e.typedParameters[no].name) == name
        assert     e.typedParameters[no].type  == type
    assert len(e.typedParameters) == len(parameters)
