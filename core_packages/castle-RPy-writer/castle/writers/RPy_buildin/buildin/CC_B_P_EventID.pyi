# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_P_EventID``.

import typing as PTH
from .._debug import DebugMixIn

class CC_B_P_EventID(DebugMixIn):
    """Describes a single event within a :class:`CC_B_Protocol`.

    Created in generated code and appended to ``cc_P_<Name>.events``
    after the protocol is constructed.

    Usage (in generated code)
    -------------------------
    ::

        cc_P_Clock.events.append(buildin.CC_B_P_EventID(
            name    = "tick",
            seqNo   = 0,
            part_of = cc_P_Clock,
        ))
    """

    name: str
    """Event name."""
    seqNo: int
    """Sequence number within the protocol (currently ``-99`` in generated code)."""
    parameters: list[PTH.Any]
    """Event parameters (currently always empty)."""
    part_of: PTH.Any
    """The :class:`CC_B_Protocol` this event belongs to."""

    def __init__(
        self,
        name: str,
        seqNo: int,
        parameters: list[PTH.Any] = ...,
        part_of: PTH.Any = ...,
    ) -> None: ...
