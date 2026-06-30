# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.names``.
# Hand-maintained companion to names.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class Names:
    """TatSu semantic-action mixin for Castle name and identifier rules.

    Mixed into :class:`~..castle_actions.CastleActions`; converts raw TatSu
    AST strings for the ``nameID``, ``nameRef``, ``typeID``, ``auto_self``,
    and ``qualRef`` grammar rules into the appropriate ``aigr.ID`` variants.
    """

    def nameID(self, ast: PTH.Any) -> aigr.ID:
        """Reduce ``nameID``: return ``ID.Def(ast)`` -- a *defining* identifier."""
        ...

    def nameRef(self, ast: PTH.Any) -> aigr.ID:
        """Reduce ``nameRef``: return ``ID.Ref(ast, context=None)`` -- an unresolved reference."""
        ...

    def typeID(self, ast: PTH.Any) -> aigr.ID:
        """Reduce ``typeID``: return ``ID.Ref(ast, context='type')`` (context is a HACK placeholder)."""
        ...

    def auto_self(self, ast: PTH.Any) -> aigr.ID:
        """Reduce ``auto_self``: return ``ID.Ref(ast, context='self')`` (context is a HACK placeholder)."""
        ...

    def qualRef(self, ast: PTH.Any) -> list[PTH.Any]:
        """Reduce ``qualRef``: flatten the multi-part reference into a list via :func:`~.support_functions.flat_list`."""
        ...
