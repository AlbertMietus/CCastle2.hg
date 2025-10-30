# (C) Albert Mietus, 2025, Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from castle.aigr import ID, RefID
from castle import aigr

@pytest.fixture
def name():
    name = ID('name', context=aigr.Def())
    logging.info(f"name \t: {name}, repr: {repr(name)}")
    return name

def test_1_RefID_points_to_alias(name):
    alias1 = RefID('alias1', context=aigr.Ref(reference=name))
    logging.info(f"alias1\t: {alias1}, repr: {repr(alias1)}")

    alias2 = RefID('alias2', context=name)
    logging.info(f"aliass\t: {alias2}, repr: {repr(alias2)}")

    assert alias1.context.reference is alias2.context.reference
    assert alias1.context.reference is name
    assert alias2.context.reference is name

def test_1b_note_alias_os_also_possible_with_plain_ID(name):
    alias3 = ID('alias3', context=aigr.Ref(reference=name)) # Same as above, but using ID
    logging.info(f"alias3\t: {alias3}, repr: {repr(alias3)}")

    #Note: With ID, we must use `Ref()` explicitly

    assert alias3.context.reference is name

@dataclass
class FakeAIGR(aigr.AIGR):
    _ : KW_ONLY
    proto : RefID[aigr.Protocol]

@pytest.fixture
def fakeProtocol():
    return aigr.EventProtocol(name=ID("FakeProtocol"), events=[])

def test_2_(fakeProtocol):
    fake = FakeAIGR(proto=RefID('p1', context=fakeProtocol))
    assert isinstance(fake.proto, ID)
    assert isinstance(fake.proto, RefID)
    assert fake.proto.context.reference is fakeProtocol
    assert isinstance(fake.proto.context.reference, aigr.Protocol)

