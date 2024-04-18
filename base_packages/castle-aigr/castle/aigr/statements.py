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
