# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentClass

from . import common

def test_0():
    emptyClass = CC_B_ComponentClass(common.emptyComp())
    assert CCompare(common.ref_emptyClass, emptyClass.render())




@pytest.mark.skip(reason="More CompClass-tests are needed")
def test_more(): pass
