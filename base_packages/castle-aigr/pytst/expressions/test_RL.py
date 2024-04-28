# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest

@pytest.mark.skip("ToDo")
def test_0():
    assert False

@pytest.mark.skip("ToDo: Power")
def test_Power():
    left, right = 1234,5678
    verify_binOp(builders.Power(left, right), left, '**', right)
