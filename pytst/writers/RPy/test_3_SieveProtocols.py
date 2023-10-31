# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Verify the SieveProtocols are correctly 'generated' with the RPy backend.

   - It used/reads a (manually crafted) AIGR, see  ``.../TestDoubles/AIGR/``,
   - the output is rendered, using a (jinja) Template (T_Protocol)
   - and compared to a reference-file ``.../TestDoubles/reference/`` - same of not
   - optionally, the output is aslo written to file (``.../TestDoubles/_generated/``),
     to diff line-by-line (for debugging)
"""

import logging; logger = logging.getLogger(__name__)

import pytest
from TestDoubles.AIGR import sieve
from . import TstDoubles, generatedProtocol_verifier
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)
from . import T_Protocol



def test_01_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.StartSieve, td=TstDoubles('protocols/StartSieve'), strip_remarker=True)

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SlowStart, td=TstDoubles('protocols/SlowStart'), strip_remarker=True)

if False: # SlowStart1 and SimpleSieve are in the same NS, so in the same file
    def test_03_SlowStart1(generatedProtocol_verifier):
        generatedProtocol_verifier(aigr_mock=sieve.SlowStart_1, td=TstDoubles('protocols/SlowStart_1'), strip_remarker=True)

    def test_04_SimpleSieve(generatedProtocol_verifier):
        generatedProtocol_verifier(aigr_mock=sieve.SimpleSieve, td=TstDoubles('protocols/SimpleSieve'), strip_remarker=True)

@pytest.mark.skip("ToDo: Merge")
def test_03_SimpleSieve_withGeneric(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=(sieve.SlowStart_1, sieve.SimpleSieve), td=TstDoubles('protocols/SimpleSieve'), strip_remarker=True)

    assert False, "Not yet done"
