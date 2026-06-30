# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery.list_DCM``.

import typing as PTH
from . import Machinery, _M_DirectCall

@Machinery.register("DirectCall.tuple", "list")
class M_DC_list(_M_DirectCall):
    """List-based DirectCall Machinery backend (registered as ``"list"``).

    Currently a stub; inherits all abstract methods from :class:`_M_DirectCall`
    without providing implementations.

    Registered hints
    ----------------
    ``"list"``, ``"DirectCall.tuple"``.
    """

    def render_EventDispatchTable(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventOverPort(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventToSub(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
