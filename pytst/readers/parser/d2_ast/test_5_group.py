import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar as rules
from castle.ast import grammar as AST

from . import parse, assert_ID, assert_ParseRule, assert_Seq


def assert_Group(grp, length=1, groupType=AST.Sequence, ids=None):
    assert len(grp)==length
    assert isinstance(grp[0], groupType)
    if ids:
        for i, name in enumerate(ids):
            assert_ID(grp[0][i], name)

def test_simple_group():
    txt = "R <- ( A B ) ;"

    ast = parse(txt, rules.parse_rule)
    assert_ParseRule(ast, 'R')

    grp = ast.expr
    assert_Group(grp, ids=('A', 'B'))


def test_nested_group():
    txt = "R <- ( (  A B ) ) ;"

    ast = parse(txt, rules.parse_rule)
    assert_ParseRule(ast, 'R')

    grp = ast.expr
    assert_Group(grp)

    ngrp = grp[0]
    assert_Group(ngrp,ids=('A', 'B'))


def test_unordered_group():
    txt = "R <- ( A B )# ;"

    ast = parse(txt, rules.parse_rule)
    assert_ParseRule(ast, 'R')

    grp = ast.expr
    assert_Group(grp, groupType=AST.UnorderedGroup)

    exp = grp[0].expr
    assert_Seq(exp, length=2)
    assert_ID(exp[0], 'A')
    assert_ID(exp[1], 'B')

