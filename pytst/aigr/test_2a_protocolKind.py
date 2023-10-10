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

def test_2_ConsecutiveSeries():
    values = sorted(k.value for k in ProtocolKind)
    v1 = values[0]
    for v2 in values[1:]:
      assert v1+1==v2, f"{ProtocolKind(v1)}+1 <> {ProtocolKind(v2)}"
      v1=v2
    
    
