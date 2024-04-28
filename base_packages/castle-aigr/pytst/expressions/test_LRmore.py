# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" An 'LRexpression' in AIGR can have 2 or more values. This file test "longer cases, as the 2-value (aka "bin-ary")
    case in tested in :file:`./test_LRbin.py`."""

import pytest
import logging; logger = logging.getLogger(__name__)

from castle.aigr import expressions
from castle.aigr.expressions import operators

def test_a_LRexpression_with3values():
    e = expressions.LRexpression(op=operators.Modulo(), values=(1,2,3))
    assert e.values == (1,2,3)

LeftAssociative = [
    (operators.Times,  		'*'),
    (operators.Div,  		'/'),
    (operators.Modulo,  	'%'),
    (operators.Add,  		'+'),
    (operators.Sub, 		'-'),
    #(operators.MatrixMult, '@'),
    ]

def test_all_LR_many_values():
    for op, opstr in LeftAssociative:
        logger.debug("testing: %s (%s)", op, opstr)
        e = expressions.LRexpression(op=op(), values=range(10))
        assert len(e.values) == 10
        assert isinstance(e.op, op), f"Expecting {op}, got {e.op}"
        assert isinstance(e.op, operators._LeftAssociative), f"Check: only Left Associative, not {e.op}"

def test_all_are_all():
    buildin_operators = operators._LeftAssociative.__subclasses__()
    all_tested = [ op for op,_ in LeftAssociative]
    for op in buildin_operators:
        assert op in all_tested, f"{op} is not part of the test, but listed in build-in operators {buildin_operators}"
    assert len(buildin_operators) == len(all_tested)
