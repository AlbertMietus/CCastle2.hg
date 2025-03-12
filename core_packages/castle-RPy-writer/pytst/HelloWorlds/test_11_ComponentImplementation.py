# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer, verify_line, verify_line_by_line
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
    verify_line('    def __init__(self, *args):',   txt, 2)
    verify_line('        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)', txt, 3)
    verify_line('        self._castle_init(*args)', txt, 4)
    ### XXXX ToDo: init instance vars


EXPECTED_RPY_CODE="""\
class CC_Elemental_HelloWorld(buildin.CC_B_Component):

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init(*args)


    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def Power_powerOn__power(self, max):
        self.HelloWorld('''Elemental''')


cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )

CC_P_Power_On = 1 # XXX ToDo: move to ..
cc_S_Elemental_HelloWorld_power = [
    None,
    CC_Elemental_HelloWorld.Power_powerOn__power,
    ]
""" #C&P: HelloWorld.rpy

def test_4_full(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    #print_out(EXPECTED_RPY_CODE, label='expected')
    #print_out(txt,      label='got/txt')
    verify_line_by_line(EXPECTED_RPY_CODE, txt)
