# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.readers.parser import CastleParser

@pytest.fixture
def castle_parser():
    parser = CastleParser()
    return parser.parse


def test_1_parameterTuple_simple(castle_parser):
    parms = castle_parser("(label :string)", start='parameterTuple')
    logger.debug(f"test_1_parameterTuple_simple:: {parms=}")

    assert isinstance(parms, (tuple,list)) and len(parms) == 1

    parm = parms[0]
    assert isinstance(parm, aigr.TypedParameter)
    assert parm.name == 'label'
    assert parm.type == 'string' # Note: a *name*; not: aigt.type.string
