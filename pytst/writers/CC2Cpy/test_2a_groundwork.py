# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
Test the supporting types (Enum, dataclasses ect) for CC_Protocol.

The more relevant test of Protocol can be found in test_2_Protocol.py"""

import pytest

from castle.writers.CC2Cpy.Protocol import *
from castle.writers.CC2Cpy.Protocol import  baseProtocol, CC_RootProtocol ## not public

def test_1_CC_ProtocolKind():
    # Test the (int) value -- needed for the generated C code
    assert CC_ProtocolKind.Unknown.value == 0
    assert CC_ProtocolKind.Event.value   == 1
    assert CC_ProtocolKind.Data.value    == 2
    assert CC_ProtocolKind.Stream.value  == 3

    # Test the long-name & short-name are the same
    assert CC_ProtocolKind.CC_ProtocolKindIs_Unknown == CC_ProtocolKind.Unknown
    assert CC_ProtocolKind.CC_ProtocolKindIs_Event   == CC_ProtocolKind.Event
    assert CC_ProtocolKind.CC_ProtocolKindIs_Data    == CC_ProtocolKind.Data
    assert CC_ProtocolKind.CC_ProtocolKindIs_Stream  == CC_ProtocolKind.Stream


def test_2_typeAliases():
    assert CC_B_Protocol is not None # As long a is exist, it's fine.

def test_3_CC_B_Protocol_NoneBase():
    p1 = CC_RootProtocol('aName', CC_ProtocolKind.Unknown, None)   #Use Root, as CC_Protocol can't be in initiated
    assert p1.name == 'aName'
    assert p1.kind == CC_ProtocolKind.Unknown
    assert p1.based_on is None

def test_3_CC_B_Protocol_baseProtocol():
    p1 = CC_RootProtocol('aName', CC_ProtocolKind.Unknown)
    assert p1.name == 'aName'
    assert p1.kind == CC_ProtocolKind.Unknown
    assert p1.based_on is baseProtocol


import dataclasses

def test_3_dataclasses_are_dataclasses():
    assert dataclasses.is_dataclass(CC_RootProtocol)
    assert dataclasses.is_dataclass(baseProtocol)

