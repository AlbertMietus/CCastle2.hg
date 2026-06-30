# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.loaders._base_loader``.
# Hand-maintained companion to _base_loader.py.

import typing as PTH
from pathlib import Path
from enum import Enum

from castle.aigr import ID, Source_NS
from ..aigr import FileNS

logger: PTH.Any


class CastleKind(Enum):
    """Maps a Castle source-file kind to the TatSu start symbol.

    The default value ``auto`` infers the kind from the file's suffix:

    * ``.Castle`` -> TatSu start symbol ``'castle_file'``
    * ``.Moat``   -> TatSu start symbol ``'moat_file'``
    * anything else -> ``None`` (TatSu uses its default)

    Pass an explicit ``CastleKind.Castle`` or ``CastleKind.Moat`` to
    :class:`_BaseLoader` to override auto-detection::

        loader = SimpleFileLoader(Path("src.Castle"), kind=CastleKind.Castle)
    """

    auto = None
    Moat = ".Moat"
    Castle = ".Castle"
    unknown = ...   # sentinel: NameError


class _BaseLoader:
    """Abstract base for all Castle source loaders.

    Holds a :class:`~castle.readers.ladon.parser.CastleParser` instance and a
    :class:`CastleKind` hint.  Subclasses supply ``self._source`` (a
    :class:`~pathlib.Path` or equivalent) and override :meth:`parse`, which
    must eventually call :meth:`_parseStream`.

    Do not instantiate directly; use :class:`~.simple_loader.SimpleFileLoader`
    or :class:`~.simple_loader.PyModuleLoader` instead.
    """

    parser: PTH.Any
    """The :class:`~castle.readers.ladon.parser.CastleParser` driving the TatSu parse."""

    _castleKind: CastleKind
    _source: PTH.Optional[Path]

    def __init__(
        self,
        parser: PTH.Any = ...,
        kind: CastleKind = ...,
    ) -> None: ...

    def parse(
        self,
        *,
        _startsymbol: PTH.Optional[str] = ...,
        **kw: PTH.Any,
    ) -> Source_NS:
        """Parse the Castle source and return a populated :class:`~castle.aigr.Source_NS`.

        Subclasses must override this; the base raises :exc:`NotImplementedError`.
        The override should eventually call :meth:`_parseStream`.
        """
        ...

    def _parseStream(
        self,
        in_stream: PTH.TextIO,
        _startsymbol: PTH.Optional[str],
        name: PTH.Optional[str] = ...,
    ) -> Source_NS:
        """Core parse step: read *in_stream*, invoke TatSu, wrap the result.

        Reads the entire stream, calls ``self.parser.parse(text, _startsymbol)``,
        then delegates to :meth:`_make_Source_NS` and returns a
        :class:`~castle.aigr.Source_NS`.  Called by :meth:`_FileLoader.parse`.
        """
        ...

    def _make_Source_NS(self, ast: FileNS, name: ID) -> Source_NS:
        """Convert a :class:`FileNS` AST (from the grammar actions) into a Source_NS.

        Creates a ``Source_NS(name, source=self._source)``, wraps it in a
        ``ScaffolderNameSpace``, iterates over the ``FileNS`` via
        ``ScaffolderFileNS``, registers each node, and returns the plain
        (unwrapped) ``Source_NS``.
        """
        ...


class _FileLoader(_BaseLoader):
    """``_BaseLoader`` specialisation for file-backed Castle sources.

    Manages opening and reading ``self._source`` (a :class:`~pathlib.Path`).
    ``_StartSymbol`` infers the TatSu start symbol from the file's suffix
    unless one is supplied explicitly.

    Subclasses must set ``self._source`` before calling :meth:`parse`.
    """

    def __init__(self, **kw: PTH.Any) -> None: ...

    def parse(
        self,
        *,
        name: PTH.Optional[str] = ...,
        _startsymbol: PTH.Optional[str] = ...,
        **kw: PTH.Any,
    ) -> Source_NS:
        """Open ``self._source``, parse it, and return a :class:`~castle.aigr.Source_NS`.

        *name* overrides the default AIGR node name (which is the file stem).
        *_startsymbol* overrides the start symbol returned by :meth:`_StartSymbol`.
        """
        ...

    def _StartSymbol(self, _startsymbol: PTH.Optional[str]) -> PTH.Optional[str]:
        """Determine the TatSu start symbol for this file.

        Priority order:

        1. *_startsymbol* argument (explicit override).
        2. ``CastleKind.Castle`` -> ``'castle_file'``.
        3. ``CastleKind.Moat``   -> ``'moat_file'``.
        4. Anything else         -> ``None`` (TatSu default).
        """
        ...
