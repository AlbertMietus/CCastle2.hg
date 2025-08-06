# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import pytest

from castle.aigr import NamedNode, Specialise
from castle.aigr import Argument


@pytest.fixture
def named_node():
    return NamedNode('Generic')

@pytest.fixture
def specialised_node(named_node):
    return Specialise('Specialise', based_on=named_node, arguments=[Argument(name='demo', value=42), Argument(2024)])

@pytest.fixture
def nameless_specialised_node(named_node):
    return Specialise(None, based_on=named_node, arguments=[Argument(name='demo', value=42), Argument(2024)])


def test_1_Specialise_basic(specialised_node):
    assert specialised_node.name == 'Specialise'
    assert specialised_node.based_on.name == 'Generic'

def test_1a_Specialise_autoName_None(named_node):
    NoneName  = Specialise(name=None, based_on=named_node, arguments=[])
    assert 'Generic' in NoneName.name

def test_1b_Specialise_autoName_Empty(named_node):
    EmptyName = Specialise(name="",   based_on=named_node, arguments=[])
    assert 'Generic' in EmptyName.name

def test_1c_Specialise_autoName_ArgNames(nameless_specialised_node):
    assert 'Specialised' in nameless_specialised_node.name
    assert 'Generic'     in nameless_specialised_node.name
    assert 'demo'        in nameless_specialised_node.name
    assert '42'          in nameless_specialised_node.name
    assert '2024'        in nameless_specialised_node.name


