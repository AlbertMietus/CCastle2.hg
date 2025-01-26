# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer

@pytest.fixture
def ComponentImplementation():
    impl = Hello_World.findNode('Elemental_HelloWorld')
    assert impl # check only, no test
    return impl

def verify_line(expect, got, line=0):
    assert expect in got.splitlines()[line], f"Expected: {expect}...., got: {got}"


def test_line1_render(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line('class CC_Elemental_HelloWorld(buildin.CC_B_Component):', txt, 0)
    print(f'\nXXX\nXXX{txt}\nXXX')
