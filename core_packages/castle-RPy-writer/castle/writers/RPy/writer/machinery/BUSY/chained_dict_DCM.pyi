# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery.chained_dict_DCM``.
#
# Oddities reported:
# - render_EventToSub raises NotImplementedError immediately; the dead code
#   below the raise is reference/scaffolding material (see intentional-dead-code.rst).
# - OLD_AND_GONE_render_sendEvent is clearly dead (name prefix), not stubbed.
# - Line 70 has a missing-return mypy error (dead code after raise); line 86
#   references aigr.machinery.sendEvent which does not exist -- both pre-existing.

import typing as PTH
from castle.writers.RPy.aid import Block
from . import Machinery, _M_DC_dict

@Machinery.register(
    "DirectCall.dict.chained", "chained.dict", "chained_dict", "chained-dict",
    default=True,
)
class M_DC_chained_dict(_M_DC_dict):
    """Chained-dictionary Machinery backend (the default).

    Renders event-dispatch tables as :class:`buildin.machinery.ChainedDict`
    instances, supporting inherited handler lookup through a ``parent``
    chain.

    Registered hints
    ----------------
    ``"chained-dict"``, ``"chained_dict"``, ``"chained.dict"``,
    ``"DirectCall.dict.chained"`` -- this is the **default** backend.

    Usage
    -----
    ::

        m = Machinery()           # selects M_DC_chained_dict (default)
        m = Machinery("chained-dict")   # explicit
    """

    def render_EventDispatchTable(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Render a ``buildin.machinery.ChainedDict(map={...}, parent=...)`` literal.

        The table variable is named via
        ``renderer.portray.cc_S_dispatchTable(comp, port)``.
        """
        ...

    def render_EventOverPort(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Not yet implemented -- raises ``NotImplementedError``."""
        ...

    def render_EventToSub(self, renderer: PTH.Any, node: PTH.Any) -> Block:
        """Not yet implemented -- raises ``NotImplementedError`` (WIP).

        The method body below the ``raise`` is reference scaffolding kept for
        the future implementation; see doc/CodeAI-analysis/ToDo/intentional-dead-code.rst.
        """
        ...
