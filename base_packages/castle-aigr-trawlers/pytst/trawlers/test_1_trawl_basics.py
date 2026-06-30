# (C) Albert Mietus, 2026. Part of Castle/CCastle project

"""Tests for Trawl construction and terminator methods: exists(), one(), all()."""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID
from castle.aigr.tools.trawlers import Trawl


class _PlainAIGR(aigr.AIGR):
    """Minimal AIGR subclass — no parent field."""


@pytest.fixture
def leaf():
    return aigr.NamedNode(name=ID.Def('leaf'))


def test_0a_trawl_wraps_an_aigr_node(leaf):
    assert Trawl(leaf).exists()

def test_0b_trawl_accepts_plain_aigr_subclass():
    assert Trawl(_PlainAIGR()).exists()

def test_0c_navigation_returns_a_trawl(leaf):
    assert isinstance(Trawl(leaf).up(), Trawl)

def test_1a_one_returns_the_wrapped_node(leaf):
    assert Trawl(leaf).one() is leaf

def test_1b_all_returns_tuple_containing_node(leaf):
    assert Trawl(leaf).all() == (leaf,)

def test_1c_all_is_an_immutable_tuple(leaf):
    assert isinstance(Trawl(leaf).all(), tuple)

def test_1d_exists_is_false_when_empty(leaf):
    assert Trawl(leaf).up().exists() is False

def test_1e_one_returns_none_when_empty(leaf):
    assert Trawl(leaf).up().one() is None

def test_1f_all_returns_empty_tuple_when_empty(leaf):
    assert Trawl(leaf).up().all() == ()
