# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.writer.machinery import Bundler, NativeBundler


@pytest.fixture
def a_bundler():
    return Bundler()                                                       # type: ignore[reportAbstractUsage, abstract]

@pytest.fixture
def forceYes_bundler(a_bundler):
    a_bundler.force_bundling = True
    return a_bundler

@pytest.fixture
def forceNo_bundler(a_bundler):
    a_bundler.force_bundling = False
    return a_bundler

@pytest.fixture
def the_bundler(a_bundler):
    return a_bundler
