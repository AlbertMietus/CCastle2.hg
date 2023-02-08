# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentClass

from .test_3b_CompInterface import emptyComp

ref_emptyClass="""\
struct CC_B_ComponentClass  cc_C_empty = {
 .isa           = NULL,
 .interface     = &cc_CI_empty,
 .instance_size = sizeof(CC_C_empty),
 .methods       = cc_B_empty_methods,
};
"""

def test_0(emptyComp):
    emptyClass = CC_B_ComponentClass(emptyComp)
    assert CCompare(ref_emptyClass, emptyClass.render())




@pytest.mark.skip(reason="More CompClass-tests are needed")
def test_more(): pass
