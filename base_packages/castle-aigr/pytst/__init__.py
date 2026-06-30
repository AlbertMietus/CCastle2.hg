# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints

from random import randint
import dataclasses
from dataclasses import dataclass, KW_ONLY

from castle.aigr import AIGR, ID
from castle.aigr import If
from castle.aigr import NamedNode, NamedSpace

from castle.aigr.tools.scaffolding import ScaffolderNameSpace

@dataclass
class Dummy(AIGR):
    mark: PTH.Any

    def __repr__(self):
        return f'<Dummy.{self.mark}>'

@dataclass
class DummyNode(NamedNode):
    name       :str
    _: KW_ONLY
    dummy      :PTH.Any=None

@pytest.fixture
def a_node():
    return DummyNode("a_node", dummy=randint(42,2023))

@pytest.fixture
def outer_NS(a_node):
    ns = NamedSpace(ID('outer_namespace'))
    ScaffolderNameSpace(ns).register(a_node)
    return ns


def verifyMark(dummy, mark):
    logger.debug("verifyMark: dummy=%s, mark=%s", dummy, mark)
    if mark is None:
        assert dummy is None
    else:
        assert isinstance(dummy, Dummy)
        assert dummy.mark == mark, f"Expecting mark: {mark}, but got {dummy.mark}"



def verifyisDataClass(cls):
    logger.debug("verifyisDataClass: %s ", cls)
    assert dataclasses.is_dataclass(cls) # This will also pass when cls inherits from a dataclass
    my_init = getattr(cls, '__init__')
    inherited_init = getattr(cls.mro()[1], '__init__')
    assert my_init is not inherited_init, f"Probably you subclasses a dataclass, but forgot @dataclass for {cls}"



