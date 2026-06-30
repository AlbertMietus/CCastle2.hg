# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_C_PortID``.

import typing as PTH
from .enums import CC_PortDirection
from .._debug import DebugMixIn

class CC_B_C_PortID(DebugMixIn):
    """Describes a single port on a :class:`CC_B_ComponentInterface`.

    Created in generated code and appended to
    ``cc_CI_<Name>.ports`` after the interface is constructed.

    Usage (in generated code)
    -------------------------
    ::

        cc_CI_MyComp.ports.append(buildin.CC_B_C_PortID(
            name      = "clk",
            portNo    = -1,
            protocol  = cc_P_Clock,
            direction = buildin.CC_PortDirection.In,
            part_of   = cc_CI_MyComp,
        ))
    """

    name: PTH.Any
    """Port name (string-like)."""
    portNo: PTH.Any
    """Port sequence number (currently unused; always ``-1``)."""
    protocol: PTH.Any
    """The :class:`CC_B_Protocol` this port is typed by."""
    _direction: PTH.Any
    """Raw direction value as supplied to ``__init__``."""
    part_of: PTH.Any
    """The :class:`CC_B_ComponentInterface` this port belongs to."""

    def __init__(
        self,
        name: PTH.Any,
        portNo: PTH.Any,
        protocol: PTH.Any,
        direction: PTH.Union[CC_PortDirection, int],
        part_of: PTH.Any,
    ) -> None: ...

    @property
    def direction(self) -> int:
        """Port direction as integer (via :meth:`CC_PortDirection.to_number`)."""
        ...

    @property
    def direction_name(self) -> str:
        """Port direction as human-readable string."""
        ...
