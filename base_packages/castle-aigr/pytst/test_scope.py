# (C) Albert Mietus, 2025,  Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints


from castle.aigr import ID
from castle.aigr import Scope
from castle.aigr import ComponentImplementation

from . import a_node

@pytest.fixture
def aComp():
    return ComponentImplementation(ID('aComp'))


def test_ComponentImplementation_hasScope(aComp, a_node):
    aComp.register(a_node)
    assert aComp.findNode('a_node') is a_node

