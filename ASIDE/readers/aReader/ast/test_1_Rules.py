import pytest

from castle.ast import grammar


def test_rulename_is_an_ID():
    anID = grammar.ID(name="aName")
    s = grammar.Rule(name=anID, expr=None)
    assert s.name  == anID

def test_rulename_isnot_string():
    with pytest.raises(TypeError):
        grammar.Rule(name="strName", expr=None)


#XXX ToBeDone: more tests


