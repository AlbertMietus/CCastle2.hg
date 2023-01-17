# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from typing import TypeAlias, ClassVar, Optional
from dataclasses import dataclass, field as dc_field, KW_ONLY
from collections.abc import Sequence # Use for typing


fstring: TypeAlias=str # a Fix (sized) string. May be inplemented as a C-string, a Pascal-string, or ...

class CC_Base: pass

@dataclass
class CC_TypedParameter(CC_Base):
    """This is many a helper class/struct to combine a parameter: a name and an type"""
    name: fstring
    type: type
