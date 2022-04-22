import pytest

from castle.ast import grammar

def test_abstracts_1():
    base = grammar.PEG()
    term = grammar.Terminal()
    nt   = grammar.NonTerminal()
    mark = grammar.Markers()

def test_abstracts_2():
    assert isinstance(grammar.Expression(), grammar.NonTerminal)
    assert isinstance(grammar.Quantity(), grammar.Expression)
    assert isinstance(grammar.Predicate(), grammar.Expression)

def test_eof():
    assert isinstance(grammar.EOF(), grammar.Markers)

def test_pred():
    assert isinstance(grammar.AndPredicate(), grammar.Predicate)
    assert isinstance(grammar.NotPredicate(), grammar.Predicate)

def test_manys():
    assert isinstance(grammar.Optional(), grammar.Quantity)
    assert isinstance(grammar.OneOrMore(), grammar.Quantity)
    assert isinstance(grammar.ZeroOrMore(), grammar.Quantity)
