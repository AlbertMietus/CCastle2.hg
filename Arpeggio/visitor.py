import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

class PegVisitor(arpeggio.PTNodeVisitor):
    def visit_str_term(self, node, children):
        ast = peg.StrTerm(value=node[1], parse_tree=node)
        return ast
