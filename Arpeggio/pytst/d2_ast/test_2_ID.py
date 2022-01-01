import pytest

import grammar

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

from . import parse, assert_ID


def test_rule_name():
    """The name of a rule is an ID"""

    txt="aName"
    ast = parse(txt, grammar.rule_name)
    assert_ID(ast, name=txt)


def test_rule_crossref():
    """The rule's expressions can also refer an ID"""

    txt="aRef"
    ast = parse(txt, grammar.rule_crossref)
    assert_ID(ast, name=txt)


def test_ID_as_expressions():
    """ An ID is also an expression"""

    txt="aRef"
    ast = parse(txt, grammar.expressions)

    assert isinstance(ast, peg.Expression),	"A crossref is also an Expression"
    assert len(ast.value) == 1,			"An expression with length==1"
    assert_ID(ast.value[0], name=txt, err_message= "The name of the (ID of the) Expression-value is still the same")


