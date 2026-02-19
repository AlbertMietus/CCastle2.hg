# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)


import typing as PTH                                       # Python TypeHints

from pathlib import Path

import tatsu


from .castle_actions import CastleActions

class CastleParser():
    """ Castle Parser using Tatsu """

    _GRAMMAR_FILE = 'castle_grammar.tatsu'

    def __init__(self, grammar_file :PTH.Optional[Path]=None, actions=None):
        if grammar_file is None:
            grammar_file = Path(__file__).parent / self._GRAMMAR_FILE
        logger.debug("using %s as grammar(file) -- %s", grammar_file, grammar_file.resolve())
        with open(grammar_file) as f:
            grammar = f.read()
        if actions is None:
            actions = CastleActions

        # HACK for TatSu: pasing the absolute file-name is needed for `#include`
        self.parser = tatsu.compile(grammar, semantics=CastleActions(), filename=grammar_file.resolve())

    def parse(self, text: str, start=None):
        return self.parser.parse(text, start=start)

