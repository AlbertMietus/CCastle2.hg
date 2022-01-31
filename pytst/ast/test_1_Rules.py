import pytest

from castle.ast import peg


def test_rulename_is_an_ID():
    anID = peg.ID(name="aName")
    s = peg.Rule(name=anID, expr=None)
    assert s.name  == anID

def test_rulename_isnot_string():
    with pytest.raises(TypeError):
        peg.Rule(name="strName", expr=None)


#XXX ToBeDone: more tests


