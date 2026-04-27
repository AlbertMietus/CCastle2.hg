# (C) Albert Mietus, 2025, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from pathlib import Path
import tatsu,  tatsu.parser

from .castle_actions import CastleActions

class CastleParser():
    """Castle Parser using TatSu 5.17 -- 5.18 does not work
       See: https://github.com/neogeny/TatSu/issues/423    """

    _GRAMMAR_FILE = 'castle_grammar.tatsu'

    def __init__(self, grammar_file: PTH.Optional[Path]=None, actions=None):
        if grammar_file is None:
            grammar_file = Path(__file__).parent / self._GRAMMAR_FILE
        if actions is None:
            actions = CastleActions()

        grammar_file = grammar_file.resolve()           # make absolute
        grammar_text = grammar_file.read_text(encoding='utf-8')

        gen = tatsu.parser.TatSuParserGenerator('Castle')
        self.parser = gen.parse(grammar_text, filename=str(grammar_file))
        self.parser.semantics = actions

    def parse(self, text: str, start=None):
        return self.parser.parse(text, start=start)


