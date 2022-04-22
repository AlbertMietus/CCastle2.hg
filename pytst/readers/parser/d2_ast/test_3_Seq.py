"""Test that a kind of  sequence's are Expression()
"""

import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser.grammar import language as rules
from castle.ast import grammar as AST

from . import parse, assert_ID, assert_Seq


def test_seq_of_one_as_single_expr():
    txt = "A"
    ast = parse(txt, rules.single_expr)

    assert_ID(ast, 'A'), "An Id as single_expr results in an ID()"

def test_seq_of_two_is_NOT_a_single_expression():
    txt = "A B"
    with pytest.raises(AssertionError):
        ast = parse(txt, rules.single_expr)


def test_seq_of_two_as_expression():
    txt = "A B"
    ast = parse(txt, rules.expression)
    logger.debug(f'seq2expr:: ast={ast}:{type(ast).__name__}')
    assert_Seq(ast, length=2, ids=('A', 'B'))


def test_seq_of_three_as_expression():
    txt = "A B C"
    ast = parse(txt, rules.expression)
    assert_Seq(ast, length=3, ids=('A', 'B', 'C'))


def test_seq_of_three_with_quantification():
    txt = "A? B+ C*"
    ast = parse(txt, rules.expression)

    assert_Seq(ast, 3)

    assert isinstance(ast[0], AST.Optional)
    assert isinstance(ast[1], AST.OneOrMore)
    assert isinstance(ast[2], AST.ZeroOrMore)

    assert_ID(ast[0].expr, 'A'),	"The first ID is an 'A'"
    assert_ID(ast[1].expr, 'B'),	"The 2nd ID is a 'B'"
    assert_ID(ast[2].expr, 'C'),	"The 3th one is a 'C'"


def assert_OC(ast, length_pattern):
    assert isinstance(ast, AST.OrderedChoice)
    assert isinstance(ast, AST.Expression), "An OrderedChoice is also a Expression"
    assert len(ast) == len(length_pattern), "Not the correct number of alternatives"
    for i, (alt, l) in enumerate(zip(ast, length_pattern)):
        if l is  not None:
            assert len(alt) == l, f'The {i}th alternative does not match the specified length -- {alt}'
        logger.debug(f'OC-alt[{i}] ==> {alt}')

def test_OrderedChoice_of_two_alternatives():
    txt = "A | B"
    ast = parse(txt, rules.expression)
    logger.debug(f"OC.2:: {ast}")
    assert_OC(ast, length_pattern=[1,1])

def test_OrderedChoice_of_three_alternatives():
    txt = "A | B | C"
    ast = parse(txt, rules.expression)
    logger.debug(f"OC.3:: {ast}")
    assert_OC(ast, length_pattern=[1,1,1])


def test_OrderedChoice_of_long_alternatives():
    txt = "A | b1 b2 | C"
    ast = parse(txt, rules.expression)
    logger.debug(f"OC.long:: {ast}")
    assert_OC(ast, length_pattern=[1,2,1])
