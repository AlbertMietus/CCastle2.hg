# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest


from castle import aigr

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import elemental, wrapped_Hello_World

@pytest.fixture
def Method(wrapped_Hello_World):
    m = wrapped_Hello_World.search('Elemental_HelloWorld.HelloWorld')
    assert isinstance(m, aigr.Method) # check only, no test
    return m


def test_1_1stLine_is_def(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line('def HelloWorld(self, label):',txt, 0)


def test_2_full(Method, my_renderer):
    expected ="""\
def HelloWorld(self, label):
    print("Hello %s World" % (label,))

""" #C&P: HelloWorld.rpy::
    txt = my_renderer.render(Method)
    #print_out(expected, label='expected')
    #print_out(txt,      label='got/txt')
    verify_line_by_line(expected, txt)
