import pytest
from grammar import *

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

def parse_rule(txt, pattern=None):
    parser = ParserPython(rule, comment)
    tree = parser.parse(txt)
    #print(f'\nTREE\n{tree.tree_str()}')

    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{txt[tree.position: tree.position_end]}<<; Not: >>{txt[tree.position_end:]}<<."
    assert len(tree) == 4, 		      		"A rule should have length=4; ..."
    assert tree[0].rule_name == "rule_name",  		"  at [0], the name of the rule"
    assert str(tree[1]) == '<-',                        "  then a arrow"
    assert tree[2].rule_name == "ordered_choice",	"  at [2] an ordered_choice"
    assert str(tree[3]) == ';',                         "  and the the closing ':'"

    return tree


def test_simple():	parse_rule(r"R <- A  B C ;")
def test_OC():		parse_rule(r"Alts <-  This | That | Or So ;")

def test_rule_rule():	parse_rule(r"""RULE	           <-  RULE_NAME '<-' ORDERED_CHOICE ';' ;""")
def test_expression_rule():	parse_rule(r"""
   expression	   <- regex_term
   		   |  rule_crossref
		   |  '(' ordered_choice ')'
		   |  str_term
		   ;""")

