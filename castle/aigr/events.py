# (C) Albert Mietus, 2023. Part of Castle/CCastle project

from dataclasses import dataclass, KW_ONLY

from castle.auxiliary import AIGR

@dataclass                              # pragma: no mutate
class Event(AIGR):
    """An event is like a (remote) function-call

    It has a name, a return-type (can be void), and a sequence of typed parameters."""

    name: str
    _: KW_ONLY # The field below must be passed as keywords, when initialising
    return_type: type=None
    typedParameters: Sequence[CC_TypedParameter]=()                                ## A tuple `()` is inmutable
