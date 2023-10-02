# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import filecmp

import pytest

from TestDoubles.AIGR.protocols import Sieve

from . import T_Protocol, TstDoubles


def test_01_StartSieve(T_Protocol):
    td = TstDoubles('protocols/StartSieve')
    out = T_Protocol.render(protocols=[Sieve.StartSieve,])
    with  open(td.gen_file, 'w') as f:
        f.write(out)
    assert filecmp.cmp(td.gen_file, td.ref_file), f"The generated file ({td.gen_file}) and the reference ({td.ref_file}) are not the same"


def test_03_SlowStart(T_Protocol):
    td = TstDoubles('protocols/SlowStart')
    out = T_Protocol.render(protocols=[Sieve.SlowStart,])
    with  open(td.gen_file, 'w') as f:
        f.write(out)
    assert filecmp.cmp(td.gen_file, td.ref_file), f"The generated file ({td.gen_file}) and the reference ({td.ref_file}) are not the same"



@pytest.mark.skip("After SlowStart")
def test_03_SimpleSieve(T_Protocol):
        assert False

