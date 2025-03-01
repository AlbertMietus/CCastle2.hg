# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import pytest

from castle.aigr.expressions import literals
from castle.aigr import types

def test_1_aConstant():
    e = literals.Constant(value=-1)
    assert e.value == -1
    assert e.type  == None

def test_2_ConstantInt():
    e = literals.Constant(value=42, type=types.int)
    assert e.value == 42
    assert e.type  == types.int

def test_3_ConstantStr():
    e = literals.Constant(value="42", type=types.string)
    assert e.value == "42"
    assert e.type  == types.string

@pytest.mark.skip("_TemplateLiteral base comes later")
def test_Template_base():
    pass

BUILD_IN_fstring = 'XXX'
def test_Template_fString(): #XXX name of class may change
    demo = 'simple Demo'
    e = literals.fString(value="This is a {demo}")
    assert e.type == types.string
    assert e.formater is BUILD_IN_fstring
