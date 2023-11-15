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
    generatedProtocol_verifier(aigr_mocks=sieve.StartSieve, td=TstDoubles('protocols/start_sieve'), strip_remarker=True)

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mocks=sieve.SlowStart, td=TstDoubles('protocols/slow_start'), strip_remarker=True)

@pytest.mark.xfail(reason="ToDo BUSY")
def test_03_SimpleSieve_withGeneric(generatedProtocol_verifier):
    """``SimpleSieve`` depend on the instantiated generic ``SlowStart_1``.
        They are in the same namespace and (so) need to be rendered in the same file.
        And so, tested together!"""
    generatedProtocol_verifier(aigr_mocks=(sieve.SlowStart_1, sieve.SimpleSieve),
                                   td=TstDoubles('protocols/simple_sieve'), strip_remarker=True)

