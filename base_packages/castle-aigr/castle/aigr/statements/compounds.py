# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from . import _statement, AIGR


@dataclass
class Body(_statement):
    """A `Body` is basically all "statements" between '{' and '}'. This can be the content of  callable, a Component etc.

    A `Body` can also be used as an component-statement
    """
    _kids = _statement._kids + ('statements',)

    _: KW_ONLY
    statements: list[_statement] = dc_field(default_factory=list)

    def __getitem__(self, index):
        """"Convenient function: return a statements in the body, based on an index (numbering like a list)"""
        return self.statements[index]

    def __len__(self):
        return len(self.statements)

    def expand(self, *s):
        """Convenient function: add one of more statements to the Body"""
        self.statements +=s
