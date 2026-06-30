# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery.tuple_DCM``.

import typing as PTH
from . import Machinery, _M_DirectCall

@Machinery.register("DirectCall.tuple", "tuple")
class M_DC_tuple(_M_DirectCall):
    """Tuple-based DirectCall Machinery backend (registered as ``"tuple"``).

    Currently a stub; inherits all abstract methods from :class:`_M_DirectCall`
    without providing implementations.

    Registered hints
    ----------------
    ``"tuple"``, ``"DirectCall.tuple"``.
    """

    def render_EventDispatchTable(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventOverPort(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventToSub(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
