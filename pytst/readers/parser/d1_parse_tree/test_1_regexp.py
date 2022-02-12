import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

from . import parse

def verify_regex(txt, pattern=None):
    parse_tree = parse(txt, grammar.regex_term)

    assert isinstance(parse_tree.rule, arpeggio.OrderedChoice) and parse_tree.rule_name == "regex_term"
    assert len(parse_tree) == 3, "regex_term is an Ordered_Choice of always 3 Terminals"
    for e in parse_tree: assert isinstance(e, arpeggio.Terminal)

    if pattern:
        validate_pattern(parse_tree, pattern=pattern)

def validate_pattern(parse_tree, pattern):
        for e,T in zip(parse_tree,pattern):
            if T is not None: assert isinstance(e.rule, T), f"{type(e.rule).__name__}  doesn't match {T.__name__}"



def test_slash_simple():	verify_regex(r"/ABC/",   pattern=[S,RE,S])
def test_slash_slashonly():	verify_regex(r"/\//",    pattern=[S,RE,S])
def test_slash_withslash_r():   verify_regex(r"/ab\/c/", pattern=[S,RE,S])

def test_Rs1_simple():	verify_regex(r"R'ABC'",   pattern=[RE,RE,S])
def test_rs2_simple():	verify_regex(r"r'abc'",   pattern=[RE,RE,S])
def test_Rd1_simple():	verify_regex(r'R"ABC"',   pattern=[RE,RE,S])
def test_rd2_simple():	verify_regex(r'r"abc"',   pattern=[RE,RE,S])

def test_grammar_re_no_slash(): verify_regex(r"/((\\/)|[^\/])*/")
def test_grammar_auto_re_no_slash(): verify_regex("/" + grammar.re_no_slash().to_match +"/") # Same as above (unless grammar changes



