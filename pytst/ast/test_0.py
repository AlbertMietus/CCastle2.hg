import pytest

from castle.ast import peg

def test_abstracts_1():
    base = peg.PEG()
    term = peg.Terminal()
    nt   = peg.NonTerminal()
    mark = peg.Markers()

def test_abstracts_2():
    assert isinstance(peg.Expression(), peg.NonTerminal)
    assert isinstance(peg.Quantity(), peg.Expression)
    assert isinstance(peg.Predicate(), peg.Expression)

def test_eof():
    assert isinstance(peg.EOF(), peg.Markers)

def test_pred():
    assert isinstance(peg.AndPredicate(), peg.Predicate)
    assert isinstance(peg.NotPredicate(), peg.Predicate)

def test_manys():
    assert isinstance(peg.Optional(), peg.Quantity)
    assert isinstance(peg.OneOrMore(), peg.Quantity)
    assert isinstance(peg.ZeroOrMore(), peg.Quantity)
