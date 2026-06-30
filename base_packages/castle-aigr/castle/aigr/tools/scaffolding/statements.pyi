# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.statements``.
# Hand-maintained "manual autodoc" companion to statements.py.

import typing as PTH
from . import ScaffolderNode as ScaffolderNode

logger: PTH.Any

class ScaffolderBody(ScaffolderNode):
    """Scaffolder for a :class:`castle.aigr.statements.Body`.

    Adds list-like access to the wrapped body's statements (``len()`` and
    ``body[i]``) and an :meth:`expand` helper to append statements.
    """

    _nodeCls: type
    _kids_fields: frozenset[str]

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> PTH.Any:
        """Return one statement of the wrapped body."""
        ...
    def expand(self, *s: PTH.Any) -> None:
        """Append one or more statements to the wrapped ``Body``."""
        ...
