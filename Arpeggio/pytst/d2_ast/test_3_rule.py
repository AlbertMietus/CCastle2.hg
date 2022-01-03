import pytest
import logging; logger = logging.getLogger(__name__)

import grammar
from castle import peg # has the AST classes

from . import parse, assert_ID

def test_trivial_rule_with_2IDS():
    """The most simple rule has only two IDs"""

    txt="trivial <- cross ;"
    ast = parse(txt, grammar.rule)

    assert isinstance(ast, peg.Rule), 		"It should be an ID"
    assert_ID(ast.name, txt.split()[0], "The name of a rule is a ID with the left-side ID as name")

    expr = ast.expr;
    assert isinstance(expr, peg.Expression), 	"The expression is an Expression ..."
    assert isinstance(expr, peg.Sequence),	" .. and a Sequence .."
    assert len(expr) == 1, 			" .. of length==1"
    assert_ID(expr[0], txt.split()[2], "The single element of the expression is an ID (the 2nd) --  which name is the 3 part of the txt")


def test_rule_with_ID_and_terms():
    txt = """aRule <- 'aStr' aCross /regexp/ ;"""
    ast = parse(txt, grammar.rule)

    assert isinstance(ast, peg.Rule), 		"It should be an ID"
    assert_ID(ast.name, txt.split()[0], "The name of a rule is a ID with the left-side ID as name")

    expr = ast.expr;
    assert isinstance(expr, peg.Expression), 	"The expression is an Expression ..."
    assert isinstance(expr, peg.Sequence),	" .. and a Sequence .."
    assert len(expr) == 3, 			" .. of length==3"

    assert isinstance(expr[0], peg.StrTerm)
    assert expr[0].value == 'aStr'

    assert_ID(expr[1], "aCross")

    assert isinstance(expr[2], peg.RegExpTerm)
    assert expr[2].value == 'regexp'


