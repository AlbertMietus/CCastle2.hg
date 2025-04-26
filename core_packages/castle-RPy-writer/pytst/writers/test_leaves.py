# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle import aigr 
from castle.aigr import ID
from castle.writers.RPy.writers import Renderer


@pytest.fixture # COPY-PAST-- pytst/HelloWorlds/__init__.py
def my_renderer() ->Renderer:
    cls = Renderer
    logger.debug(f'Using "{cls}" as Renderer')
    return cls()


def test_visit_ID(my_renderer):
    node = ID("id")
    txt = my_renderer.visit(node)
    assert txt == str(node)

def test_render_ID(my_renderer): # ends in '\n'
    node = ID("id")
    txt = my_renderer.render(node)
    assert txt == str(node) + "\n"

def test_visit_fString(my_renderer):
    node = aigr.fString("NoVars")
    txt = my_renderer.visit(node)
    assert txt == '"' + node.value + '"'

def test_render_fString(my_renderer):
    node = aigr.fString("NoVars")
    txt = my_renderer.render(node)
    assert txt == '"' + node.value + '"' +'\n'
    



def test_noSubNodes(my_renderer):
    for node in (
            ID('a'),
            aigr.fString("NoVars"),
            ): # XXX Add more nodes
        assert my_renderer.render_subNodes(node) is None

