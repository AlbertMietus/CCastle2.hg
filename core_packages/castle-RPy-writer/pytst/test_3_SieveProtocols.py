# (C) Albert Mietus, 2023. Part of Castle/CCastle project
"""Verify the SieveProtocols are correctly 'generated' with the RPy backend.

   - It used/reads a (manually crafted) AIGR, see  ``.../TestDoubles/AIGR/``,
   - the variant "basic1" is used -- so:
     * no Generics
     * no SlowStart
   - the output is rendered, using a (jinja) Template (T_Protocol)
   - and compared to a reference-file ``.../TestDoubles/reference/`` - same of not
   - optionally, the output is aslo written to file (``.../TestDoubles/_generated/``),
     to diff line-by-line (for debugging)
"""

import pytest
from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols

from . import TstDoubles, generatedProtocol_verifier, T_Protocol
##Note: T_* are used in **_verifier; but need to be in this scope (or pytest can't find it)




@pytest.mark.skip(reason="no way of currently testing this")
def test_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mocks=protocols.StartSieve, td=TstDoubles('protocols/start_sieve'), strip_remarker=True)

@pytest.mark.skip(reason="no way of currently testing this")
def test_SimpleSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mocks=protocols.StartSieve, td=TstDoubles('protocols/simple_sieve'), strip_remarker=True)

