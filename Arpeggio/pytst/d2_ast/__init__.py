import visitor
import arpeggio

def parse(txt, rule):
    parser = arpeggio.ParserPython(rule)
    pt = parser.parse(txt)
    assert pt.position_end == len(txt), f"Did not parse all input txt=>>{txt}<<len={len(txt)} ==> parse_tree: >>{pt}<<_end={pt.position_end}"
    ast = arpeggio.visit_parse_tree(pt, visitor.PegVisitor())
    assert ast.position == 0 and ast.position_end == len(txt), f"Also the AST (type={type(ast)}) should include all input"
    return ast
