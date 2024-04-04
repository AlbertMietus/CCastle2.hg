import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser.grammar import language as rules
from castle.ast import grammar as AST

from . import parse, assert_ID, precondition_ID, precondition_Expressions

def simple_ID_Predicate_ID(txt, predicateType, rule_name='R', id0='A', predicateID='B', id2='C'):
    ast = parse(txt, rules.parse_rule)
    precondition_ID(ast.name, rule_name)

    expr = ast.expr
    precondition_Expressions(expr, length=3, type=AST.Sequence)
    precondition_ID(expr[0], id0)
    precondition_ID(expr[2], id2)

    predicate= expr[1]
    logger.debug(f'predicate: {predicate}')

    assert isinstance(predicate, AST.Predicate)
    assert isinstance(predicate, predicateType)
    assert_ID(predicate.expr, predicateID)

def test_simple_AndPredicate():
    simple_ID_Predicate_ID("R <- A &B C;", AST.AndPredicate)

def test_simple_NotPredicate():
    simple_ID_Predicate_ID("R <- A !B C;", AST.NotPredicate)
