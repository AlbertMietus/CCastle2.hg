# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import pytest
from castle.aigr import expressions
from castle.aigr.expressions import operators
#from castle.aigr import builders


def test_simple_eq():
    """Test (modeling) a simple "2-value" comparison, using the equal operator --again no execution.

    .. note:: `expressions.compare()` also handles complex, cascaded/liniar comparison with different operators.
       Then, .ops can be an tuple. But for simple comparison it is always a operators directly.
       Therefore, both `ops=` and `values=` need a tuple as input."""
    e = expressions.Compare(ops=operators.Equal(), values=(1,2))
    verify_simple(e)

def test_simple_all():
    values=('X','Y')
    for op_cls in operators._compare_op.__subclasses__():
        logger.info("testing SIMPLE (2-value) comparison with: op: %s with %s", op_cls.__name__, values)
        e = expressions.Compare(ops=op_cls(), values=values)
        assert e.values is values and isinstance(e.ops, op_cls)
        assert verify_simple(e)

def test_single_all():
    """An Comparison can have a single operator, with multiple (>2) values.
     It almost the same as simple, but more values - testing it (the model) is trivial when simple works"""
    for i, op_cls in enumerate(operators._compare_op.__subclasses__(),3):
        values=tuple(f'val_{j}' for j in range(i))
        logger.info("testing SINGLE (1-op) comparison with: op: %s with %s", op_cls.__name__, values)
        e = expressions.Compare(ops=op_cls(), values=values)
        assert e.values is values and isinstance(e.ops, op_cls)
        assert verify_single(e)

def test_multi_1():
    """``a is a==2!=4<b<=5>4>=4 in [1,2,3,4,5] is not [1,2,3,b,5] not in [1,2,3,4,5,6]``,
         assuming a:=2, b:=4, is True -- fun & useless:-)"""
    e = expressions.Compare(ops=(
                  operators.Is(),
                  operators.Equal(),
                  operators.Notequal(),
                  operators.Less(),
                  operators.LessEqual(),
                  operators.Greater(),
                  operators.GreaterEqual(),
                  operators.In(),
                  operators.IsNot(),
                  operators.IsNot()
                ), values=('a','a', 2,4,'b',5,4,4, [1,2,3,4,5], [1,2,3,'b',5], [1,2,3,4,5,6]))
    assert len(e.ops) == len(e.values)-1 #Trivial test


def _verify_base(e):
    assert not isinstance(e.ops, (tuple, list)), f"Expect a single ops for simple comparisons, not {e.ops} (a ({type(e.ops).__name__}))"
    assert not isinstance(e.ops, type), f"Expect instance, not a class ({e.ops})"
    assert isinstance(e.ops, operators._compare_op), f"Need a {operators._compare_op.__name__} subtype, not: {e.ops}"
    assert isinstance(e.values, tuple), f"values should be a tuple - got: {e.values}"

def verify_simple(e):
    _verify_base(e)
    #Note: Compare() can hande tuples of 2+; for =2, we call it simple, for 2+ we call it single (or multi)
    assert len(e.values)==2, f"Simple (2-values) comparisons need a tuple of 2... not: {e.values}"
    return True

def verify_single(e):
    _verify_base(e)
    #Note: Compare() can hande tuples of 2+; for =2, we call it simple, for 2+ we call it single (or multi)
    assert len(e.values)>2, f"To compare 3 or more values, the values-tuple should be longer than: : {e.values}"
    return True
