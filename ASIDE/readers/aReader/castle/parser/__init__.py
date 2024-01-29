"""The  PEG :py:mod:`castle.readers.parser` module is based on Arpeggio

.. seealso::

   * **PEG** *(Parsing Expression Grammar*) https://en.wikipedia.org/wiki/Parsing_expression_grammar
   * **Arpeggio** https://textx.github.io/Arpeggio

"""

import logging; logger = logging.getLogger(__name__)

from typing import Callable

import arpeggio
from castle.readers.general.file import BaseReader


class FileParser(BaseReader):
    """A FileParser reads input-files and parse them using a PEG-parser.

    The ("programming") language --in which the input-files are written-- is defined once, by language- and (optionally)
    comment-definitions (using a PEG). Also a ``visitor`` (a class) has to be specified; which translate the parse-tree
    into an AST.  Then no ``comment_def`` is given, it is assumed either no comments are expected, or the
    ``language_def`` will handle it.

    After the language is defined, multiple (unrelated) files can be read/parsed -- each one is translated into an AST.

    Note: the language/comment-definitions and visitor-class should defined using *Arpeggio*.

    Also, a :py:class:`visitor` (class) should be specified. (this can only be done once).
    When creating a class the search-path `read_dirs` (to look for file-to-be-parsed) can be set.

    """

    def __init__(self, *, language_def=None, comment_def=None, visitor:Callable=None,
                 read_dirs: list[str]=[],
                 **kwargs):
        super().__init__(read_dirs=read_dirs, **kwargs)
        if language_def is None:
            raise ValueError("The `language_def` is a mandatory parameter") # pragma: no mutate
        # comment_def is allowed to be None
        if visitor is None:
            raise ValueError("visitor is a mandatory parameter")

        self._parser = arpeggio.ParserPython(language_def=language_def, comment_def=comment_def)
        self._visitor = visitor


    def parse(self,  filename:str, *, language_def=None, comment_def=None):
        """Read & Parse a file"""
        txt = self._read(filename)
        ast = self._do_parse(txt)
        return ast


    def _do_parse(self, txt):
        pt = self._parser.parse(txt)
        logger.info(f"Reader:_do_parse::\t parse_tree: start={pt.position} end={pt.position_end}; len(txt)={len(txt)}")

        ast = arpeggio.visit_parse_tree(pt, self._visitor)
        logger.debug(f"Reader:_do_parse::\t ast: start={ast.position} end={ast.position_end} -- not counting comments.")

        return ast


