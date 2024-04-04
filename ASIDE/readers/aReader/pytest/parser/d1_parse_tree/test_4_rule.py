import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser.grammar import language as grammar

import arpeggio
RE, S = arpeggio.RegExMatch, arpeggio.StrMatch                          # shortcut

from . import parse

def check_rule(txt, pattern=None):
    parse_tree = parse(txt, grammar.parse_rule)
    logger.debug("%s", parse_tree.tree_str())

    assert len(parse_tree) == 4, 		    	"A rule should have length=4; ..."
    assert parse_tree[0].rule_name == "rule_name",  	"  at [0], the name of the rule"
    assert str(parse_tree[1]) == '<-',                  "  then a arrow"
    assert parse_tree[2].rule_name == "expression",	"  at [2] an expression"
    assert str(parse_tree[3]) == ';',                   "  and the the closing ':'"

    return parse_tree


def test_simple():	check_rule(r"R <- A B C ;")
def test_OC():		check_rule(r"Alts <-  This | That | Or So ;")

def test_rule_rule():	check_rule(r"""RULE  <-  RULE_NAME '<-' ORDERED_CHOICE ';' ;""")
def test_expression_rule():	check_rule(r"""
   expression	   <- regex_term
   		   |  rule_crossref
		   |  '(' ordered_choice ')'
		   |  str_term
		   ;""")

