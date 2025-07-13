# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import  AIGR, ID
from . import _expression
from ..base import types

@dataclass
class _literal(_expression):
    _: KW_ONLY
    value : PTH.Any
    type  : PTH.Optional[types._types] = None

@dataclass
class Constant(_literal):
    """A (literal) Constant is a value that is given in code-text, like 0 (an int), 3.14 (a float) or "Hoi" (a string)"""

    pass


@dataclass
class _TemplateLiteral(_literal):
    """A template literal is like a **f-string** in Python, or a **tagged template literal** in JavaScript;
       but more generic: not only for strings"""
    _: KW_ONLY
    formater : PTH.Any = None  #Typical: aigr.statements.callables._callable
    args     : list[ID] = dc_field(default_factory=list)

@dataclass
class fString(_TemplateLiteral):
    """"XXX Name can change
        This `_TemplateLiteral` results in a string, by filling in the (str) value of (local) variables.
        It is like fstrings in python (but potential more restricted)"""

    value : str # Allow to set without keyword
    _: KW_ONLY

    def __post_init__(self):
        if self.type is None:
            self.type  = types.string
        if self.formater is None:
            self.formater = 'XXX'
