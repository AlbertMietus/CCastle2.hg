# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle import aigr
from castle.aigr import ID
from castle.writers.RPy.writers import Renderer

from .. import my_renderer


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

def test_fString(my_renderer):
    node = aigr.fString("NoVars")
    assert my_renderer.visit(node) == '"NoVars"'
    assert my_renderer.render(node) == '"NoVars"\n'


def test_noSubNodes(my_renderer):
    for node in (
            ID('a'),
            aigr.Constant(value=123, type=aigr.types.int),
            aigr.Constant(value=3.14, type=aigr.types.float),
            aigr.Constant(value='str', type=aigr.types.string),
            aigr.fString("NoVars"),
            ): # XXX Add more nodes
        assert my_renderer.render_subNodes(node) is None

