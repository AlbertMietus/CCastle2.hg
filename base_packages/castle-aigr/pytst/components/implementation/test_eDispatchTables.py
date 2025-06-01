# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Test the EVENT DispatchTables; see `test_DispatchTables.py` for generic tests"""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle.aigr.components import EventDispatchTable

from castle import aigr
from castle.aigr import ID

@pytest.fixture
def mockHandler(): # More (unused) mocks are in ./mocks.py
    return ID('mockHandler')

@pytest.fixture
def mockTriple(mockHandler):
    return ID('port'), ID('event'), mockHandler

def test_1_startEmpty():
    table = EventDispatchTable()
    assert len(table) == 0, "Initially the table should have 0 events"

def test_2_register_oneEvent_with_IDs(mockHandler):
    p,e = ID('port'), ID('event')
    table = EventDispatchTable()

    table.register_event(p,e, mockHandler)

    assert len(table) == 1, "After one registration, the length should be one"
    assert table.find_byNames(p,e) == mockHandler, "Can't find the just registered event"


def test_3_overwrite_Event(mockHandler):
    p,e = ID('port'), ID('event')
    table = EventDispatchTable()
    table.register_event(p,e, ID('This_one_will_be_overwritten'))

    table.register_event(p,e, mockHandler)

    assert len(table) == 1, "After one registration, the length should be one"
    assert table.find_byNames(p,e) == mockHandler, "Can't find the just registered event"


def test_4a_findNone_asEmpty():
    p,e = ID('port'), ID('event')
    table = EventDispatchTable()

    empty =table.find_byNames(p,e)
    assert empty is None

def test_4b_findNone_asOtherPort(mockHandler):
    p,e = ID('port'), ID('event')
    table = EventDispatchTable()
    table.register_event(p,e, mockHandler)

    empty =table.find_byNames(ID('otherPort'), e)
    assert empty is None

def test_4c_findNone_asOtherEvent(mockHandler):
    p,e = ID('port'), ID('event')
    table = EventDispatchTable()
    table.register_event(p,e, mockHandler)

    empty =table.find_byNames(p,ID('otherEvent'))
    assert empty is None
