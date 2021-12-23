import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

class PegVisitor(arpeggio.PTNodeVisitor):

    def visit_str_term(self, node, children):
        ast = peg.StrTerm(value=node[1], parse_tree=node)
        return ast
    def visit_regex_term(self, node, children):
        ast = peg.RegExpTerm(value=node[1], parse_tree=node)
        return ast

    def visit_rule_name(self, node, children):
        ast = peg.ID(name=str(node), parse_tree=node)
        return ast
    def visit_rule_crossref(self, node, children):
        ast = peg.ID(name=str(node), parse_tree=node)
        return ast

    def visit_single_expr(self, node, children):                        #  [ rule_crossref, term, group, predicate ] Optional([ '?' , '*' , '+' , '#' ]))
        if len(children) == 1: # No optional part
            ast = peg.Sequence(value=children, parse_tree=node)
        else:
            assert NotImplementedError("To Do: visit_single_expr with optional part")  # XXX
        return ast

    def visit_rule(self, node, children):                               #  Name '<-' expressions ';'
        ast = peg.Rule(name=children[0],expr=children[1], parse_tree=node)
        return ast
