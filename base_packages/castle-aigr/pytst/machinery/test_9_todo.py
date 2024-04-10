# (C) Albert Mietus, 2024. Part of Castle/CCastle project


import pytest
from castle.aigr import machinery


@pytest.mark.skip("\t sendStream: Other protocol then Event are not planned yet")
def test_sendStream():
    assert False
@pytest.mark.skip("\t sendData: Other protocol then Event are not planned yet")
def test_sendData():
    assert False

@pytest.mark.skip("\t Handlers in eDispatchTable: The Handler AIGR isn't defined")
def test_DispatchTables_Handlers():
    assert False
