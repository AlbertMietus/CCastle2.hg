# (C) Albert Mietus, 2024. Part of Castle/CCastle project

""" Often Left-(-2-Right) associative operators are use as bin-operator, like `2+3`. They are tested here.

    An expressions as ``2+3`` becomes (in the AIGR) an Lift-associative expression, with operator 'Add' and values
    '(2,3)'.  Such an "LR-expression" can have more values, e.g. 'Min' with '(3,2,1)' as values. That represents:
    ``3-2-1``, resulting in 0).
    Those "longer" expressions are tested in ``test_LRlong.py`

   .. note:: An example of a expression that is not left-associative is power (operator: '**').

       ``2**3**4`` is the same as ``2**(3**4)``, and is right associative

"""

import pytest
import logging; logger = logging.getLogger(__name__)
from .. import verifyKids

from castle.aigr import expressions
from castle.aigr.expressions import operators
from castle.aigr import builders

def verify_binOp(expr, left, opstr, right):
    ops = {
        '*' : operators.Times,
        '/' : operators.Div,
        '%' : operators.Modulo,
        '+' : operators.Add,
        '-' : operators.Sub,
        }
    assert isinstance(expr.op, ops[opstr]), f"Expected '{opstr}'-operator, found {expr.op}. Details: needed an {ops[opstr]} class"
    assert expr.values[0] == left,	f"Expected '{left}' for values[0] of expr ({expr}), but found: {expr.values[0]}"
    assert expr.values[1] == right,	f"Expected '{right}' for values[1] of expr ({expr}), but found: {expr.values[1]}"
    verifyKids(expr)

# We start with modulo, as we have to start somewhere ...

def test_modulo_aigr():
    """The AIGR has no true binary expression; it a special case of the Left (or Right) generics Associative expression.

    Here, we show that with the Modulo Operator, it's a parameter to an LRexpression, which has a tuple of "values". 
    With a 2-tuple it represents a binary (modulo) expression.

    So, ``42 % 5`` ==> LRexpression(<opMod>, (42,5))
    """
    # Low-lever interface
    e = expressions.LRexpression(op=operators.Modulo(), values=(42,5))
    verify_binOp(e, 42, '%', 5)

def test_modulo_quick():
    """ The aigr (as module) has some (quick) builders, to build the same structure as above: ``builders.Modulo()``
    """
    # Use the builders interface for the same modulo expression
    e = builders.Modulo(42,5)
    # As the result is the same we verify the same...
    verify_binOp(e, 42, '%',5)

def test_modulo_same():
    """They really are equivalent ..."""
    assert builders.Modulo(42,5) == expressions.LRexpression(op=operators.Modulo(), values=(42,5))

# Now the others, in a compact test

def test_add():
    e1 = expressions.LRexpression(op=operators.Add(), values=(42,5))
    e2 = builders.Add(42,5)
    verify_binOp(e1,42,'+',5)
    verify_binOp(e2,42,'+',5)
    assert e1 == e2

# Now the builders are meta-build, they are all the same. And we can use them here to test/verify the low-level
# structure by only using those quick-builders


def quick_verify_binOp(builder, opstr):
    left, right = 1234,5678
    verify_binOp(builder(left, right), left, opstr, right)

def test_all_quick():
    for builder, opstr in [
            (builders.Times,  '*'),
            (builders.Div,    '/'),
            (builders.Modulo, '%'),
            (builders.Add,    '+'),
            (builders.Sub,    '-'),
            ]:
        logger.debug("testing: %s (%s)", builder, opstr)
        quick_verify_binOp(builder, opstr)



