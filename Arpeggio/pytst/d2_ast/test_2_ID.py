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
    txt="aName"
    ast = parse(txt, grammar.rule_crossref)
    assert isinstance(ast, peg.ID), "It should be an ID"
    assert ast.name == txt

