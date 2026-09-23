# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import elemental, wrapped_Hello_World

expected ="""\
def HelloWorld(self, pos, named):
    label = pos[0].value

    print("Hello %s World" % (label,))
"""
def expected_lines(n):
    return '\n'.join(expected.splitlines()[:n])+'\n'


@pytest.fixture
def Method(wrapped_Hello_World):
    m = wrapped_Hello_World.search('Elemental_HelloWorld.HelloWorld')
    assert isinstance(m, aigr.Method) # check only, no test
    return m

@pytest.mark.xfail(reason="Rendering.Call/Bundler:: .unpack is needed")
def test_1a_unpack_def_1stline(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line(expected_lines(1), txt, 0)

@pytest.mark.xfail(reason="Rendering.Call/Bundler:: .unpack is needed")
def test_1b_unpack_def_head(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line(expected_lines(2), txt, 2)

@pytest.mark.xfail(reason="Rendering.Call/Bundler:: .unpack is needed")
def test_2_full(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line_by_line(expected, txt)
