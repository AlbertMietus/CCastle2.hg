import pytest
import logging; logger = logging.getLogger(__name__)

from castle.readers.parser import PEGReader
from castle.readers.parser import grammar, visitor


def test_file():
    reader = PEGReader(read_dirs=('../../../demos/ThinOnion',
                                  '../../.././demos/ThinOnion/grammar',
                                  '../../.././pytst/readers/parser'),
                       language_def=grammar.peg_grammar,
                       comment_def=grammar.comment,
                       visitor=visitor.PegVisitor())
    ast = reader.parse('grammar.peg')
    # Remember: ast is a peg.Grammar!!

    #Manuel count ...
    no_rules, no_settings = 20,19
    assert len(ast.parse_rules) == no_rules, f"The number of (real) rules should be {no_rules} -- unless the file is changed"
    assert len(ast.settings) == no_settings, f"The number of settings ('=') should be {no_settings} -- unless the file is changed"

    # XXX See grammar.peg :: comment doesn't works

