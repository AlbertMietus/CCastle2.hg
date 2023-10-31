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


@pytest.mark.skip("Top one first")
@pytest.mark.xfail(reason="NS support in ``TestDoubles/reference/protocols/*``, not in code")
def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SlowStart, td=TstDoubles('protocols/SlowStart'))

@pytest.mark.skip("Top one first")
@pytest.mark.xfail(reason="NS support in ``TestDoubles/reference/protocols/*``, not in code")
def test_03a_SlowStart1(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SlowStart_1, td=TstDoubles('protocols/SlowStart_1'))

@pytest.mark.skip("Top one first")
@pytest.mark.xfail(reason="NS support in ``TestDoubles/reference/protocols/*``, not in code")
def test_03b_SimpleSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=sieve.SimpleSieve, td=TstDoubles('protocols/SimpleSieve'))


