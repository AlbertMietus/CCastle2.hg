# (C) Albert Mietus, 2023/24. Part of Castle/CCastle project

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from .AIGR import AIGR

class _Context(AIGR)  : "The context of an ID (base class)"

class Def(_Context)   : "Here, the name is defined"

@dataclass
class Ref(_Context):
    "Here, the name is defined"
    _ : KW_ONLY
    reference: PTH.Optional[PTH.Any] = None # like a href in html -- links to a Def - not used for now


@dataclass
class Set(_Context):
    "Here, the name is set"
    _ : KW_ONLY
    reference: PTH.Optional[PTH.Any] = None # like a href in html -- links to a Def - not used for now


class ID(str,AIGR):
    """An `ID` is a name as used in a CastleCode, for component, functions, variables etc.

    An `ID` is a string, although not all string are allowed (ony those, as typical in code. The AIGR does not, however,
    impose restrictions.
    An `ID` can have an (optional) context; is it a definition, or a reference."""

    def __new__(cls, name:str, context:PTH.Optional[_Context]=None):
       return super().__new__(cls,name)

    def __init__(self, name:str, context:PTH.Optional[_Context]=None):
        self.context=context

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        if self.context is None:
          return super().__repr__()
        else:
          return f'ID({self}/{self.context})'

class Label(str):
    """A `Label` is a string, but unlike an ID it's NOT USED in CastleCode. This is an "internal" name, in the AIGR."""







