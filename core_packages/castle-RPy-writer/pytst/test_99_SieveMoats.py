# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import pytest
from castle.TESTDOUBLES.aigr import sieve

from . import TstDoubles, generatedMoat_verifier, T_Moat
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)

@pytest.mark.skip(reason="To Busy with other things")
def test_04_SieveMoat(generatedMoat_verifier):
    generatedMoat_verifier(aigr_mock=sieve.SieveMoat, td=TstDoubles('interfaces/SieveMoat'))
    assert False, "Not Done"

