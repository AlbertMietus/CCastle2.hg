# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

@pytest.mark.skip(reason="This needs more design work first")
def test_999_NoNameCollision():
    assert False, "names will clash"

