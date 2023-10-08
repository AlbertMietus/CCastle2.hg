# (C) Albert Mietus, 2023. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from TestDoubles.AIGR import sieve
from . import TstDoubles, generatedProtocol_verifier, generatedMoat_verifier
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)
from . import T_Protocol, T_Moat



def test_01_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.StartSieve, td=TstDoubles('protocols/StartSieve'))

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SlowStart, td=TstDoubles('protocols/SlowStart'))

def test_03_SimpleSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SimpleSieve, td=TstDoubles('protocols/SimpleSieve'))

def test_04_SieveMoat(generatedMoat_verifier):
    generatedMoat_verifier(aigr_mock=sieve.SieveMoat, td=TstDoubles('interfaces/SieveMoat'))

    assert False, "Not Done"

    
