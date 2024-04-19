# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR
from . import _expression



@dataclass
class BinExpr(_expression):
    _: KW_ONLY
    left: AIGR
    op: int
    right: AIGR
    


