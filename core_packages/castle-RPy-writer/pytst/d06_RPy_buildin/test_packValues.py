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


def test_1a_CC_B_int_value():
    assert CC_B_int(1).value == 1

def test_1b_CC_B_float_value():
    assert CC_B_float(1.5).value == 1.5

def test_1c_CC_B_string_value():
    assert CC_B_string("hi").value == "hi"

def test_1d_CC_B_boolean_value():
    assert CC_B_boolean(True).value == True


def test_2a_CC_B_int_casts():
    assert CC_B_int(1.9).value == 1

def test_2b_CC_B_float_casts():
    assert CC_B_float(1).value == 1.0

def test_2c_CC_B_string_casts():
    assert CC_B_string(42).value == "42"

def test_2d_CC_B_boolean_casts():
    assert CC_B_boolean(0).value == False
