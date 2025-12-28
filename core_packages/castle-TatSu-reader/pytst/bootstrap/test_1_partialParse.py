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

def test_2_parameterTuples(castle_parser):
    txt="""(a :t1, b: t2, c : t3)""" # No real types; jyst names
    parms = castle_parser(txt, start='parameterTuple')
    logger.debug(f"test_2_parameterTuples: {parms=}")

    assert isinstance(parms, (tuple,list)) and len(parms) == 3

    for parm, name, type_ in zip(
            parms,
            ('a',  'b',  'c'),
            ('t1', 't2', 't3')):
        assert isinstance(parm.name, aigr.ID) and parm.name == name, f"Expecting {aigr.ID(name)=}, got {parm.name!r}"
        assert parm.type == type_
        assert isinstance(parm.type, aigr.ID)
        assert isinstance(parm.type.context, aigr.base.names.Ref) # Note aigr.base.names.Ref) != aigr.ID.Ref
    #end
