import pytest
from grammar import *

import arpeggio

R, S, X = regex_term.__name__, str_term.__name__, rule_crossref.__name__  # shortcut in grammar

def parse_sequence(txt, pattern=None):
    parser = ParserPython(sequence, comment)
    tree = parser.parse(txt)

    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[tree.position: tree.position_end]}<<; Not: >>{txt[tree.position_end:]}<<."
    assert isinstance(tree.rule, arpeggio.ZeroOrMore) and tree.rule_name == "sequence"

    if pattern: validate_pattern(tree,pattern=pattern)
    return tree

def validate_pattern(tree, pattern=None):
    assert len(tree) == len(pattern), f"Not correct number-of-element at sublevel={sub}"

    exs=tree.prefix.suffix.expression
    for ex,p in zip(exs, pattern):
        if p is not None:
            if not isinstance(p, (tuple, list)):
                assert ex[0].rule_name == p, f"{ex} doesn't match given {p} sublevel={sub}"
            else:
                validate_pattern(tree=ex[1][0], pattern=p)



def test_simple_1():	parse_sequence(r"abc",		pattern=[X])
def test_simple_2():	parse_sequence(r'A  Bc',	pattern=[X, X])
def test_mix():		parse_sequence(r'/regex/ "string" crossref crossref',	pattern=[R,S, X, X])

def test_sub():		parse_sequence(r'( A  B )',	pattern=[(X, X)])
def test_mix_nosub():	parse_sequence(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, None, X])
def test_mix_sub():	parse_sequence(r'/regex/ "string" ( A  B ) crossref',	pattern=[R,S, (X, X), X])

def test_sub_sub():	parse_sequence(r'level0 ( level1_1  (level2a level2b ) level1_2) level0', pattern=[X, (X, (X,X), X), X])
def test_sub_sub2():	parse_sequence(r'level0 ( level1_1  (level2a level2b ) level1_2) level0', pattern=[X, [X, [X,X], X], X]) 




