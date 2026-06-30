# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.files``.
# Hand-maintained companion to files.py.

import typing as PTH
from ...aigr import FileNS, ScaffolderFileNS

logger: PTH.Any


class Files:
    """TatSu semantic-action mixin for top-level Castle file rules.

    Mixed into :class:`~..castle_actions.CastleActions`; handles the
    ``castle_file`` (and ``moat_file`` via ``_old``) grammar rules.
    Collects all top-level definitions (protocols, components, ...) into a
    temporary :class:`~castle.readers.ladon.aigr.FileNS` that the loader
    later converts to a :class:`~castle.aigr.Source_NS`.
    """

    def castle_file(self, ast: PTH.Any) -> FileNS:
        """Reduce ``castle_file``: return a :class:`~...aigr.FileNS` with all top-level nodes.

        Dispatches to ``_old`` for the legacy sequence-style AST; the
        dict-style AST path is a TODO and currently raises ``AssertionError``.
        """
        ...

    def _old(self, seq: PTH.Any) -> FileNS:
        """Handle the legacy sequence-style TatSu AST for a Castle file."""
        ...
