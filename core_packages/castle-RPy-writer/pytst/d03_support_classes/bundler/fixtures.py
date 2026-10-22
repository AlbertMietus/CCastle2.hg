# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.writer.machinery import Bundler, NativeBundler


@pytest.fixture
def bundler():
    return Bundler()                                                       # type: ignore[reportAbstractUsage, abstract]

