# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR
from .. import expressions

@dataclass
class Become(_statement):
    """The statement ``Become`` models a single assignment, with can have multiple targets & values...

       * A Single-assignment, is the typical use, like in  `a:=2;` or `b:=foo();`
       * Multiple assignment: `a,b := b,a'` -- works as expected: swap the values
       * For multiple assignment `len(targets)==len(values)`
       * Tuple assignment `a := 1,2,3` is also possible -- then the two tuples do not have the same length
       * Un/Packing as in Python `a,*b,c= 1,2,3,4,5;` is also possible -- here 'b' becomes '2,3,4'

       Currently, only single assignment are supported -- so both tuples have len==1
    """
    _kids = _statement._kids + ('targets', 'values')

    _ : KW_ONLY
    targets: tuple[AIGR]                   # LHS: (sequence of) Variables etc
    values:  tuple[AIGR]                   # RGS: (sequence of) Values

@dataclass
class VoidCall(_statement):
    """As a (function) Call is an expression --not a statement--, it should be wrapped in ``VoidCall` to make it s statement.

    .. note::

       * In CastleCode, this wrapper is not needed
       * Typical VoidCall is used without named parameters
       """
    _kids = _statement._kids + ('call',)

    call : expressions.Call
