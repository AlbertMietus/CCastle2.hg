import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_Rule

def test_some_rules():
    txt="""R1 <- A;
           R2 <- B;"""
    ast = parse(txt, grammar.rules, print_tree_debug=False, visitor_debug=False)

    assert isinstance(ast, peg.Rules)
    assert len(ast) == 2, "We expect the same number as Rules as lines"
    for r in ast:
        assert_Rule(r)


