import pytest

from castle.readers.parser.grammar import language as rules
from castle.ast import grammar as AST

from . import parse, assert_Setting


def test_setting_a_value42():
    txt="aNumber = 42;"
    ast = parse(txt, rules.setting)
    assert_Setting(ast, grammarType=AST.Number, name='aNumber', value='42')

def test_setting_str1():
    txt="String = '42';"
    ast = parse(txt, rules.setting)
    assert_Setting(ast, grammarType=AST.StrTerm, name='String', value='42')

def test_setting_str2():
    txt='''String = "42";'''
    ast = parse(txt, rules.setting)
    assert_Setting(ast, grammarType=AST.StrTerm, name='String', value='42')

def test_setting_re():
    txt="RegExp = /abc/;"
    ast = parse(txt, rules.setting)
    assert_Setting(ast, grammarType=AST.RegExpTerm, name='RegExp', value='abc')

def test_setting_setting_xref():
    txt="aSetting = anOtherSetting;"
    ast = parse(txt, rules.setting)
    assert_Setting(ast, grammarType=AST.ID, name='aSetting')
    assert ast.value.name == 'anOtherSetting'

