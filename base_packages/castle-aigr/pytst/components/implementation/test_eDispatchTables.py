# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Test the EVENT DispatchTables; see `test_DispatchTables.py` for generic tests"""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

### DispatchTable(s): See remark on EventDispatchTable
#from castle.aigr.components import EventDispatchTable

from castle import aigr
from castle.aigr import ID

###from mocks import *


def DEAD_test_1_givenPort_whenEventDispatchTableInit_thenPortIsSet():
    table = EventDispatchTable(_comp=ID('DummyCompName'), _port=ID('MockPortName'))
    assert table._port == "MockPortName",   "Any DispatchTable should be associated with a Port -Found {table._port}"
    assert isinstance(table._port, ID), "The port should be an ID"


def DEAD_test_2a_InitializedWithEventsAndHandlers_TableIsNotEmpty(etable):
    assert len(etable.map) != 0

def DEAD_test_2b_InitializedWithEventsAndHandlers_CountsMatch(etable, mock_events):
    assert len(etable.map) == len(mock_events)


def DEAD_test_3a_InitializedWithEventsAndHandlers_NotNone(etable, mock_events):
    map = etable.map
    for e,h in map.items():
        for name in (e,h):
            assert isinstance(name, ID) and name != "", f"All names in a table should be an ID and never empty. Found: {name}:{type(name)}"





