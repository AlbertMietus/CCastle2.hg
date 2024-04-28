# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR
from . import _expression

from . import operators


#ToDo: option: Replace BinExpr by a more general (liniar, LR Expression sommething
@dataclass
class BinExpr(_expression):
    """A `BinExpr` models any expression two attributes (and an operator).

    Such a "binary expression" is very typical, usually written in infix nation, like `1+2`.  It has
    tree "kids", the left and right (value) attributes, and an operator.

    .. note:: Notice, by modeling it with an operator, the is no need to have "AddExpression" and simular.
        The AIGR doesn't have such an notation!

        However, the aigr.builders module has some auxiliary functions to create the correct
        "BinExp(left,<Op>,right) construct by calling builders.<Op>(left, right)."""
    _kids = _expression._kids + ('left', 'op', 'right')

    _: KW_ONLY
    left  : AIGR
    op    : operators._bin_op
    right : AIGR


@dataclass
class Compare(_expression):
    """`Compare` models the comparison of 2 or more values, resulting in a boolean.

    A more mathematical model is used, than more traditional programma languages (C*, Java) which only
    allow two values to be compared. Like in (e.g. Python) liniar multi-value comparison are possible.
    A few examples: ``1<2<3``, or ``9>8>7>5>4>3>2>1``, and even ``7>5<11`` -all resulting in True.

    An expression as ``a $op1 b $op2 c`` is the same as ``(a $op1 b) and (b $op2 c)`` where `b` is
    only evaluated once. But it is more compact (both in code as AIGR), and therefor preferred.

    The comparison (in a single `Compare()` is always left to right (left-associative).

    The .ops element defines how to compare; see the available compare-operators. There are two options:

    1. A *single* ops-operators: this operator is used [#1] for all parts.

       * You can "read" that operator between any two consecutive values.
       * #1: it the abstract operator that is reused, not the implementation of it. That is determined by
         the type (of each left) values

    2. A tuple of operators (in the ops element); always one less as the number of values.

       * Than, the values and ops can be considered as intermediate placed.

    .. attention::

       * When .ops is a tuple: len(.ops) == len(.values) -1
       * When len(values)==2, ops should not be an tuple.
    """
    _kids = _expression._kids + ('ops', 'values')

    _: KW_ONLY
    ops    : operators._compare_op | tuple[operators._compare_op]
    values : tuple[AIGR]

