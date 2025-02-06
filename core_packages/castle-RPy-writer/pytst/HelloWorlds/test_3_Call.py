# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
from castle import aigr

from . import my_renderer, verify_line
from . import print_out

@pytest.fixture
def Call():
    call=Hello_World.search('Elemental_HelloWorld.HelloWorld').body[0].call
    assert isinstance(call, aigr.Call) # Check only
    return call

def test_1_render_visitCallNeedsMoreWork_ButFineForNow(Call, my_renderer):
    txt = my_renderer.render(Call)
    verify_line("print(f'''Hello {label} World''')", txt)



