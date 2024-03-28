# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""

import pytest

from castle import aigr
from castle.TESTDOUBLES.aigr.sieve import moats
from . import verify_ComponentInterface

def test_1_3interfaces():
    "Just test the 3 component-interfaces exist, and have the correct name"
    for (name, i) in {
            "Generator": moats.GeneratorMoat,
            "Sieve"    : moats.SieveMoat,
            "Finder"   : moats.FinderMoat,
            }.items():
        assert isinstance(i, aigr.ComponentInterface)
        assert str(i.name) == name
        assert i.name == aigr.ID(name)


def test_2a_generator():
    verify_ComponentInterface(moats.GeneratorMoat, "Generator", my_port_names=['controll', 'outlet'])

def test_2b_sieve():
    verify_ComponentInterface(moats.SieveMoat, "Sieve", my_port_names=['try', 'coprime'])

def test_2c_finder():
    verify_ComponentInterface(moats.FinderMoat, "Finder", my_port_names=['newPrime', 'found',])

