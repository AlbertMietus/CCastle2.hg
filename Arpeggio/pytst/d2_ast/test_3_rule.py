import pytest

import grammar

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

from . import parse

def test_trivial_rule_with_2IDS():
    """The most simple rule has only two IDs"""

    txt="trivial <- cross ;"

    ast = parse(txt, grammar.rule)
    assert isinstance(ast, peg.Rule), "It should be an ID"

    name, expr  = ast.name, ast.expr;
    assert isinstance(name, peg.ID)
    assert isinstance(expr, peg.Expression), 	"The expression is an Expression ..."
    assert isinstance(expr, peg.Sequence),	" .. and a Sequence .."
    assert len(expr) ==1, 			" .. of length==1"
    assert name.name == txt.split()[0], 	"the name of the (ID of ) rule is the first ID"
    assert expr[0].name == txt.split()[2], 	"The single element of the expression is the 2nnd ID, which name os the 3 part of the txt"
