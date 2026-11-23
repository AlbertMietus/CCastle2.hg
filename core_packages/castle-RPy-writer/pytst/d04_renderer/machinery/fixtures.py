# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.writer.machinery import Machinery
from castle.writers.RPy.writer.machinery import Bundler, NativeBundler

@pytest.fixture
def machinery() ->Machinery:
    m = Machinery(hint="chained_dict")                                  # type: ignore[reportAbstractUsage, abstract]
    m.arg_bundler.force_bundling = True                                 #XXX HACK
    logger.info("FORCE_BUNDLING:: m.arg_bundler=%s", m.arg_bundler)
    return m


