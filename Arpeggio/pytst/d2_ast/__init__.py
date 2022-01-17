import visitor
import arpeggio

import sys; sys.path.append("./../AST/") ; sys.path.append("./../../AST/")
from castle import peg # has the AST clases

import grammar

def parse(txt, rule, *,
          with_comments=False,
          print_tree_debug=False,
          visitor_debug=False):

    parser = arpeggio.ParserPython(rule, comment_def = grammar.comment if with_comments else None)
    pt = parser.parse(txt)

    if print_tree_debug:
        print('\n'+pt.tree_str())
    assert pt.position_end == len(txt), f"Did not parse all input txt=>>{txt}<<len={len(txt)} ==> parse_tree: >>{pt}<<_end={pt.position_end}"
    ast = arpeggio.visit_parse_tree(pt, visitor.PegVisitor(debug=visitor_debug))
    if with_comments: #   When the txt starts with comments, the AST does start 'after' that comment -- so skip the start-check
        assert ast.position_end == len(txt), f"The AST (type={type(ast)}) does not include (start) comments; however typically the end_position ({ast.position_end}) is the end of the text ({len(txt)}"
    else:
        assert ast.position == 0 and ast.position_end == len(txt), f"Without comments, the AST (type={type(ast)}) should include all input: {ast.position}/0 -- {ast.position_end}/{len(txt)}"
    return ast


def assert_ID(id, name:str=None, err_message="Not correct Name"):
    assert name is not None
    assert isinstance(id, peg.ID),		f"The id should be an ID, but is a {type(id)}"
    peg.ID.validate_or_raise(id)                # with correct syntax
    assert id.name == name, err_message if err_message  else f"Note correct name, expected {name}"
precondition_ID = assert_ID                                             # It's not a "validation assert", but a precondition for the test


def assert_Seq(ast, length=None, ids=None):
    assert isinstance(ast, peg.Sequence)
    assert isinstance(ast, peg.Expression),	"A sequence is aslo an Expression()"
    if length:
        assert len(ast) == length,  		f" ... of specified length=={length}"
    if ids:
        for i, name in enumerate(ids):
            assert_ID(ast[i], name)


def assert_Rule(ast, rune_name=None):
    assert isinstance(ast, peg.Rule), 	"It should be an Rule"
    if rune_name:
        assert_ID(ast.name, rune_name)
precondition_Rule = assert_Rule


def precondition_Expressions(expr, *, type=peg.Sequence, length=None):
    assert isinstance(expr, type), "PreCondition failed"
    if length:
        assert len(expr)==length, "PreCondition failed"


def assert_PEG(ast, *, no_of_rules=None, no_of_settings=None):
    assert isinstance(ast, peg.Grammar)

    rules = ast.rules
    assert isinstance(rules, peg.Rules)
    if no_of_rules:
        assert len(rules) == no_of_rules, "We expect the same number as Rules as lines"

    settings = ast.settings
    assert isinstance(settings, (type(None), peg.Settings))
    if no_of_settings:
        assert isinstance(settings, peg.Settings)
        len(settings) == no_of_settings
