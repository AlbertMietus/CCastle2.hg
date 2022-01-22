import pytest

from castle.ast.peg import Rule

@pytest.mark.skip("This test is wrong: (1) An ID is not string, (2) a int is not an Expression")
def test_a_ID():
    a_name, a_val = 'aName', 42
    s=Rule(name=a_name, expr=a_val)
    assert s.name  == a_name, "Remember the ID"
    assert s.expr == a_val,   "Remember the expr"


def test_needID():
    with pytest.raises(ValueError):
        Rule(name=42) # The name should be an ID, or string
    with pytest.raises(ValueError):
        Rule(name='a b') # "A space in not allowed in an ID


