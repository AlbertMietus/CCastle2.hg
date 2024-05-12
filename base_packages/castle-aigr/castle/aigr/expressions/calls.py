# (C) Albert Mietus, 2023-2024. Part of Castle/CCastle project

from __future__ import annotations # Postponed evaluation of annotations
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .. import AIGR, ID, errors
from . import _expression



class _call(_expression):pass # _kids = _expression._kids

@dataclass
class Call(_call):
    """ A `Call` is e.g. a method/function-call; but also a call by a 'function-pointer' is a `Call`
    """
    _kids = _call._kids + ('callable', 'arguments')

    _: KW_ONLY
    callable  : AIGR # often a name but a "function-pointer" is an option too
    arguments : PTH.Optional[tuple[AIGR, ...]]=()


@dataclass
class Part(_call):
    """A `Part` is like 'a.b' (attribute) or `a[1]` (index). It's illegal to use both 'attribute' and 'index' together.

    It's a `_call` as the compiler will call a method (of 'base') to calculate the result-- so it (like an operator too
    """
    _kids = _call._kids + ('base', 'attribute', 'index')

    base      : PTH.Optional[AIGR]          # Usually an ID, but can be a ref/pointer, return-value etc
    _: KW_ONLY
    attribute : PTH.Optional[AIGR] = None   # Usually an ID
    index     : PTH.Optional[AIGR] = None   # Can be a number, an ID, or ....

    def __post_init__(self):
        if (self.attribute is not None) and (self.index is not None):
            raise errors.PartError("Use only ONE:  attribute or index, not both:: {self.attribute} and {self.index}")
        if (self.attribute is None) and (self.index is  None):
            raise errors.PartError("Use ONE: attribute or index - now both are None")

