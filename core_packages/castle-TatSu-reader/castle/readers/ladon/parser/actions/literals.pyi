# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.literals``.
# Hand-maintained companion to literals.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class Literals:
    """TatSu semantic-action mixin for Castle literal-value rules.

    Mixed into :class:`~..castle_actions.CastleActions`; currently handles
    the ``lit_string`` rule only.
    """

    def lit_string(self, ast: PTH.Any) -> aigr.fString:
        """Reduce ``lit_string``: wrap the raw string token in a :class:`~castle.aigr.fString`."""
        ...
