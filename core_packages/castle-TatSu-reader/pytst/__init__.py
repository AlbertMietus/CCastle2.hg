# (C) Albert Mietus, 2025, 2026 Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle.readers.parser import CastleParser

@pytest.fixture
def castle_parser():
    parser = CastleParser()
    return parser.parse
