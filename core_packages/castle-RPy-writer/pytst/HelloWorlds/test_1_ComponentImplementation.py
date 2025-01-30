# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer, verify_line
from . import print_out

@pytest.fixture
def ComponentImplementation():
    impl = Hello_World.findNode('Elemental_HelloWorld')
    assert impl # check only, no test
    return impl


def test_1_1stLine_is_class(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line('class CC_Elemental_HelloWorld(buildin.CC_B_Component):\n', txt,0)

def test_2_render_init(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    print_out(txt)
    verify_line('    def __init__(self, *args):',   txt, 2)
    verify_line('        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)', txt, 3)
    verify_line('        self._castle_init(*args)', txt, 4)

def test_3_depart(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line('cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(', txt)#, 6)
    verify_line('    interface = cc_CI_Elemental_HelloWorld,',              txt)#, 7)
    print_out(txt)


@pytest.mark.xfail(reason="TODO")
def test_depart_801():
    assert False, 'TODO: lineno in verify_line -- but empty lines do not work in Block'


@pytest.mark.skip
def test_NotBut_print(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    print_out(txt)



