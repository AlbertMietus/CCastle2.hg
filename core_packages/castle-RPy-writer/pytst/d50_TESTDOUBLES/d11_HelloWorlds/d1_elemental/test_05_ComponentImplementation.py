# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from . import pytestmark

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import EXPECTED_CompImplementation, EXPECTED_DispatchTables

from . import elemental, wrapped_Hello_World

@pytest.fixture
def ComponentImplementation(wrapped_Hello_World):
    impl = wrapped_Hello_World.findNode('Elemental_HelloWorld')
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

def test_4_full(ComponentImplementation, my_renderer):
    txt = my_renderer.render(ComponentImplementation)
    verify_line_by_line(EXPECTED_CompImplementation, txt)
