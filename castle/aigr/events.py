# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" This file is based (a fork) on `../writers/CC2Cpy/Protocol.py`,
  - the rendering part is removed
  - the prefixed are gone
  - better
TODO: update the CC2Cpy parts to use this generic AIGR layer
"""

import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from .aid import TypedParameter                                                                       # Castle/AIGR type
from .namednodes import *

__all__ = ['Event']




@dataclass                                                                                          # pragma: no mutate
class Event(NamedNode):
    """An event is like a (remote) function-call

    It has a name, a return-type (can be void), and an (inmutable) sequence of typed parameters."""

    name: str
    _: KW_ONLY
    return_type: PTH.Optional[type]=None
    typedParameters: PTH.Sequence[TypedParameter]=()

