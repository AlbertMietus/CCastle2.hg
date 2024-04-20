# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from castle.aigr import expressions
from castle.aigr.expressions import operators
from castle.aigr import builders

def verify_binOp(expr, left, opstr, right):
    ops = {
        '**': operators.Power,
        '*' : operators.Times,
        '/' : operators.Div,
        '%' : operators.Modulo,
        '+' : operators.Add,
        '-' : operators.Sub,
        }
    assert expr.left == left,	f"Expected '{left}' for left part of expr ({expr}), but found: {expr.left}"
    assert isinstance(expr.op, ops[opstr]), f"Expected '{opstr}'-operator, found {expr.op}. Details: needed an {ops[opstr]} class"
    assert expr.right == right, f"Expected '{right}' for right part of expr ({expr}), but found: {expr.right}"

# We start with modulo, as we have to start somewhere ...

def test_modulo_aigr():
    """The AIGR has a generic Binary Expression, with an (Modulo) Operator as parameter.

    So, 2 % 5 ==> BinExp(2, <opMod>, 5)

    However, we can *build* this structure with 'builders' methods; see below. The give the same result!
    """
    # Low-lever interface
    e = expressions.BinExpr(left=42, op=operators.Modulo(), right=5)
    verify_binOp(e, 42, '%', 5)

def test_modulo_quick():
    # Build interface, see above
    e = builders.Modulo(42,5)
    # As the result is the same we verify the same...
    verify_binOp(e, 42, '%',5)

def test_modulo_same():
    """They really are equivalent ..."""
    assert builders.Modulo(42,5) == expressions.BinExpr(left=42, op=operators.Modulo(), right=5)

# Now the others, in a compact test

def test_add():
    e1 = expressions.BinExpr(left=42, op=operators.Add(), right=5)
    e2 = builders.Add(42,5)
    verify_binOp(e1,42,'+',5)
    verify_binOp(e2,42,'+',5)
    assert e1 == e2

# Now the builders are meta-build, they are all the same. And we can use them here to test/verify the low-level
# structure by only using those quick-builders

def test_Power():
    left, right = 1234,5678
    verify_binOp(builders.Power(left, right), left, '**', right)

def quick_verify_binOp(builder, opstr):
    left, right = 1234,5678
    verify_binOp(builder(left, right), left, opstr, right)


def test_all_quick():
    for builder, opstr in [
            (builders.Power,  '**'),
            (builders.Times,  '*'),
            (builders.Div,    '/'),
            (builders.Modulo, '%'),
            (builders.Add,    '+'),
            (builders.Sub,    '-'),
            ]:
        quick_verify_binOp(builder, opstr)
