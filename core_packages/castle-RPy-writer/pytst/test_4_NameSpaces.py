# (C) Albert Mietus, 2023. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from castle.TESTDOUBLES.aigr import sieve  # type: ignore 

from . import TstDoubles, generatedProtocol_verifier,  T_Moat
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)

@pytest.mark.skip(reason="ToDo")
def test_0():
    assert False, "Not Done"

