# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from castle.aigr import ProtocolKind


def test_0_Unknow_value():
    assert ProtocolKind.Unknown.value ==0

def test_O_unset_value():
    assert ProtocolKind._unset.value < 0

def test_1_NameExist():
    assert ProtocolKind.Unknown
    assert ProtocolKind.Event
    assert ProtocolKind.Data
    assert ProtocolKind.Stream
