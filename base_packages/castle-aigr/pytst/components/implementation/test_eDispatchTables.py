# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Test the EVENT DispatchTables; see `test_DispatchTables.py` for generic tests"""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle.aigr.components import EventDispatchTable

from castle import aigr
from castle.aigr import ID

@pytest.fixture
def mockEvents() -> list[aigr.Event]:
    return [
        aigr.Event("mockEvent_1"),
        aigr.Event("mockEvent_2")]

@pytest.fixture
def mockProtocol(mockEvents) ->aigr.EventProtocol:
    return aigr.EventProtocol("MockProtocol", events=mockEvents)

@pytest.fixture
def mockPort(mockProtocol) ->aigr.Port:
    return aigr.Port("MockPort", direction=aigr.PortDirection.In, type=mockProtocol)


@pytest.fixture
def mockHandler():
    return ID('mockHandler')


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
    


