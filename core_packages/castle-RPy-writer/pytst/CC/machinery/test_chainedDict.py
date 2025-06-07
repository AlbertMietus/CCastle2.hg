# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC.buildin.machinery import ChainedDict

@pytest.fixture
def cd():
    d = ChainedDict()
    d['key'] = 'value'
    return d

@pytest.fixture
def chain(cd):
    return ChainedDict(cd)

def test_1_asDict(cd):
    assert cd['key'] == 'value'

def test_2_chain(cd, chain):
    assert cd['key'] == 'value'
    assert chain['key'] == 'value'

def test_3a_contains_asDict(cd):
    assert 'key' in cd

def test_3b_contains_chain(chain):
    assert 'key' in chain

def test_3c_containsNot(cd, chain):
    assert not ('not_a_Key' in cd)
    assert not ('not_a_Key' in chain)

def test_4a_withMap():
    d = ChainedDict({1:2, 2:3})
    assert d[1] == 2
    assert d[2] == 3

def test_4b_withMapt():
    d = ChainedDict(
        map={
            1:2,
            2:3,
            },
        parent=None)
    assert d[1] == 2
    assert d[2] == 3
