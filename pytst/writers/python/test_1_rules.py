import pytest

from jinja2  import Template

from castle.ast import grammar # To build the ATS



def __test_simple_rule():
    expected	= """def rule_crossref():\treturn ID"""
    castle	= """rule_crossref	<- ID ;"""

    ## Build the AST -- Ignoring the parse_tree
    id_rn = grammar.ID(name="rule_crossref")
    id_xr = grammar.ID(name="ID")

