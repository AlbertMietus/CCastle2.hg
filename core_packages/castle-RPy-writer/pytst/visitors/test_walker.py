# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers.RPy.writers.walker import Walker



@pytest.fixture
def Hello_World():
    from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
    return Hello_World

@pytest.fixture
def tree():
    return Walker()

def test_1_Hello_World_hasComp(tree, Hello_World):
    nodes = tree.visit(Hello_World)
    assert len(nodes) == 1, f"Expect only ComponentImplementation, but got: {nodes}"
    assert isinstance(nodes[0], aigr.ComponentImplementation)
