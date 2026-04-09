# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from castle  import aigr
from castle.aigr import types as CCTypes

from castle.writers.RPy.writer import portray

CC_B_= 'CC_B_'

@pytest.fixture
def prefixer():
    p= portray.PortrayType()
    return p.prefix

def test_1_TypePrefix_forString(prefixer):
    assert prefixer(CCTypes.string) == CC_B_ + 'string'

def test_2_TypePrefix_forNumbers(prefixer):
    for t, txt in [
            (CCTypes.int,     CC_B_ + 'int'),
            (CCTypes.float,   CC_B_ + 'float'),
            ]:
        assert prefixer(t) == txt

def test_3_TypePrefix_forElement(prefixer):
    element =aigr.ComponentImplementation(name='foo')
    assert prefixer(element) == 'CC_B_Component'
