# (C) Albert Mietus, 2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the BASIC1 Sieve protocols
   documented in :
       *  .../TestDoubles_packages/TestDoubles-aigr-sieve/doc/basic1-import.puml
       *  http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols
from . import verify_Protocol


def test_0_all_sieveProtocols_exist():
    for p in (protocols.StartSieve, protocols.SlowStart, protocols.SimpleSieve):
        assert isinstance(p, aigr.EventProtocol)

def test_1_StartSieve():
    p = protocols.StartSieve
    verify_Protocol(p, name="StartSieve", my_event_names=('runTo', 'newMax'))

def test_1_SlowStart():
    p = protocols.SlowStart
    verify_Protocol(p, name="SlowStart", my_event_names=['setMax'])

def test_2_SlowStart_1():
    p = protocols.SlowStart_1
    verify_Protocol(p, name="SlowStart_1", cls=aigr.Specialise, base=protocols.SlowStart, my_event_names=['setMax'])

def test_2_SimpleSieve():
    p = protocols.SimpleSieve
    verify_Protocol(p, name="SimpleSieve", base=protocols.SlowStart_1, total_no_of_event=2, my_event_names=['input'])



def test_99_update():
    assert False
