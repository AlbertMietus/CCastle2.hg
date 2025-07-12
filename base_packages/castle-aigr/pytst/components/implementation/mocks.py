# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from castle.aigr.components import EventDispatchTable

@pytest.fixture
def mock_protocol():
    return ID("MockProtocol")


@pytest.fixture
def mock_events():
    return [
        ID("MockEvent1"),
        ID("MockEvent2"),
        ID("MockEvent3"),
    ]


@pytest.fixture
def etable(mock_protocol, mock_events):
    map = {event: ID(f"{mock_protocol}_{event}") for event in mock_events}
    return EventDispatchTable(port=ID("MockPortName"), map = map)
