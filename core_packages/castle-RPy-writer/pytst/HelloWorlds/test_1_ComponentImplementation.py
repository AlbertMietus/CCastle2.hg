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

def verify_line(expect, got, line=None):
    txt = got.splitlines()[line] if line else got
    assert expect in txt, f"Expected: {expect}...., got: {got}"


def test_line1_render(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line('class CC_Elemental_HelloWorld(buildin.CC_B_Component):\n', txt,0)

def test_render_init(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line('    def __init__(self, *args):', txt)
    print(f'\n<<<\n{txt}>>>')
