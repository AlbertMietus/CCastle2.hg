# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.castle_parser``.
# Hand-maintained companion to castle_parser.py.

import typing as PTH
from pathlib import Path

logger: PTH.Any


class CastleParser:
    """TatSu-based parser for the Castle grammar.

    Reads ``castle_grammar.tatsu`` from the same directory as this module,
    compiles it with ``tatsu.parser.TatSuParserGenerator``, and attaches a
    :class:`~.castle_actions.CastleActions` semantics object.  The resulting
    ``tatsu`` grammar object is stored in :attr:`parser`.

    **TatSu version requirement**: this parser requires TatSu ``== 5.17``.
    TatSu 5.18 is known-broken for the Castle grammar (see
    https://github.com/neogeny/TatSu/issues/423).  A version mismatch logs an
    ``ERROR`` but continues, so the error is non-fatal.

    :class:`CastleParser` is normally created automatically by a loader; you
    only construct it directly when you need to reuse the same compiled grammar
    across multiple loads or override the grammar file or actions::

        from castle.readers.ladon.parser.castle_parser import CastleParser

        parser = CastleParser()
        ast    = parser.parse(castle_source_text, start='castle_file')

    The raw *ast* from :meth:`parse` is the return value of the semantic
    actions -- typically a :class:`~castle.readers.ladon.aigr.FileNS`.  Loaders
    consume this to produce a :class:`~castle.aigr.Source_NS`.
    """

    _GRAMMAR_FILE: PTH.ClassVar[str]
    """Filename of the TatSu grammar file (default ``'castle_grammar.tatsu'``)."""

    parser: PTH.Any
    """The compiled ``tatsu.grammars.Grammar`` instance (untyped; TatSu has no stubs)."""

    def __init__(
        self,
        grammar_file: PTH.Optional[Path] = ...,
        actions: PTH.Any = ...,
    ) -> None: ...

    def parse(self, text: str, start: PTH.Optional[str] = ...) -> PTH.Any:
        """Run TatSu on *text* with the optional *start* symbol.

        Returns the raw TatSu parse result after semantic actions have been
        applied -- ordinarily a :class:`~castle.readers.ladon.aigr.FileNS`.
        Pass ``start='castle_file'`` for ``.Castle`` files or
        ``start='moat_file'`` for ``.Moat`` files; ``None`` uses TatSu's
        default start symbol.
        """
        ...
