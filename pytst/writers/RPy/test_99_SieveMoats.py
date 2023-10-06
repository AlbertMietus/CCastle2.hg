# (C) Albert Mietus, 2023. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from TestDoubles.AIGR.protocols import Sieve
from . import TstDoubles, generatedProtocol_verifier, generatedMoat_verifier
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)
from . import T_Protocol, T_Moat

SAVE_FILE=True

def test_01_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=Sieve.StartSieve, td=TstDoubles('protocols/StartSieve'), save_file=SAVE_FILE)

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=Sieve.SlowStart, td=TstDoubles('protocols/SlowStart'), save_file=SAVE_FILE)

def test_03_SimpleSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=Sieve.SimpleSieve, td=TstDoubles('protocols/SimpleSieve'), save_file=SAVE_FILE)

@pytest.mark.fail
def test_04_SieveMoat(generatedMoat_verifier):
    assert False
    
