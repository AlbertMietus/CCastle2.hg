import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar

import arpeggio

R, S, X = grammar.regex_term.__name__, grammar.str_term.__name__, grammar.rule_crossref.__name__  # shortcut in grammar
P = grammar.predicate.__name__
G = grammar.group.__name__

from . import parse


def validate_expression(txt, pattern):
    parse_tree = parse_expression(txt)
    validate_pattern(parse_tree, pattern=pattern)

def parse_expression(txt):
    parse_tree = parse(txt, grammar.expression)
    assert parse_tree.rule_name == "expression"
    return parse_tree


def validate_pattern(pt, pattern=None):
    elements = pt[0]
    assert len(elements) == len(pattern), f"Not correct number-of-element"

    for p, s in zip(pattern, elements):
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


def test_simple_1():	validate_expression(r"abc",	pattern=[X])
def test_simple_2():	validate_expression(r'A  Bc',	pattern=[X, X])

def test_string_1():	validate_expression(r"'abc'",	pattern=[S])
def test_regexp_1():	validate_expression(r"/re/",	pattern=[R])

def test_mix():		validate_expression(r'/regex/ "string" crossref crossref',	pattern=[R,S, X, X])

def test_sub():		validate_expression(r'( A  B )',	pattern=[(X, X)])
def test_mix_nosub():	validate_expression(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, None, X])
def test_mix_sub():	validate_expression(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, (X, X), X])

def test_sub_sub():	validate_expression(r'level0 ( level1_1  (level2a level2b ) level1_2) level0', pattern=[X, (X, (X,X), X), X])


def test_bug1():	parse_expression(r"""( rule_crossref | term | group | predicate ) ( '?' | '*' | '+' | '#' )?""")
def test_bug1a():	parse_expression(r"""( rule_crossref | term | group | predicate )""")
def test_bug1a1():	parse_expression(r"""A | B | C | D""")
def test_bug1a2():	parse_expression(r"""(A | B | C | D)""")
def test_bug1b():	parse_expression(r"""( rule_crossref | term | group | predicate ) ( '?' | '*' | '+' | '#' )""")
def test_bug1c():	parse_expression(r"""( '?' | '*' | '+' | '#' )""")


