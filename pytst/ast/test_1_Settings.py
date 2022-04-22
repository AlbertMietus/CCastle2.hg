import pytest


from castle.ast.grammar import Setting

def test_a_ID():
    a_name, a_val = 'aName', 42
    s=Setting(name=a_name, value=a_val)
    assert s.name  == a_name, "Remember the ID"
    assert s.value == a_val,  "Remember the value"


def test_needID():
    with pytest.raises(ValueError):
        Setting(name=42, value="the name should be an ID, or string")
    with pytest.raises(ValueError):
        Setting(name='a b', value="a space in not allowed in an ID")

def test_needID():
    with pytest.raises(TypeError):
        Setting(name='Forgot_a_Value')

