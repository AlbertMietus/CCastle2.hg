# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_OutPort``.

import typing as PTH
from .._debug import DebugMixIn

class CC_B_OutPort(DebugMixIn):
    """Runtime representation of a connected output port.

    Holds the remote component reference (:attr:`connection`) and the list of
    event-handler function pointers (:attr:`handlers`).  Both are populated
    at runtime when the component topology is wired together.
    """

    connection: PTH.Any
    """Reference to the connected :class:`CC_B_Component` subclass instance, or ``None``."""
    handlers: list[PTH.Any]
    """List of event-handler callables (dispatch table)."""

    def __init__(self) -> None: ...
