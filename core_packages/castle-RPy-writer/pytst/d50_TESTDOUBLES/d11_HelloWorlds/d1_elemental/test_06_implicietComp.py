# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out

from . import elemental, wrapped_Hello_World

@pytest.fixture
def implicietComp(wrapped_Hello_World):
    component_implementation = wrapped_Hello_World.findNode('Elemental_HelloWorld')
    component_interface = component_implementation.interface
    assert component_interface # check only, no test
    return component_interface


def test_0(implicietComp):
    from castle import aigr
    assert isinstance(implicietComp, aigr.ComponentInterface)

def test_1_full(implicietComp, my_renderer):
    txt = my_renderer.render(implicietComp)
    #print_out(txt, label="implicietComp")
    verify_line('cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(',	txt, 0)
    verify_line('    name         = "Elemental_HelloWorld",',						txt, 1)
    verify_line('    inherit_from = base.cc_CI_Component,',							txt, 2)
    verify_line('    ports        = [],',											txt, 3)
    verify_line('    )',															txt, 4)

