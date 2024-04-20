# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR
from . import _expression

@dataclass
class Call(_expression):
    _kids = _expression._kids + ('callable', 'arguments')
    _: KW_ONLY
    callable  : AIGR # often a name but a "function-pointer" is an option too
    arguments : PTH.Optional[tuple[AIGR, ...]]=()
