# (C) Albert Mietus, 2026. Part of Castle/CCastle project
# mostly generated with codeAI, & seen as "good enough" by Albert
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.writers.RPy_buildin.buildin import *

def test_0a_CC_B_int_is_CC_B_Value():
    assert isinstance(CC_B_int(1), CC_B_Value)

def test_0b_CC_B_float_is_CC_B_Value():
    assert isinstance(CC_B_float(1.0), CC_B_Value)

def test_0c_CC_B_string_is_CC_B_Value():
    assert isinstance(CC_B_string("hi"), CC_B_Value)

def test_0d_CC_B_boolean_is_CC_B_Value():
    assert isinstance(CC_B_boolean(True), CC_B_Value)

##Note
##
## The old test, using .value to unpack are outdated (and wrong/misleading)
##
## Reading .value, for multiple types is not rpython -- it can't handle it
## We have to use the unbox (staticmethod)!!
##
## See pytst/d06_RPy_buildin/test_0_CC_B_Values.py
