# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from castle.aigr.expressions import operators
from .. import verifyKids

import pytest
import logging; logger = logging.getLogger(__name__)

def verify_binOp(expr, left, opstr, right):
    ops = {
        '**' : operators.Power,
        '*'  : operators.Times,
        '/'  : operators.Div,
        '%'  : operators.Modulo,
        '+'  : operators.Add,
        '-'  : operators.Sub,
        }
    assert isinstance(expr.op, ops[opstr]), f"Expected '{opstr}'-operator, found {expr.op}. Details: needed an {ops[opstr]} class"
    assert expr.values[0] == left,	f"Expected '{left}' for values[0] of expr ({expr}), but found: {expr.values[0]}"
    assert expr.values[1] == right,	f"Expected '{right}' for values[1] of expr ({expr}), but found: {expr.values[1]}"
    verifyKids(expr)
