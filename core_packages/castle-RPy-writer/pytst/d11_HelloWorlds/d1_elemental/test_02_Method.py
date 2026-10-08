# (C) Albert Mietus, 2025. Part of Castle/CCastle project

# See file: ..../doc/devNotes/CallConventions.rst. AND pytestmark below

import logging; logger = logging.getLogger(__name__)
import pytest

pytestmark = pytest.mark.xfail(reason="""\
(a): Design Desison (ADR) needed: Does `Method` use the Bundler (or trust the RPY dispatcher)\
(b): The (renewed) `Bundler` needs work (when (un)pack/box is needed""", allow_module_level=True) #type: ignore


from castle import aigr

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import elemental, wrapped_Hello_World

@pytest.fixture
def Method(wrapped_Hello_World):
    """Find the HelloWorld method in the (elemental) HelloWorld TestDouble """
    m = wrapped_Hello_World.search('Elemental_HelloWorld.HelloWorld')
    assert isinstance(m, aigr.Method) # check only, no test
    logger.info("CC-Method: %s", m)   #XXXX
    return m

expected ="""\
def HelloWorld(self, pos, named):
    label = pos[0].value

    print("Hello %s World" % (label,))
"""


def test_1a_unpack_def_1stline(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line(expected_lines(1), txt, 0)

def test_1b_unpack_def_head(Method, my_renderer):
    txt = my_renderer.render(Method) ;
    verify_line_by_line(expected_lines(2), first_lines(txt, 2))

def test_2_full(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line_by_line(expected, txt)

def expected_lines(n):
    "Return the `n` first lines of `expected (n==1 --> one line`"
    return '\n'.join(expected.splitlines()[:n])+'\n'

def first_lines(lines, n):
    """Return the `n` first lines of"""
    return '\n'.join(lines.splitlines()[:n])+'\n'
