# (C) Albert Mietus, 2023. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from TestDoubles.AIGR import sieve
from . import TstDoubles
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)
from . import T_Protocol, T_Moat


@pytest.mark.skip(reason="ToDo")
def test_0():
    assert False, "Not Done"

