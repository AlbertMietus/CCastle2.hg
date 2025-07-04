# (C) Albert Mietus, 2025. Part of Castle/CCastle project
""" ..seealso:: /../../doc/mocks/writers-mocks.rst"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

@pytest.fixture
def mockEvents() -> list[aigr.Event]:
    return [
        aigr.Event(ID("MockEvent_1")),
        aigr.Event(ID("MockEvent_2")),
        ]

@pytest.fixture
def mockProtocol(mockEvents) ->aigr.EventProtocol:
    return aigr.EventProtocol(ID("MockProtocol"), events=mockEvents)

@pytest.fixture
def mockPort(mockProtocol) ->aigr.Port:
    return aigr.Port("MockPort", direction=aigr.PortDirection.In, type=mockProtocol)

@pytest.fixture
def mockComp(mockPort) ->aigr.ComponentImplementation:
    name=ID("MockComp")
    return aigr.ComponentImplementation(name, interface=aigr.ComponentInterface(name, ports=[mockPort]))

