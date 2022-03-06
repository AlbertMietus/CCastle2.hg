"""The  PEG :py:mod:`castle.readers.parser` module is based on Arpeggio

.. seealso::

   * **PEG** *(Parsing Expression Grammar*) https://en.wikipedia.org/wiki/Parsing_expression_grammar
   * **Arpeggio** https://textx.github.io/Arpeggio

"""

import logging; logger = logging.getLogger(__name__)

from typing import Callable

import arpeggio
from castle.readers.general.file import BaseReader


class PEGReader(BaseReader):
    """File-Reader to read & parse files, using a PEG parser.

    When creating a :py:class:`PEGReader` a default value for the `language_def` & `comment_def` can be set (and/or can
    be set when reading a file -- see py:func`parse`). This language_def & comment_def should defined using *Arpeggio*.

    Also, a :py:class:`visitor` (class) should be specified. (this can only be done once).

    When creating a class the search-path `read_dirs` (to look for file-to-be-parsed) can be set.
    """

    def __init__(self, *, read_dirs: list[str]=[],
                 language_def=None, comment_def=None, visitor:Callable=None,
                 **kwargs):
        super().__init__(read_dirs=read_dirs, **kwargs)
        if visitor is None:
            raise ValueError("visitor is a mandatory parameter")
        self._visitor = visitor
        self.default_language_def = language_def
        self.default_comment_def = comment_def


    def parse(self,  filename:str, *, language_def=None, comment_def=None):
        """Read & Parse a file"""
        if not language_def: language_def = self.default_language_def
        if not comment_def: comment_def = self.default_comment_def
        txt = self._read(filename)
        ast = self._do_parse(txt, language_def, comment_def)
        return ast


    def _do_parse(self, txt, language_def, comment_def):
        parser = arpeggio.ParserPython(language_def=language_def, comment_def=comment_def)

        pt = parser.parse(txt)
        logger.info(f"Reader:_do_parse::\t parse_tree: start={pt.position} end={pt.position_end}; len(txt)={len(txt)}")

        ast = arpeggio.visit_parse_tree(pt, self._visitor)
        logger.debug(f"Reader:_do_parse::\t ast: start={ast.position} end={ast.position_end} -- not counting comments.")

        return ast


