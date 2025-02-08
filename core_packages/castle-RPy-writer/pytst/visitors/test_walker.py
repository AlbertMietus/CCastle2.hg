# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers.RPy.writers.walker import Walker


@pytest.fixture
def tree():
    return Walker()

@pytest.fixture
def Hello_World():
    from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
    return Hello_World

def verify_Types(gotNodes, needClasses):
    assert len(gotNodes) == len(needClasses), f"Expected {len(needClasses)} nodes, but got {len(gotNodes)}"
    gotClasses = [type(n) for n in gotNodes]
    for cls in needClasses:
        assert cls in gotClasses, f"Expected (at least) a {cls}, but got only {gotClasses}"


def test_1_Hello_World_hasComp(tree, Hello_World):
    nodes = tree.visit(Hello_World)
    verify_Types(nodes, (aigr.ComponentImplementation,))

def test_2_ComponentImplementation_has_2callables(tree, Hello_World):
    """The Comp should have HelloWorld:Method and  Power_powerOn__power:EventHandler"""
    nodes = tree.visit(Hello_World.search('Elemental_HelloWorld'))
    verify_Types(nodes, (aigr.Method, aigr.EventHandler))
