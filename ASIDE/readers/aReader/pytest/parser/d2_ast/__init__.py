import logging; logger = logging.getLogger(__name__)

import arpeggio

from castle.readers.parser import grammar
from castle.ast import grammar as AST

def parse(txt, rule, *,
          with_comments=False,
          visitor_debug=False):

    parser = arpeggio.ParserPython(rule, comment_def = grammar.comment if with_comments else None)
    pt = parser.parse(txt)
    logger.debug('PARSE_TREE\n'+pt.tree_str())
    assert pt.position_end == len(txt), f"Did not parse all input txt=>>{txt}<<len={len(txt)} ==> parse_tree: >>{pt}<<_end={pt.position_end}"

    ast = arpeggio.visit_parse_tree(pt, grammar.PegVisitor(debug=visitor_debug))
    logger.debug('AST\n' + f'{ast}:{type(ast).__name__}')

    if with_comments: #   When the txt starts with comments, the AST does start 'after' that comment -- so skip the start-check
        assert ast.position_end == len(txt), f"The AST (type={type(ast)}) does not include (start) comments; however typically the end_position ({ast.position_end}) is the end of the text ({len(txt)}"
    else:
        assert ast.position == 0 and ast.position_end == len(txt), f"Without comments, the AST (type={type(ast)}) should include all input: {ast.position}/0 -- {ast.position_end}/{len(txt)}"
    return ast


def assert_ID(id, name:str=None, err_message="Not correct Name"):
    assert name is not None
    assert isinstance(id, AST.ID),		f"The id should be an ID, but is a {type(id)}"
    AST.ID.validate_or_raise(id)                # with correct syntax
    assert id.name == name, err_message if err_message  else f"Note correct name, expected {name}"
precondition_ID = assert_ID                                             # It's not a "validation assert", but a precondition for the test


def assert_Seq(ast, length=None, ids=None):
    assert isinstance(ast, AST.Sequence)
    assert isinstance(ast, AST.Expression),	"A sequence is also an Expression()"
    if length:
        assert len(ast) == length,  		f" ... of specified length=={length}"
    if ids:
        for i, name in enumerate(ids):
            assert_ID(ast[i], name)


def assert_ParseRule(ast, rule_name=None):
    assert isinstance(ast, AST.Rule), 	"It should be an Rule"
    if rule_name:  assert_ID(ast.name, rule_name)

def assert_Rule(ast, rule_name=None):
    assert isinstance(ast, (AST.Rule, AST.Setting))
    if isinstance(ast, AST.Rule): assert_ParseRule(ast, rule_name)
    if isinstance(ast, AST.Setting): assert_Setting(ast, rule_name)

def precondition_Expressions(expr, *, type=AST.Sequence, length=None):
    assert isinstance(expr, type), "PreCondition failed"
    if length:
        assert len(expr)==length, "PreCondition failed"


def assert_PEG(ast, *, no_of_rules=None, no_of_settings=None):
    assert isinstance(ast, AST.Grammar)

    rules = ast.parse_rules
    assert isinstance(rules, AST.Rules)
    if no_of_rules:
        assert len(rules) == no_of_rules, f"The number of (parse_)rules ({len(rules)}) does not match the spec: {no_of_rules}"

    settings = ast.settings
    if settings:
        assert isinstance(settings, AST.Settings)
    if no_of_settings:
        assert len(settings) == no_of_settings, f"The number of settings ({len(settings)}) does not match the spec: {no_of_settings}"


def assert_Setting(ast, grammarType=None, name=None, value=None):
    assert isinstance(ast, AST.Setting)
    assert isinstance(ast.name, AST.ID)
    assert isinstance(ast.value, (AST.StrTerm, AST.RegExpTerm, AST.Number, AST.ID)), f'Unexpected Type for ast.value: {type(ast.value)}'

    if grammarType: assert isinstance(ast.value, grammarType)
    if name:    assert ast.name.name == name
    if value:   assert ast.value.value == value
