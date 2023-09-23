# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr.types import TypedParameter

from . import T_Protocol
from . import MockEvent, MockProtocol

@pytest.mark.xfail
def test_99_StartSieve(T_Protocol):
    out = T_Protocol.render(
        protocol=MockProtocol("StartSieve"),
        events=[
            MockEvent("runTo",  indexNo=7, typedParameters=[TypedParameter(name='max', type=int)]),
            MockEvent("newMax", indexNo=8, typedParameters=[TypedParameter(name='max', type=int)]),
            ])
    logger.info("\n---------- out:: ------------------------\n%s\n--------------------------------", out)
    assert False
