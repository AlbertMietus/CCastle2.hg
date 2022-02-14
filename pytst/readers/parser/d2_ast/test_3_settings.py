import pytest

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_Setting


def test_setting_a_value42():
    txt="aNumber = 42;"
    ast = parse(txt, grammar.setting)
    assert_Setting(ast, pegType=peg.Number, name='aNumber', value='42')

def test_setting_str1():
    txt="String = '42';"
    ast = parse(txt, grammar.setting)
    assert_Setting(ast, pegType=peg.StrTerm, name='String', value='42')

def test_setting_str2():
    txt='''String = "42";'''
    ast = parse(txt, grammar.setting)
    assert_Setting(ast, pegType=peg.StrTerm, name='String', value='42')

def test_setting_re():
    txt="RegExp = /abc/;"
    ast = parse(txt, grammar.setting)
    assert_Setting(ast, pegType=peg.RegExpTerm, name='RegExp', value='abc')

def test_setting_setting_xref():
    txt="aSetting = anOtherSetting;"
    ast = parse(txt, grammar.setting)
    assert_Setting(ast, pegType=peg.ID, name='aSetting')
    assert ast.value.name == 'anOtherSetting'

