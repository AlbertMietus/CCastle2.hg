import pytest

import grammar

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

from . import parse

def test_rule_name():
    """The name of a rule is an ID"""
    txt="aName"
    ast = parse(txt, grammar.rule_name)
    assert isinstance(ast, peg.ID), "It should be an ID"
    assert ast.name == txt

def test_rule_crossref():
    """The rule's expressions can also refer an ID"""
    txt="aRef"
    ast = parse(txt, grammar.rule_crossref)
    assert isinstance(ast, peg.ID), "It should be an ID"
    assert ast.name == txt


def test_ID_as_single_expr():
    txt="aRef"
    ast = parse(txt, grammar.single_expr)
    assert isinstance(ast, peg.Expression),	"A crossref is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert ast.value[0].name == txt, 		"The name of the (ID of the) Expression-value is still the same"

def test_ID_as_expressions():
    txt="aRef"
    ast = parse(txt, grammar.expressions)
    assert isinstance(ast, peg.Expression),	"A crossref is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert ast.value[0].name == txt, 		"The name of the (ID of the) Expression-value is still the same"

