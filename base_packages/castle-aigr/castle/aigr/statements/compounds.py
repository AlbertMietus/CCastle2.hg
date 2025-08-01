# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
#import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR


@dataclass
class Body(_statement):
    """A `Body` is basically all "statements" between '{' and '}'. This can be the content of  callable, a Component etc.

    A `Body` can also be used as an component-statement
    """
    _: KW_ONLY
    statements: list[_statement] = dc_field(default_factory=list)

