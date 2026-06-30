# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_Protocol``.

import typing as PTH
from .enums import CC_ProtocolKind
from .._debug import DebugMixIn

class CC_B_Protocol(DebugMixIn):
    """Runtime descriptor for a Castle protocol.

    One ``CC_B_Protocol`` instance is generated per Castle protocol
    declaration.  Events are appended after construction.

    Usage (in generated code)
    -------------------------
    ::

        cc_P_Clock = buildin.CC_B_Protocol(
            name         = "Clock",
            kind         = buildin.CC_ProtocolKind.Event,
            inherit_from = None,
            events       = [],
        )
        cc_P_Clock.events.append(buildin.CC_B_P_EventID(
            name="tick", seqNo=0, part_of=cc_P_Clock
        ))

    Either *kind* or *inherit_from* must be provided; if *kind* is ``None``
    it is inherited from the parent protocol.
    """

    name: str
    """Protocol name."""
    parameters: PTH.Any
    """Protocol type-parameters (currently unused; ``None``)."""
    inherit_from: PTH.Any
    """Parent :class:`CC_B_Protocol`, or ``None`` for base protocols."""
    base_arguments: PTH.Any
    """Base-protocol specialisation arguments (currently unused; ``None``)."""
    _kind: PTH.Any
    """Raw kind value as supplied to ``__init__``."""
    events: list[PTH.Any]
    """List of :class:`CC_B_P_EventID` objects."""

    def __init__(
        self,
        name: str,
        parameters: PTH.Any = ...,
        inherit_from: PTH.Any = ...,
        base_arguments: PTH.Any = ...,
        kind: PTH.Optional[PTH.Union[CC_ProtocolKind, int]] = ...,
        events: list[PTH.Any] = ...,
    ) -> None: ...

    @property
    def length(self) -> int:
        """Number of events in this protocol."""
        ...

    @property
    def kind(self) -> int:
        """Protocol kind as integer (via :meth:`CC_ProtocolKind.to_number`)."""
        ...

    @property
    def kind_name(self) -> str:
        """Protocol kind as human-readable string."""
        ...
