# (C) Albert Mietus, 2023,2024 Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""

import pytest
from castle.TESTDOUBLES.aigr.sieve.basic1 import moats

from castle import aigr


def test_0_all_interfaces():
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
    verify_ComponentInterface(moats.GeneratorMoat, "Generator", port_names=['controll', 'outlet'])

def test_2b_sieve():
    verify_ComponentInterface(moats.SieveMoat, "Sieve", port_names=['try', 'coprime'])

def test_2c_finder():
    verify_ComponentInterface(moats.FinderMoat, "Finder", port_names=['newPrime', 'found',])




def verify_ComponentInterface(i, name, port_names):
    assert isinstance(i, aigr.ComponentInterface)
    assert str(i.name) == name, f"{i.name} reported but expected: {name}"

    for no, name in enumerate(port_names):
        assert str(i.ports[no].name) == name, f"{i.name} (own/local) port no={no}: {i.ports[no].name}, expected: {name} (str-compare)"
        assert i.ports[no].name == aigr.ID(name),  f"{i.name} (own/local) port no={no}: {i.ports[no].name}, expected: {name} (ID)"
