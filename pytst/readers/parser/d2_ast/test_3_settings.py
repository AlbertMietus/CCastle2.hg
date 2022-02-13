import pytest

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse

def validate_setting(ast, pegType=None, name=None, value=None):
    assert isinstance(ast, peg.Setting)
    assert isinstance(ast.name, peg.ID)
    assert isinstance(ast.value, (peg.StrTerm, peg.RegExpTerm, peg.Number))

    if pegType: assert isinstance(ast.value, pegType)
    if name:    assert ast.name.name == name
    if value:   assert ast.value.value == value


def test_setting_a_value42():
    txt="aNumber = 42;"
    ast = parse(txt, grammar.setting)
    validate_setting(ast, pegType=peg.Number, name='aNumber', value='42')

def test_setting_str1():
    txt="String = '42';"
    ast = parse(txt, grammar.setting)
    validate_setting(ast, pegType=peg.StrTerm, name='String', value='42')

def test_setting_str2():
    txt='''String = "42";'''
    ast = parse(txt, grammar.setting)
    validate_setting(ast, pegType=peg.StrTerm, name='String', value='42')

def test_setting_re():
    txt="RegExp = /abc/;"
    ast = parse(txt, grammar.setting)
    validate_setting(ast, pegType=peg.RegExpTerm, name='RegExp', value='abc')
