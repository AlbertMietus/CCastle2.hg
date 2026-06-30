# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.body``.
# Hand-maintained companion to body.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class Body:
    """TatSu semantic-action mixin for Castle statement-body rules.

    Mixed into :class:`~..castle_actions.CastleActions`; handles the
    ``body`` and ``stat_voidcall`` grammar rules.  Each method receives
    the raw TatSu ``ast`` (dict-like or list) and returns the matching
    AIGR node.
    """

    def body(self, ast: PTH.Any) -> aigr.Body:
        """Reduce the ``body`` rule: return a :class:`~castle.aigr.Body` from the statement list.

        Handles the edge case where TatSu returns something other than a
        ``list`` (e.g. an empty match) by substituting ``[]``.
        """
        ...

    def stat_voidcall(self, ast: PTH.Any) -> aigr.VoidCall:
        """Reduce the ``stat_voidcall`` rule: wrap a :class:`~castle.aigr.Call` in a VoidCall."""
        ...
