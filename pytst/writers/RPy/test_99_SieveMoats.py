# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import filecmp

import pytest

from TestDoubles.AIGR.protocols import Sieve

from . import T_Protocol





def test_01_StartSieve(T_Protocol):
    ref_file = 'TestDoubles/reference/protocols/StartSieve.rpy'
    gen_file = 'Testdoubles/_generated/protocols/StartSieve.rpy'

    out = T_Protocol.render(protocols=[Sieve.StartSieve,])
    with  open(gen_file, 'w') as f:
        f.write(out)
    logger.debug(f"Comparing the generated file ({gen_file}) and the reference ({ref_file})")
    assert filecmp.cmp(gen_file, ref_file), f"The generated file ({gen_file}) and the reference ({ref_file}) are not the same"


#@pytest.mark.skip("Need to test AIGR.protocols:: parameters first (and writer for it to)")
def test_03_SlowStart(T_Protocol):
    ref_file = 'TestDoubles/reference/protocols/SlowStart.rpy'
    gen_file = 'Testdoubles/_generated/protocols/SlowStart.rpy'

    out = T_Protocol.render(protocols=[Sieve.SlowStart,])
    with  open(gen_file, 'w') as f:
        f.write(out)
    logger.debug(f"Comparing the generated file ({gen_file}) and the reference ({ref_file})")
    assert filecmp.cmp(gen_file, ref_file), f"The generated file ({gen_file}) and the reference ({ref_file}) are not the same"



@pytest.mark.skip("After SlowStart")
def test_03_SimpleSieve(T_Protocol):
        assert False

