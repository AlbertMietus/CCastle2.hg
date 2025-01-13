# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
from dataclasses import dataclass

import pytest

from castle import aigr
from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

@pytest.fixture
def elemental():
    return Hello_World

@pytest.fixture
def HW(elemental):
    comp = elemental.findNode('Elemental_HelloWorld')
    assert isinstance(comp, aigr.ComponentImplementation)
    return  comp


@dataclass
class DummyNode(aigr.NamedNode):
    name       :aigr.ID

@pytest.fixture
def dummy():
    return DummyNode('dummy')

