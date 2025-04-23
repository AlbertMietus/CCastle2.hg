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

@pytest.mark.xfail(reason="First I need to workout dottedID in general. Then: 'base.cc_CI_Component'")
def test_1_full(implicietComp, my_renderer):
    txt = my_renderer.render(implicietComp)
    #print_out(txt, label="implicietComp")
    verify_line('cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(',	txt, 0)
    verify_line('    name         = "Elemental_HelloWorld",',						txt, 1)
    verify_line('    ports        = (),',											txt, 3)
    verify_line('    )',															txt, 4)
    #Move this up, when it works
    verify_line('    inherit_from = base.cc_CI_Component,',							txt, 2) # dottedID: base.cc_CI_Component ? XXXX
