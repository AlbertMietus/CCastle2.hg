# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
from castle import aigr

from . import my_renderer, verify_line


@pytest.fixture
def fString():
    call=Hello_World.search('Elemental_HelloWorld.HelloWorld').body[0].call
    assert isinstance(call, aigr.Call) # Check only
    arg0=call.arguments[0]
    assert isinstance(arg0, aigr.fString) # Check only
    return arg0

def test_visit_fString(fString, my_renderer):
    """Bypass the render method, check only `visit_fString()` -- As the text below fails"""
    txt = my_renderer.visit_fString(fString)
    assert txt == '''"Hello %s World" % (label,)''', f"Got: {repr(txt)}"


def test_render_fString(fString, my_renderer):
    """Now via the render method""" # It (did/once) fail as it adds newlines
    assert fString.value == "Hello {label} World" #Check only

    EXPECTED = '''"Hello %s World" % (label,)\n''' # with newline

    txt = my_renderer.render(fString)

    verify_line(EXPECTED, txt)     # At least the EXPECTED text is there
    verify_line(EXPECTED, txt, 0)   # But no more lines are needed



