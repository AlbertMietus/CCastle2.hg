"""Test that a sequence of expressions is an Expression()

   Note: the value of Expression() is a list-subclass; which is fine. But use it as list!!"""

import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_ID, assert_Seq


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

    assert_Seq(ast, 2, ids=('A', 'B'))
    assert isinstance(ast.value, list),		"It will be an `arpeggio.SemanticActionResult` which is a subclass of list"


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

