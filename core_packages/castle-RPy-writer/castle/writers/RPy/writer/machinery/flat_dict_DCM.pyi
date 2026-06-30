# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery.flat_dict_DCM``.

import typing as PTH
from castle.writers.RPy.aid import Block
from . import Machinery, _M_DC_dict

@Machinery.register(
    "DirectCall.dict.flat", "flat.dict", "flat_dict", "flat-dict",
)
class M_DC_flat_dict(_M_DC_dict):
    """Flat-dictionary Machinery backend.

    A variant of the dict-based dispatch table that does *not* chain to a
    parent.  Currently a stub (inherits all behaviour from :class:`_M_DC_dict`
    without overriding anything).

    Registered hints
    ----------------
    ``"flat-dict"``, ``"flat_dict"``, ``"flat.dict"``,
    ``"DirectCall.dict.flat"``.
    """

    def render_EventDispatchTable(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventOverPort(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
    def render_EventToSub(self, renderer: PTH.Any, node: PTH.Any) -> PTH.Any: ...
