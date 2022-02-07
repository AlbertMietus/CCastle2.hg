import pytest
import logging;logger = logging.getLogger(__name__)

from castle.readers.parser import grammar

import arpeggio

def format_node(n):
    return f"\tNODE:: {n!r}:{type(n)}"

def format_children(l):
    if l is None: return "~~~Forget to pass children~~~"
    if len(l)<1:  return "\tCHILDREN: None"
    return ("\n\tCHILDREN::" + ", ".join(f'>>{c}<<' for c in l))

def show_visited(label="VISIT_", node=None, children=None):
    nl= "\n" if label[-1] != '_' else ""
    logger.info(f'{label}{nl}{format_node(node)}{format_children(children)}')



class DemoVisitor(arpeggio.PTNodeVisitor):
    def visit__default__(self, node, children):
        show_visited('visit__default__', node, children)
        return (node, children)
    def visit_rule(self, node, children):
        show_visited('visit_rule', node, children)
        return (node, children)
    def visit_ordered_choice(self, node, children):
        show_visited('ordered_choice', node, children)
        return (node, children)

    def visit_rule_name(self, node, children):
        show_visited('VISIT_rule_name', node, children)
        return (node, children)
    def visit_rule_crossref(self, node, children):
        show_visited('VISIT_rule_crossref', node, children)
        return (node, children)



def _test_Rule():
    TXT= """RULE_NAME <- EXP1 EXP2 ;"""
    parse_tree = arpeggio.ParserPython(language_def=grammar.rule).parse(TXT)

    print("\nPARSE-TREE\n" + parse_tree.tree_str()+'\n')

    ast = arpeggio.visit_parse_tree(parse_tree, DemoVisitor())
    print("\nAST:\t" + ast)


def QAZ(txt, rule, label=None):
    if label: print(f'\nLABEL: {label}')
    parse_tree = arpeggio.ParserPython(language_def=rule).parse(txt)
    print("PARSE-TREE\n" + parse_tree.tree_str()+'\n')

    ast = arpeggio.visit_parse_tree(parse_tree, DemoVisitor())
    print("AST:\t",  ast)

def test_QAZ_rule_name():    	QAZ("""aName""",	grammar.rule_name,	label="rule_name")
def test_QAZ_rule_crossref():	QAZ("""aName""",	grammar.rule_crossref,	label="rule_crossref")
def test_QAZ_expressions():	QAZ("""aName""",	grammar.expressions,	label="expressions")
