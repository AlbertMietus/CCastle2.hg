import pytest

from castle.readers.parser import grammar as rules
from castle.ast import grammar as AST

from . import parse, assert_ID


def test_rule_name():
    """The name of a rule is an ID"""

    txt="aName"
    ast = parse(txt, rules.rule_name)
    assert_ID(ast, name=txt)


def test_rule_crossref():
    """The rule's expression can also refer an ID"""

    txt="aRef"
    ast = parse(txt, rules.rule_crossref)
    assert_ID(ast, name=txt)


def test_ID_as_expression():
    """ An ID is also an expression"""

    txt="aRef"
    ast = parse(txt, rules.expression)

    assert isinstance(ast, AST.Expression),	"A crossref is also an Expression"
    assert len(ast) == 1,			"An expression with length==1"
    assert_ID(ast[0], name=txt, err_message= "The name of the (ID of the) Expression-value is still the same")
