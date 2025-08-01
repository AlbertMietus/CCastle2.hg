# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from castle.aigr_extra.scaffolding import ScaffolderBody

LEN = 13

@pytest.fixture
def wrapped_body() -> ScaffolderBody:
    b = aigr.Body(statements=[f'fake_{n}' for n in range(LEN)])
    return ScaffolderBody(b)

def test_1_len(wrapped_body):
    assert len(wrapped_body) == LEN

def test_2_items(wrapped_body):
    for n in range(LEN):
        assert 'fake' in wrapped_body[n]
        assert str(n) in wrapped_body[n]

def test_3_expand(wrapped_body):
    fake = 'one_more'
    wrapped_body.expand(fake)
    assert len(wrapped_body) == LEN+1
    assert wrapped_body[-1] == fake
