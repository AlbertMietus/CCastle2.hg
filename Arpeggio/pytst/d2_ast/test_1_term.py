import pytest

import grammar
import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases


class DemoVisitor(arpeggio.PTNodeVisitor):
    def visit_str_term(self, node, children):
        ast = peg.StrTerm(value=node[1], parse_tree=node)
        return ast


def parse(txt, rule):
    parser = arpeggio.ParserPython(rule)
    pt = parser.parse(txt)
    assert pt.position_end == len(txt), "Did not parse all input"# JTBS
    ast = arpeggio.visit_parse_tree(pt, DemoVisitor())
    return ast

def test_simple_str():
    ast = parse("'a string'", grammar.term)
    assert isinstance(ast, peg.Terminal),	"It should be a term ..."
    assert isinstance(ast, peg.StrTerm), 	"... and a str"
    assert ast.value == "a string", 		"It's correct value should be without quotes"
