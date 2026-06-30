# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_ComponentInterface``.

import typing as PTH
from .._debug import DebugMixIn

class CC_B_ComponentInterface(DebugMixIn):
    """Describes the *interface* of a Castle component at runtime.

    One ``CC_B_ComponentInterface`` instance is generated per Castle
    ``.Moat`` interface declaration.  It is *static*: created once during
    module initialisation and never mutated after setup.

    Ports are appended after construction via :attr:`ports`.append().

    Usage (in generated code)
    -------------------------
    ::

        cc_CI_MyComp = buildin.CC_B_ComponentInterface(
            name         = "MyComp",
            inherit_from = base.cc_CI_Component,
            ports        = [],
        )
        cc_CI_MyComp.ports.append(...)
    """

    name: str
    """Component-interface name as it appears in the Castle source."""
    inherit_from: PTH.Any
    """Parent :class:`CC_B_ComponentInterface`, or ``None`` for the root."""
    ports: list[PTH.Any]
    """List of :class:`CC_B_C_PortID` objects; populated after construction."""

    def __init__(
        self,
        name: str,
        inherit_from: PTH.Any,
        ports: list[PTH.Any],
    ) -> None: ...

    @property
    def length(self) -> int:
        """Number of ports in this interface."""
        ...
