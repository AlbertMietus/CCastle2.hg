# (C) Albert Mietus, 2026. Part of Castle/CCastle project

"""Contract tests: the Scaffolder API that Trawl depends on."""

import typing as PTH
import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import AIGR, AIGRNode, NamedNode
from castle.aigr import ID


class _StubScaffolder:
    """Stub that documents and approximates the Auto_Scaffolder return type.

    Template for the real implementation.
    """

    def __init__(self, node: AIGR) -> None:
        self._node = node

    def parent(self) -> PTH.Optional[AIGRNode]:
        if isinstance(self._node, AIGRNode):
            return self._node.parent
        return None

    def kids(self) -> PTH.Sequence[AIGRNode]:
        return ()


def _stub_auto_scaffolder(node: AIGR) -> _StubScaffolder:
    return _StubScaffolder(node)


try:
    from castle.aigr.tools.scaffolding import Auto_Scaffolder
except ImportError:
    logger.warning("Using a stub for Auto_Scaffolder")
    print("\n\n\t WARNING Using a stub for Auto_Scaffolder\n")
    Auto_Scaffolder = _stub_auto_scaffolder  # type: ignore[assignment]


class _PlainAIGR(AIGR):
    """Minimal AIGR subclass — no parent field."""


@pytest.fixture
def root():
    return NamedNode(name=ID.Def('root'))

@pytest.fixture
def child(root):
    return NamedNode(name=ID.Def('child'), parent=root)


def test_0a_auto_scaffolder_wraps_an_aigr_node(root):
    wrapped = Auto_Scaffolder(root)
    assert wrapped is not None

def test_0b_auto_scaffolder_accepts_plain_aigr():
    wrapped = Auto_Scaffolder(_PlainAIGR())
    assert wrapped is not None


def test_1a_parent_of_root_is_none(root):
    assert Auto_Scaffolder(root).parent() is None

def test_1b_parent_returns_the_parent_node(child, root):
    assert Auto_Scaffolder(child).parent() is root

def test_1c_parent_of_plain_aigr_is_none():
    assert Auto_Scaffolder(_PlainAIGR()).parent() is None


def test_2a_kids_is_iterable(root):
    wrapped = Auto_Scaffolder(root)
    assert hasattr(wrapped.kids(), '__iter__')

def test_2b_kids_of_leaf_node_is_empty(root):
    wrapped = Auto_Scaffolder(root)
    assert not list(wrapped.kids())
 
