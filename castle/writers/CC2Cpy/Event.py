# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from .CCbase import *
from dataclasses import dataclass, KW_ONLY
from collections.abc import Sequence # Use for typing

@dataclass
class CC_Event(CC_Base):
    """An event is like a (remote) function-call

       It has a name, a return-type (can be void), and a sequence of typed parameters."""

    name: fstring
    _: KW_ONLY # The field below must be passed as keywords, when initialising
    return_type: type=None
    typedParameters: Sequence[CC_TypedParameter]=()                                ## A tuple `()` is inmutable
