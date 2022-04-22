import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar as rules
from castle.ast import grammar as AST

from . import parse, assert_ID, assert_Seq, assert_ParseRule


def test_trivial_rule_with_2IDS():
    """The most simple rule has only two IDs"""

    txt="trivial <- cross ;"
    ast = parse(txt, rules.parse_rule)

    assert_ParseRule(ast, rule_name=txt.split()[0])                # The name of a rule is a ID with the left-side ID as name

    expr = ast.expr
    assert_Seq(expr, length=1)
    assert_ID(expr[0], txt.split()[2], "The single element of the expression is an ID (the 2nd) --  which name is the 3 part of the txt")


def test_rule_with_ID_and_terms():
    txt = """aRule <- 'aStr' aCross /regexp/ ;"""
    ast = parse(txt, rules.parse_rule)

    assert_ParseRule(ast, rule_name=txt.split()[0])

    expr = ast.expr;
    assert_Seq(expr, length=3)

    assert isinstance(expr[0], AST.StrTerm)
    assert expr[0].value == 'aStr'

    assert_ID(expr[1], "aCross")

    assert isinstance(expr[2], AST.RegExpTerm)
    assert expr[2].value == 'regexp'


