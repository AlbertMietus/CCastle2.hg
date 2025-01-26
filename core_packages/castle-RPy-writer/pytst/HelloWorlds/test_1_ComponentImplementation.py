# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer

@pytest.fixture
def ComponentImplementation():
    impl = Hello_World.findNode('Elemental_HelloWorld')
    assert impl
    return impl

 
def test_1_render(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    expected = 'class CC_Elemental_HelloWorld(buildin.CC_B_Component):'
    assert expected in txt.splitlines()[0], f"Expected: {expected}...., got: {txt}"
