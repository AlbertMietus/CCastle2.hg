# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import EXPECTED_CompImp

@pytest.fixture
def implicietComp():
    component_implementation = Hello_World.findNode('Elemental_HelloWorld')
    component_interface = component_implementation.interface
    assert component_interface # check only, no test
    return component_interface


def test_0(implicietComp):
    from castle import aigr
    assert isinstance(implicietComp, aigr.ComponentInterface)

def test_1_XXX(implicietComp, my_renderer):
    txt = my_renderer.render(implicietComp)
    print_out(txt)
    assert False, txt
