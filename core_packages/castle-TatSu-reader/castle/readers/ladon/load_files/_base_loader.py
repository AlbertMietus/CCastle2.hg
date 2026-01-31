# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from pathlib import Path
from enum import Enum

from castle.aigr import ID, Source_NS
from castle.aigr_extra.scaffolding import ScaffolderNameSpace


from ..parser import CastleParser


class FileKind(Enum):
    auto    = None
    Moat    = ".Moat"
    Castle  = ".Castle"
    unknown = NameError

class _FileLoader():
    def __init__(self, parser=None, kind:FileKind=FileKind.auto):
        self.parser = parser if parser else CastleParser()
        self._file:PTH.Optional[Path]=None
        self._fileKind = kind

    def _StartSymbol(self, start:PTH.Optional[str])->str:
        """Determnine the parster start symbol, which can be, pasted (with start), or calculated on rhe file extention.
           - 'castle_file'
           - 'moat_file'
           - None
        """
        if start:
            return start
        #else
        ## Determnine the FileKind
        if (self._fileKind is None) or (self._fileKind is FileKind.auto):
            try:
                kind = FileKind(self._file.suffix)
            except NameError:
                logger.warning("Unexpected file extention: %s -- %s", self._file.suffix, self._file)
                return None
        else:
            kind = self._fileKind

        ## translate FileKind to startSymbol (a str, or None)
        if kind == FileKind.Castle:
            return 'castle_file'
        elif kind == FileKind.Moat:
            return 'moat_file'
        #else:
        return None

    def parse(self, _startsymbol=None) -> Source_NS:
        assert self._file, f"Can't parse a file that isn't given"
        start_symbol = self._StartSymbol(_startsymbol)

        with open(self._file) as f:
            txt=f.read()
            logger.debug("file=%s, start_symbol=%s -- head: %s", self._file, start_symbol, txt[:100])
        ast = self.parser.parse(txt, start_symbol)
        return self._make_Source_NS(ast)

    def _make_Source_NS(self, ast, asName=None):
        logger.info(f"{ast=} {asName=}")   #XXXX 
        name = ID(asName) if asName else ID(self._file.stem)
        src = Source_NS(name, source=self._file)
        wrapped = ScaffolderNameSpace(src)
        for e in ast:
            wrapped.register(e)
        return src


