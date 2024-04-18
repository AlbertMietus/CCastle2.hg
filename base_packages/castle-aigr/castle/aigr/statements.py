# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import AIGR

@dataclass
class _statement(AIGR): pass

@dataclass
class If(_statement):
    _kids = ('test', 'body', 'orelse')
    _ : KW_ONLY
    test:   AIGR                     # Boolean Expr
    body:   AIGR                     # Typical: `AIGR.Body`
    orelse: PTH.Optional[AIGR]=None  # Typical: `AIGR.Body | AIGR.If`

@dataclass
class Become(_statement):
    """ It can be a single assignment as `a:=2`; or `b=foo()`; or more complex ones ...

        * Multiple assignment: `a,b := b,a` -- works as expected: swap the values
        * For multiple assignment `len(targets)==len(values)`
        * Tuple assignment `a := 1,2,3` is also possible -- then the two tuples do not have the same length
        * Un/Packing as in Python `a,*b,c= 1,2,3,4,5;` is also possible -- here 'b' becomes '2,3,4'

        Currently, only single assignment are supported -- so both tuples have len==1

    """
    _kids = ('targets', 'values')
    _ : KW_ONLY
    targets: tuple[AIGR]                   # LHS: (sequence of) Variables etc
    values:  tuple[AIGR]                   # RGS: (sequence of) Values
