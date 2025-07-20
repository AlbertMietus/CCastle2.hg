# (C) Albert Mietus, 2025. Part of Castle/CCastle project
""" ..seealso:: /../../doc/mocks/writers-mocks.rst"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID



@pytest.fixture
def stubProtocol() ->aigr.EventProtocol:
    dummyEvents = [
        aigr.Event(ID("DummyEvent_1")),
        aigr.Event(ID("DummyEvent_2")),
        ]
    return aigr.EventProtocol(ID("StubProtocol"), events=dummyEvents)

@pytest.fixture
def mockPort(stubProtocol) ->aigr.Port:
    return aigr.Port(ID("MockPort"), direction=aigr.PortDirection.In, type=stubProtocol)

@pytest.fixture
def mockComp(mockPort) ->aigr.ComponentImplementation:
    return aigr.ComponentImplementation(name=ID("MockComp"), interface=aigr.ComponentInterface(name, ports=[mockPort]))





