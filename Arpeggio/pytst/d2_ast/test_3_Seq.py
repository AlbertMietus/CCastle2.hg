"""Test that a sequence of expressions is an Expression()

   Note: the value of Expression() is a list-subclass; which is fine. But use it as list!!"""

import pytest
import logging; logger = logging.getLogger(__name__)

import grammar
from castle import peg # has the AST classes

from . import parse, assert_ID


def assert_Seq(ast, length=None):
    assert isinstance(ast, peg.Sequence)
    assert isinstance(ast, peg.Expression),	"A sequence is aslo an Expression()"
    if length:
        assert len(ast) == length,  		f" ... of specified length=={length}"


def test_seq_of_one_as_single_expr():
    txt = "A"
    ast = parse(txt, grammar.single_expr)

    assert_ID(ast, 'A'), "An Id as single_expr results in an ID()"

def test_seq_of_two_is_NOT_a_single_expression():
    txt = "A B"
    with pytest.raises(AssertionError):
        ast = parse(txt, grammar.single_expr)


def test_seq_of_two_as_expressions():
    txt = "A B"
    ast = parse(txt, grammar.expressions)

    assert_Seq(ast, 2)
    assert isinstance(ast.value, list),		"It will be an `arpeggio.SemanticActionResult` which is a subclass of list"
    assert_ID(ast[0], 'A'),			" ... the first one is ID('A')"
    assert_ID(ast[1], 'B'),			"... and the 2nd: ID('B')"


def test_seq_of_three_with_quantification():
    txt = "A? B+ C*"
    ast = parse(txt, grammar.expressions)

    assert_Seq(ast, 3)

    assert isinstance(ast[0], peg.Optional)
    assert isinstance(ast[1], peg.OneOrMore)
    assert isinstance(ast[2], peg.ZeroOrMore)

    assert_ID(ast[0].expr, 'A'),	"The first ID is an 'A'"
    assert_ID(ast[1].expr, 'B'),	"The 2nd ID is a 'B'"
    assert_ID(ast[2].expr, 'C'),	"The 3th one is a 'C'"

