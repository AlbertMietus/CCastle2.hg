# (C) Albert Mietus, 2023. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from TestDoubles.AIGR import sieve
from . import TstDoubles, generatedMoat_verifier
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)
from . import T_Protocol, T_Moat

@pytest.mark.xfail(reason="To Busy with other things")
def test_04_SieveMoat(generatedMoat_verifier):
    generatedMoat_verifier(aigr_mock=sieve.SieveMoat, td=TstDoubles('interfaces/SieveMoat'))

    assert False, "Not Done"

