# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from dataclasses import dataclass
import pytest

from castle import aigr
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

@dataclass
class DummyNode(aigr.NamedNode):
    name       :aigr.ID

@pytest.fixture
def dummy():
    return DummyNode('dummy')

def find_impl(start: aigr.Source_NS, name:str) ->aigr.ComponentImplementation:
    comp = ScaffolderNameSpace(start).findNode(name)
    assert comp, f"`{name}` should be in file/SOURCE_NS, but isn't -- comp={comp}, start={start}"
    assert isinstance(comp, aigr.ComponentImplementation), f"check: {type(comp)}"
    return  comp
