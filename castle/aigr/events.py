# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" This file is based (a fork) on `../writers/CC2Cpy/Protocol.py`,
  - the rendering part is removed
  - the prefixed are gone
  - better
TODO: update the CC2Cpy parts to use this generic AIGR layer
"""
from dataclasses import dataclass, KW_ONLY
from . import AIGR
from .types import TypedParameter

__all__ = ['Event']

from dataclasses import dataclass, KW_ONLY

from castle.auxiliary import AIGR

@dataclass                              # pragma: no mutate
class Event(AIGR):
    """An event is like a (remote) function-call

    It has a name, a return-type (can be void), and a sequence of typed parameters."""

    name: str
    _: KW_ONLY # The field below must be passed as keywords, when initialising
    return_type: type=None
    typedParameters: Sequence[TypedParameter]=()                                ## A tuple `()` is inmutable
