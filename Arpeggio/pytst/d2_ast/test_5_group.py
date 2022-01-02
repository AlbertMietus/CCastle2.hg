import pytest
import logging;logger = logging.getLogger(__name__)

import grammar
from castle import peg # has the AST classes

from . import parse, assert_ID

def test_simple_group():
    txt = "R <- ( A B ) ;"

    ast = parse(txt, grammar.rule)
    assert_ID(ast.name, 'R')

    grp = ast.expr
    assert len(grp)==1,			"There should be only one expr; the group"
    assert isinstance(grp[0], peg.Sequence)

    assert_ID(grp[0][0], 'A')
    assert_ID(grp[0][1], 'B')

def test_nested_group():
    txt = "R <- ( (  A B ) ) ;"

    ast = parse(txt, grammar.rule)
    assert_ID(ast.name, 'R')

    grp = ast.expr
    assert len(grp)==1, "There should be only one expr; the group"
    assert isinstance(grp[0], peg.Sequence)

    ngrp = grp[0]
    assert len(ngrp)==1
    assert isinstance(ngrp[0], peg.Sequence)

    assert_ID(ngrp[0][0], 'A')
    assert_ID(ngrp[0][1], 'B')

