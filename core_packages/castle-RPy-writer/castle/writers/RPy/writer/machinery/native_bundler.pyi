# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.writer.machinery.native_bundler``.
#
# Oddities reported:
# - OLD_XXXX_pack is dead code (name prefix), not stubbed.
# - unpack raises AssertionError (WIP), stubbed faithfully.

import typing as PTH
from castle import aigr
from castle.aigr import types as CCTypes
from castle.writers.RPy.aid import TextBlock
from ._bundler import Bundler, GeneratedCode, TypeTag
from ..portray import PortrayType

class NativeBundler(Bundler):
    """Concrete argument bundler using the native ``[args], {}`` convention.

    This is the only currently active :class:`Bundler` implementation.
    ``Bundler.__new__`` always returns a ``NativeBundler``.

    Calling convention
    ------------------
    * :meth:`box` wraps a value: ``CC_B_int(expr)`` (type determined by
      ``PortrayType``).
    * :meth:`pack` produces ``[CC_B_int(v1), CC_B_str(v2)], {}``  -- a list of
      boxed args plus an empty keyword dict.
    * :meth:`unpack` -- **WIP**, raises ``AssertionError``.
    * :meth:`unbox` extracts the value: ``parm.value``.
    """

    portray: PortrayType
    """Used to produce the correct ``CC_B_<type>`` wrapper name for :meth:`box`."""

    def __init__(self) -> None: ...

    def box(self, argument: GeneratedCode, cc_type: CCTypes._types) -> TypeTag:
        """Return ``'<CC_B_type>(<argument>)'``."""
        ...

    def pack(
        self,
        arguments: PTH.Sequence[TypeTag],
        formal_parameters: aigr.OptionalTypedParameterList,
    ) -> TextBlock:
        """Return ``'[arg1, arg2, ...], {}'`` (list + empty dict string)."""
        ...

    def unpack(
        self,
        parameters: GeneratedCode,
        formal_parameters: aigr.OptionalTypedParameterList,
    ) -> TextBlock:
        """Unpack packed parameters in the callee.  WIP -- raises ``AssertionError``."""
        ...

    def unbox(self, parm: str) -> GeneratedCode:
        """Return ``'<parm>.value'``."""
        ...
