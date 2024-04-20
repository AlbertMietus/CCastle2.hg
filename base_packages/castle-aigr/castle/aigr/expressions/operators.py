# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR

class _operator(AIGR): pass
class _bin_op(_operator): pass

class Power(_bin_op)  :'**'
class Times(_bin_op)  : '*'
class Div(_bin_op)    : '/'
class Modulo(_bin_op) : '%'
class Add(_bin_op)    : '+'
class Sub(_bin_op)    : '-'
