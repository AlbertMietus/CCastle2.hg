import pytest
from grammar import *

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

show_dot=True

def parse_regex(txt, pattern=None):
    #print(f'\nXXX >>{txt}<<')
    parser = ParserPython(regex_term, comment, debug=show_dot)
    tree = parser.parse(txt)
    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[tree.position: tree.position_end]}<<; Not: >>{txt[tree.position_end:]}<<."

    assert isinstance(tree.rule, arpeggio.OrderedChoice) and tree.rule_name == "regex_term"
    assert len(tree) == 3, "regex_term is an Ordered_Choice of always 3 Terminals"

    for e in tree: assert isinstance(e, arpeggio.Terminal)
    if pattern:
        for e,T in zip(tree,pattern):
            if T is not None: assert isinstance(e.rule, T), f"{type(e.rule).__name__}  doesn't match {T.__name__}"

    return tree

def test_slash_simple():	parse_regex(r"/ABC/",   pattern=[S,RE,S])
def test_slash_slashonly():	parse_regex(r"/\//",    pattern=[S,RE,S])
def test_slash_withslash_r():   parse_regex(r"/ab\/c/", pattern=[S,RE,S])

def test_Rs1_simple():	parse_regex(r"R'ABC'",   pattern=[RE,RE,S])
def test_rs2_simple():	parse_regex(r"r'abc'",   pattern=[RE,RE,S])
def test_Rd1_simple():	parse_regex(r'R"ABC"',   pattern=[RE,RE,S])
def test_rd2_simple():	parse_regex(r'r"abc"',   pattern=[RE,RE,S])

def test_grammar_re_no_slash(): parse_regex(r"/((\\/)|[^\/])*/")
def test_grammar_auto_re_no_slash(): parse_regex("/" + re_no_slash().to_match +"/") # Same as above (unless grammar changes



