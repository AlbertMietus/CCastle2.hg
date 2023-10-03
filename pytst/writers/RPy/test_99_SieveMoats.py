# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import filecmp

import pytest

from TestDoubles.AIGR.protocols import Sieve

from . import T_Protocol, TstDoubles
from castle.writers import RPy


@pytest.fixture
def generatedProtocol_verifier():
     def matcher(aigr_mock, td):
        template = RPy.Template("protocol.jinja2")
        out = template.render(protocols=(aigr_mock,))
        ref = open(td.ref_file).read()
        assert out == ref
     return matcher


def test_01_StartSieve(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=Sieve.StartSieve, td=TstDoubles('protocols/StartSieve'))

def test_02_SlowStart(generatedProtocol_verifier):
    generatedProtocol_verifier(aigr_mock=Sieve.SlowStart, td=TstDoubles('protocols/SlowStart'))



@pytest.mark.skip("After SlowStart")
def test_03_SimpleSieve(generatedProtocol_verifier):
        assert False

