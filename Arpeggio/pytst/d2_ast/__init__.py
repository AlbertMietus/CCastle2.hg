import visitor
import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

import grammar

def parse(txt, rule,
          print_tree_debug=False,
          visitor_debug=False):
    parser = arpeggio.ParserPython(rule, grammar.comment)
    pt = parser.parse(txt)
    if print_tree_debug:
        print('\n'+pt.tree_str())
    assert pt.position_end == len(txt), f"Did not parse all input txt=>>{txt}<<len={len(txt)} ==> parse_tree: >>{pt}<<_end={pt.position_end}"
    ast = arpeggio.visit_parse_tree(pt, visitor.PegVisitor(debug=visitor_debug))
    assert ast.position == 0 and ast.position_end == len(txt), f"Also the AST (type={type(ast)}) should include all input"
    return ast


def assert_ID(id, name:str=None, err_message="Not correct Name"):
    assert name is not None
    assert isinstance(id, peg.ID),		"The id should be an ID"
    peg.ID.validate_or_raise(id)                # with correct syntax
    assert id.name == name, err_message if err_message  else f"Note correct name, expected {name}"


