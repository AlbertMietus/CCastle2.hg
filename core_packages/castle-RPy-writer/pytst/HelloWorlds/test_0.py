# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest

from castle import aigr
from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

def test_0_dummy():
    "Just check the aigr-TestDouble can be read"
    assert isinstance(Hello_World, aigr.Source_NS),  f"Unexpected class: {Hello_World}"
    assert Hello_World.name == 'HelloWorld'

@pytest.mark.skip
def test_1_render():
    assert 'ToDo'
