# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

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

