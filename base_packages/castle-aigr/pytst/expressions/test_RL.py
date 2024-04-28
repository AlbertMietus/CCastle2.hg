# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" An 'RLexpression' in AIGR is very alike the RLexpressions, but the association is Right (to Left). An example is '**' (power).

   The test are also very similar."""

import pytest
import logging; logger = logging.getLogger(__name__)

from castle.aigr import expressions
from castle.aigr.expressions import operators
from castle.aigr import builders

from . import verify_binOp

def test_power_with_2values():
    e = expressions.RLexpression(op=operators.Power(), values=(1,2))
    verify_binOp(e, 1, '**', 2)

def test_power_builder():
    e = builders.Power(42,5)
    verify_binOp(e, 42, '**', 5)

def test_power_same():
    assert builders.Power(1,2,3,4,5) == expressions.RLexpression(op=operators.Power(), values=(1,2,3,4,5))

RightAssociative = [
    (operators.Power,  		'**'),
    ]

def test_all_RL_many_values():
    for op, opstr in RightAssociative:
        logger.debug("testing: %s (%s)", op, opstr)
        e = expressions.RLexpression(op=op(), values=range(10))
        assert len(e.values) == 10
        assert isinstance(e.op, op), f"Expecting {op}, got {e.op}"
        assert isinstance(e.op, operators._RightAssociative), f"Check: only Right Associative, not {e.op}"

def test_all_are_all():
    buildin_operators = operators._RightAssociative.__subclasses__()
    all_tested = [ op for op,_ in RightAssociative]
    for op in buildin_operators:
        assert op in all_tested, f"{op} is not part of the test, but listed in build-in operators {buildin_operators}"
    assert len(buildin_operators) == len(all_tested)

