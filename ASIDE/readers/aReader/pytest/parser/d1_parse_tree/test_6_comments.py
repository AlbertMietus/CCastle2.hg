import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser.grammar import language as grammar

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

from . import parse

def test_comment_hash():
    parse_tree=parse("""a = b ;# Comment\n""", grammar.peg_grammar)
    logging.debug(f"parse_tree {parse_tree} -- no comments!")
    assert True, "When comments (with hash) are parsed, it's fine"

def test_comment_slash():
    parse_tree=parse("""a = b ;// Comment\n""", grammar.peg_grammar)
    logging.debug(f"parse_tree {parse_tree} -- no comments!")
    assert True, "When comments (with slashed) are parsed, it's fine"

def test_comment_rule():
    #OK rule = r"""comment <- ( '#' | '//' ) /.*\n/ ;"""

    rule = """comment <- ( '#' | '//' ) /.*\\n/ ;"""
    parse_tree = parse(rule, grammar.parse_rule)
