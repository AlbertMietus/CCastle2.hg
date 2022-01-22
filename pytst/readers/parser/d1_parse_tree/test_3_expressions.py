import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar

import arpeggio

R, S, X = grammar.regex_term.__name__, grammar.str_term.__name__, grammar.rule_crossref.__name__  # shortcut in grammar
P = grammar.predicate.__name__
G = grammar.group.__name__

def parse_expressions(txt, pattern=None):
    parser = arpeggio.ParserPython(grammar.expressions)
    parse_tree = parser.parse(txt)
    logger.info("\nPARSE-TREE\n" + parse_tree.tree_str()+'\n')

    assert parse_tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[parse_tree.position: parse_tree.position_end]}<<; Not: >>{txt[parse_tree.position_end:]}<<."
    assert parse_tree.rule_name == "expressions"

    if pattern: validate_pattern(parse_tree, pattern=pattern)

    return parse_tree

def validate_pattern(pt, pattern=None):
    assert len(pt) == len(pattern), f"Not correct number-of-element"

    for p, s in zip(pattern, pt): # E <- S* (| E)?
        if p is None: continue
        if p == X:
            assert s[0].rule_name == p
        elif p in (S,R):
            assert s[0][0].rule_name == p  # S => T => str/regex
        elif isinstance(p, tuple):         # Group: '(' ... ')'
            assert s[0].rule_name == G
            validate_pattern(s[0][1:-1][0], pattern=p) # G=>E=>
        elif p == P:
            assert False, "To Do: Predicate"
        else:
            assert False, "To Do: More"


def test_simple_1():	parse_expressions(r"abc",	pattern=[X])
def test_simple_2():	parse_expressions(r'A  Bc',	pattern=[X, X])

def test_string_1():	parse_expressions(r"'abc'",	pattern=[S])
def test_regexp_1():	parse_expressions(r"/re/",	pattern=[R])

def test_mix():		parse_expressions(r'/regex/ "string" crossref crossref',	pattern=[R,S, X, X])

def test_sub():		parse_expressions(r'( A  B )',	pattern=[(X, X)])
def test_mix_nosub():	parse_expressions(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, None, X])
def test_mix_sub():	parse_expressions(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, (X, X), X])

def test_sub_sub():	parse_expressions(r'level0 ( level1_1  (level2a level2b ) level1_2) level0', pattern=[X, (X, (X,X), X), X])





