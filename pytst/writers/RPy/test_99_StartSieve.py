# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import pytest

from pytst.TestDoubles.protocols import StartSieve   #XXX

from . import T_Protocol

@pytest.mark.xfail
def test_99_StartSieve(T_Protocol):
    out = T_Protocol.render(protocols=[StartSieve,])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert False
