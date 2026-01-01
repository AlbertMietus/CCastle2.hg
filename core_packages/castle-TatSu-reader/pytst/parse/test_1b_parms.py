# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *


###
### .. note: in "name: type" the "type" is just a name (aigr.ID), not a real type (aigt.type.*)
###
def test_1_parameterTuple_simple(castle_parser):
    txt="(label :string)"
    parms = castle_parser(txt, start='parameterTuple')
    logger.debug(f"{txt=} ==> {parms=}")

    verify_parms_tuple(parms, 1)
    verify_parm(parms[0], 'label', 'string')


def test_2_parameterTuples(castle_parser):
    txt="""(a :t1, b: t2, c : t3)"""
    parms = castle_parser(txt, start='parameterTuple')
    logger.debug(f"{txt=} ==> {parms=}")

    verify_parms_tuple(parms, 3)
    for parm, name, type_ in zip(
            parms,
            ('a',  'b',  'c'),
            ('t1', 't2', 't3')):
            verify_parm(parm, name, type_)


@pytest.mark.skip(reason="optional parameters not yet supported in AIGR")
def test_3_optionalParameter(castle_parser):
    txt="(optional bar :foo)"
    parms = castle_parser(txt, start='parameterTuple')
    logger.debug(f"{txt=} ==> {parms=}")

    verify_parms_tuple(parms, 1)
    verify_parm(parms[0], 'bar', 'foo', check_optional=True) # Will fail ...
    assert False
