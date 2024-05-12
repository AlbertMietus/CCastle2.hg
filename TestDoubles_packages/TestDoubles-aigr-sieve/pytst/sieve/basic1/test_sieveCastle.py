# (C) Albert Mietus 2024, Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols (basic1 variant)
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.TESTDOUBLES.aigr.sieve.basic1 import sieveCastle
from castle import aigr

from . import find_name_in_body


@pytest.fixture
def comp():
    return sieveCastle.Sieve


def test_0a_types(comp):
    assert isinstance(comp, aigr.ComponentImplementation)
    assert isinstance(comp.interface, aigr.ComponentInterface)
    assert isinstance(comp.parameters, (type(None), tuple))
    assert isinstance(comp.body, aigr.Body)

def test_0b_nameIsName(comp):
    assert comp.name == comp.interface.name
    assert comp.name == 'Sieve'

def test_0c_noParms(comp):
    assert comp.parameters == ()

def test_has_init(comp):
    init = find_name_in_body('init', comp.body)
    assert isinstance(init, aigr.Method), f"Expected an init method, got {init}"

def test_init_has_body(comp):
    init = find_name_in_body('init', comp.body)
    assert len(init.body)==2, f"Expected that 'init' has 2 statements, but found: {len(init.body.statements)}"

