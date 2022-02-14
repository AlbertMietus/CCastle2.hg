import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_Rule, assert_ParseRule, assert_Setting

def test_some_parse_rules():
    txt="""R1 <- A;
           R2 <- B;"""
    ast = parse(txt, grammar.rules)

    assert isinstance(ast, peg.Rules)
    assert len(ast) == 2, "We expect the same number as Rules as lines"
    for p in ast:
        assert_ParseRule(p)

def test_some_setting_rules():
    txt="""S1 = A;
           S2 = 42;"""
    ast = parse(txt, grammar.rules, visitor_debug=False)

    assert isinstance(ast, peg.Rules)
    assert len(ast) == 2, "We expect the same number as Rules as lines"
    for s in ast:
        assert_Setting(s)

def test_mixed_rules():
    txt="""M1 <- A;
           M2 =  B;"""
    ast = parse(txt, grammar.rules, visitor_debug=False)

    assert isinstance(ast, peg.Rules)
    assert len(ast) == 2, "We expect the same number as Rules as lines"
    for r in ast:
        assert_Rule(r)



