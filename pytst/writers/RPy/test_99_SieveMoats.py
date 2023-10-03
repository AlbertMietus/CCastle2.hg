# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import filecmp

import pytest

from TestDoubles.AIGR.protocols import Sieve

from . import T_Protocol, TstDoubles
from castle.writers import RPy


@pytest.fixture
def generatedProtocol_verifier():
    def file_matcher(aigr_dummy, td):
        template = RPy.Template("protocol.jinja2")
        out = template.render(protocols=(aigr_dummy,))
        with  open(td.gen_file, 'w') as f:
            f.write(out)
        assert filecmp.cmp(td.gen_file, td.ref_file), f"The generated file ({td.gen_file}) and the reference ({td.ref_file}) are not the same"
    return file_matcher


def test_01_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_dummy=Sieve.StartSieve, td=TstDoubles('protocols/StartSieve'))

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_dummy=Sieve.SlowStart, td=TstDoubles('protocols/SlowStart'))



@pytest.mark.skip("After SlowStart")
def test_03_SimpleSieve(T_Protocol):
        assert False

