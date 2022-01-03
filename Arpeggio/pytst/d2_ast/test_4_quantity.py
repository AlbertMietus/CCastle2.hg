"""  Test several optional parts of an expression -- mosty quantity suffixes like '?' '*' and '+' -- also '#' although is different"""

import pytest
import logging; logger = logging.getLogger(__name__)

import grammar
from castle import peg # has the AST classes

from . import parse, assert_ID

def assert_Quantification(token:str, kind:type(peg.Quantity)):
    txt = f"R <- X {token} ;"

    ast = parse(txt, grammar.rule)
    assert_ID(ast.name, 'R')

    expr = ast.expr
    assert len(expr)==1,			"There should be only one expr"

    assert isinstance(expr[0], peg.Quantity), 	"It should be a (sub of) Quantity .."
    assert isinstance(expr[0], kind),		f"... namely the specified one: {kind}"

    opt_ex = expr[0].expr
    assert_ID(opt_ex, 'X', "should be same a the expr; without the Quantification")


def test_Optional():
    assert_Quantification('?', peg.Optional)

def test_ZeroOrMore():
    assert_Quantification('*', peg.ZeroOrMore)

def test_OneOrMore():
    assert_Quantification('+', peg.OneOrMore)

