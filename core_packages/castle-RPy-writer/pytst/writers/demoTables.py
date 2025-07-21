# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr.components import EventDispatchTable

from castle.aigr_extra.blend import mangle_event_handler

from .mocks import *

@pytest.fixture
def simpleTable(mockComp, mockPort, stubProtocol) -> aigr.EventDispatchTable:
    """A simple EventDispatchTable, with no inherited details."""

    map = {event.name: mangle_event_handler(event=event.name, port=mockPort.name, protocol=stubProtocol.name) for event in stubProtocol.events}
    table = EventDispatchTable(comp=mockComp.name, port=mockPort.name, map=map)

    return table

@pytest.fixture
def childTable(mockPort, mockProtocol) -> aigr.EventDispatchTable:
    """An EventDispatchTable, with linked to `simpleTable`"""

    map = {event.name: mangle_event_handler(event=event.name, port=mockPort.name, protocol=mockProtocol.name) for event in mockProtocol.events}
    table = EventDispatchTable(comp=mockComp.name, port=mockPort.name, map=map,) # XXX ToDo Add "parent"

    return table

Expected_4_simpleTable="""\
cc_S_MockComp_MockPort = buildin.machinery.ChainedDict(map={
    MockEvent_1 : an_other__name,
    },
    parent=None)
"""

Expected_4_childTable="""\
cc_S_MockSuper_MockPort = buildin.machinery.ChainedDict(map={
    MockEvent_1 : ...
    },
    parent=cc_S_MockComp_MockPort)
"""
