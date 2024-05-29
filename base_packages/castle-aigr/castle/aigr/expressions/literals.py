# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR
from . import _expression

class _literal(_expression):pass # _kids = _expression._kids

@dataclass
class Constant(_literal):
    """A (literal) Constant is a value that is given in code-text, like 0 (an int), 3.14 (a float) or "Hoi" (a string)"""

    _kids = _literal._kids + ('value', 'type')

    _: KW_ONLY
    value : PYH.Any
    type  : PTH.Optional[type] = None



