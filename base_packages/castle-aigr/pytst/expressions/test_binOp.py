# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from castle.aigr import expressions
from castle.aigr.expressions import operators
from castle.aigr import builders

def verify_binOp(expr, left, opstr, right):
    ops = {
        '%': operators.Modulo,
        '+': operators.Add
        }
    assert expr.left == left,	f"Expected '{left}' for left part of expr ({expr}), but found: {expr.left}"
    assert isinstance(expr.op, ops[opstr]), f"Expected '{opstr}'-operator, found {expr.op}. Details: needed an {ops[opstr]} class"
    assert expr.right == right, f"Expected '{right}' for right part of expr ({expr}), but found: {expr.right}"


def test_modulo_aigr():
    """The AIGR has a generic Binary Expression, with an (Modulo) Operator as parameter.

    So, 2 % 5 ==> BinExp(2, <opMod>, 5)

    However, we can *build* this structure with 'builders' methods; see below. The give the same result!
    """
    # Low-lever interface
    e = expressions.BinExpr(left=42, op=operators.Modulo(), right=5)
    verify_binOp(e, 42, '%', 5)

if False:
    def test_modulo_quick():
        # Build interface, see above
        e = builders.Modulo(42,5)
        # As the result is the same we verify the same...
        verify_binOp(e, 42, '%',5)




