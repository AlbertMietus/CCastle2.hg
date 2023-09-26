# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import pytest

from TestDoubles.AIGR.protocols import Sieve

from . import T_Protocol



ref_file = 'TestDoubles/reference/protocols/StartSieve.rpy'
gen_file = 'Testdoubles/_generated/StartSieve.rpy'

import filecmp

def test_99_StartSieve(T_Protocol):
    out = T_Protocol.render(protocols=[Sieve.StartSieve,])
    with  open(gen_file, 'w') as f:
        f.write(out)
    logger.debug(f"Comparing the generated file ({gen_file}) and the reference ({ref_file})")
    assert filecmp.cmp(gen_file, ref_file), f"The generated file ({gen_file}) and the reference ({ref_file}) are not the same"

