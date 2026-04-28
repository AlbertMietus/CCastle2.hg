# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from pathlib import Path
from enum import Enum

from castle.aigr import ID, Source_NS
from castle.aigr_extra.scaffolding import ScaffolderNameSpace
from ..aigr import FileNS, ScaffolderFileNS

from ..parser import CastleParser


class CastleKind(Enum):
    auto    = None
    Moat    = ".Moat"
    Castle  = ".Castle"
    unknown = NameError


class _BaseLoader():
    def __init__(self, parser=None, kind:CastleKind=CastleKind.auto):
        self.parser = parser if parser else CastleParser()
        self._castleKind = kind
        self._source:PTH.Optional[Path]

    def parse(self, *, _startsymbol=None, **kw) -> Source_NS:
        raise NotImplementedError("Implement in a subclass, using `self._parseStream()`""")

    def _parseStream(self, in_stream:PTH.TextIO, _startsymbol, name=None) -> Source_NS:
        name = ID(name) if name else ID(str(self._source)) # None becomes 'None'
        txt=in_stream.read()
        ast = self.parser.parse(txt, _startsymbol)
        return self._make_Source_NS(ast, name=name)

    def _make_Source_NS(self, ast:FileNS, name:ID):
        src = Source_NS(name, source=self._source)
        wrapped_src = ScaffolderNameSpace(src)
        for e in ScaffolderFileNS(ast):
            wrapped_src.register(e)
        return src


class _FileLoader(_BaseLoader):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._source = None # Will be set in sub-class

    def parse(self, *, name=None, _startsymbol=None, **kw) -> Source_NS:
        assert self._source, f"Can't parse a file that isn't given"
        start_symbol = self._StartSymbol(_startsymbol)

        name = ID(name) if name else ID(self._source.stem)
        with open(self._source) as f:
            return self._parseStream(in_stream=f,_startsymbol=start_symbol, name=name)

    def _StartSymbol(self, _startsymbol:PTH.Optional[str]) ->PTH.Optional[str]:
        """Determnine the parster start symbol, which can be
           - set by the user, via _startsymbol
           - 'castle_file'
           - 'moat_file'
           - None"""

        if PTH.TYPE_CHECKING:
            assert(self._source) # is always checked in parse; but linters do forget ..

        if _startsymbol:
            return _startsymbol
        #else ..

        ## Determnine the CastleKind
        if (self._castleKind is None) or (self._castleKind is CastleKind.auto):
            try:
                kind = CastleKind(self._source.suffix)
            except NameError:
                logger.warning("Unexpected file extention: %s -- %s", self._source.suffix, self._source)
                return None
        else:
            kind = self._castleKind

        ## translate CastleKind to startSymbol (a str, or None)
        if kind == CastleKind.Castle:
            return 'castle_file'
        elif kind == CastleKind.Moat:
            return 'moat_file'
        #else:
        return None

