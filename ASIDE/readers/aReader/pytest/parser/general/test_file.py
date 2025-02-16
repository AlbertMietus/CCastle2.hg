import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import FileParser
from castle.readers.parser import grammar


def test_file():
    reader = FileParser(language_def=grammar.peg_grammar,
                        comment_def=grammar.comment,
                        visitor=grammar.PegVisitor(),
                        read_dirs=('../../../demos/ThinOnion',
                                   '../../.././demos/ThinOnion/grammar',
                                   '../../.././pytst/readers/parser'))
    ast = reader.parse('grammar.peg')
    # Remember: ast is a Grammar!!

    #Manuel count ...
    no_rules, no_settings = 20,19
    assert len(ast.parse_rules) == no_rules, f"The number of (real) rules should be {no_rules} -- unless the file is changed"
    assert len(ast.settings) == no_settings, f"The number of settings ('=') should be {no_settings} -- unless the file is changed"

    # XXX See grammar.peg :: comment doesn't works

