# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR
from . import _expression

from .operators import _bin_op

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
    op    : _bin_op
    right : AIGR
