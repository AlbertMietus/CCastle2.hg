# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from . import *


def test_ID(my_renderer):
    node = ID("id")
    assert my_renderer.visit(node) == str(node)
    assert my_renderer.render(node) ==  str(node) + "\n"

def test_intConstant(my_renderer):
    node = aigr.Constant(value=123, type=aigr.types.int)
    assert my_renderer.visit(node) == "123"
    assert my_renderer.render(node) == "123\n"

def test_floatConstant(my_renderer):
    node = aigr.Constant(value=3.14, type=aigr.types.float)
    assert my_renderer.visit(node) == "3.14"
    assert my_renderer.render(node) == "3.14\n"

def test__stringConstant(my_renderer):
    node = aigr.Constant(value='str', type=aigr.types.string)
    assert my_renderer.visit(node) == "'''str'''"
    assert my_renderer.render(node) == "'''str'''\n"

def test_fString_simple(my_renderer):
    node = aigr.fString("NoVars")
    assert my_renderer.visit(node) == '"NoVars"'
    assert my_renderer.render(node) == '"NoVars"\n'

def test_fString_value(my_renderer):
    node = aigr.fString(value="NoVars")
    assert my_renderer.visit(node) == '"NoVars"'
    assert my_renderer.render(node) == '"NoVars"\n'

def test_fString_value_str(my_renderer):
    node = aigr.fString(value="NoVars", type=aigr.types.string,)
    assert my_renderer.visit(node) == '"NoVars"'
    assert my_renderer.render(node) == '"NoVars"\n'

def test_fString_1parm(my_renderer):
    expected = '"A%sC" % (b,)'
    node = aigr.fString(value="A{b}C", args=[ID('b')])
    assert my_renderer.visit(node) == expected
    assert my_renderer.render(node) ==  expected + '\n'

def test_fString_someParm(my_renderer):
    expected = '"A=%s B=%s C=%s" % (a, b, c,)'
    node = aigr.fString(value="A={a} B={b} C={c}", args=[ID('a'),ID('b'),ID('c')])
    assert my_renderer.visit(node) == expected
    assert my_renderer.render(node) ==  expected + '\n'
    
def test_noSubNodes(my_renderer):
    for node in (
            ID('a'),
            aigr.Constant(value=123, type=aigr.types.int),
            aigr.Constant(value=3.14, type=aigr.types.float),
            aigr.Constant(value='str', type=aigr.types.string),
            aigr.fString("NoVars"),
            ): # XXX Add more nodes
        assert my_renderer.render_subNodes(node) is None

