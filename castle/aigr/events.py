# (C) Albert Mietus, 2023. Part of Castle/CCastle project


import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from .aid import TypedParameter                                                                       # Castle/AIGR type
from .namednodes import *

__all__ = ['Event']




@dataclass                                                                                          # pragma: no mutate
class Event(NamedNode):
    """An event is like a (remote) function-call

    It has a name, a return-type (can be void), and an (inmutable) sequence of typed parameters."""
    _: KW_ONLY
    return_type: PTH.Optional[type]=None
    typedParameters: PTH.Sequence[TypedParameter]=()

