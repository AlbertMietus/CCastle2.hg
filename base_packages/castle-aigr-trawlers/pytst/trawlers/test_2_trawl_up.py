# (C) Albert Mietus, 2026. Part of Castle/CCastle project

"""Tests for Trawl.up() — the upward structural axis."""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.tools.trawlers import Trawl


@pytest.fixture
def parent():
    return aigr.NamedNode(name=ID.Def('parent'))

@pytest.fixture
def child(parent):
    return aigr.NamedNode(name=ID.Def('child'), parent=parent)

@pytest.fixture
def grandchild(child):
    return aigr.NamedNode(name=ID.Def('grandchild'), parent=child)


def test_1a_up_reaches_parent(child, parent):
    assert Trawl(child).up().one() is parent

def test_1b_up_on_root_is_empty(parent):
    assert not Trawl(parent).up().exists()

def test_1c_up_returns_trawl(child):
    assert isinstance(Trawl(child).up(), Trawl)


def test_2a_up_two_steps_reaches_grandparent(grandchild, parent):
    assert Trawl(grandchild).up(2).one() is parent

def test_2b_up_beyond_tree_depth_is_empty(grandchild):
    assert not Trawl(grandchild).up(10).exists()
