import pytest

## Notice `test_1_Rules.py` and `test_1_Settings.py` are the same, but for the SUT; in the line below -- Keep it that way!!
from castle.peg import Rule as SUT

def test_a_ID():
    a_name, a_val = 'aName', 42
    s=SUT(name=a_name, value=a_val)
    assert s.name  == a_name, "Remember the ID"
    assert s.value == a_val,  "Remember the value"


def test_needID():
    with pytest.raises(ValueError):
        SUT(name=42, value="the name should be an ID, or string")
    with pytest.raises(ValueError):
        SUT(name='a b', value="a space in not allowed in an ID")

def test_needID():
    with pytest.raises(TypeError):
        SUT(name='Forgot_a_Value')

