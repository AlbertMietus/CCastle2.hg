# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest


from castle import aigr


from . import my_renderer, verify_line
from . import print_out
from . import elemental, wrapped_Hello_World

@pytest.fixture
def Call(wrapped_Hello_World): ### Not a great way to navigate, but fine for Now....
    method = wrapped_Hello_World.search('Elemental_HelloWorld.HelloWorld')
    statements = method.body.statements
    call = statements[0].call
    assert isinstance(call, aigr.Call) # Check only
    return call


def test_1_render_visitCallNeedsMoreWork_ButFineForNow(Call, my_renderer):
    EXPECTED = '''print("Hello %s World" % (label,))'''
    txt = my_renderer.render(Call)
    verify_line(EXPECTED, txt)



