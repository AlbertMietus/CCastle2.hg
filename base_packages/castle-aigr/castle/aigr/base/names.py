# (C) Albert Mietus, 2023/24. Part of Castle/CCastle project
from __future__ import annotations

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from .AIGR import AIGR

class _Context(AIGR)  : "The context of an ID (base class) (Def/Ref/Set)"       # pragma: no mutate
class Def(_Context)   : "Here, the name is defined"                             # pragma: no mutate
_Def_cls = Def # Alias
@dataclass                                                                      # pragma: no mutate
class Ref(_Context):
    "Points to a Def() of an name"                                              # pragma: no mutate
    _ : KW_ONLY
    reference: PTH.Optional[AIGR] = None
_Ref_cls= Ref # Alias, as ID.Ref also uses Ref ...

@dataclass                                                                      # pragma: no mutate
class Set(_Context):
    "Here, the name is set/changed"                                             # pragma: no mutate
    _ : KW_ONLY
    reference: PTH.Optional[PTH.Any] = None  ##not used for now                 # pragma: no mutate

RefType = PTH.TypeVar("RefType", bound=AIGR)

class ID(str, AIGR):
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
          return f'ID(`{str(self)}`/{repr(self.context)})'

    class Def:
        def __new__(cls, name:str) -> ID.Def:
            """`ID.Def()` creates an ID with Def() context; and ID.Def is a type-hint"""
            return PTH.cast(ID.Def, ID(name, context=_Def_cls()))

    class Ref(PTH.Generic[RefType]):
        """`ID.Ref()` creates an ID with Ref() context. && ID.Ref[type] can be used as type-hint"""

        def __new__(cls, name:str, context:RefType|_Ref_cls) -> ID.Ref:
            if not isinstance(context, _Ref_cls):
                context = _Ref_cls(reference=context)
            return PTH.cast(ID.Ref, ID(name, context))

        def __class_getitem__(cls, item):          # Needed for generic type-hinting
            return PTH.Optional[item]


class Label(str):
    """A `Label` is a string, but unlike an ID it's NOT USED in CastleCode. This is an "internal" name, in the AIGR."""

QualID = list[ID]  # To be used a PTH
