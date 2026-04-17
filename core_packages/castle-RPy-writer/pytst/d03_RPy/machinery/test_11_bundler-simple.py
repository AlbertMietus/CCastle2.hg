# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from .fixtures import bundler
from .verify import *

from castle import aigr
from castle.aigr import types as CCTypes


def box_and_pack(bundler, arguments, formal_parameters) ->str:
    boxed: list[str] = []
    for arg, parm in zip(arguments, formal_parameters):
        typ = parm.type
        type_tag: str = bundler.box(arg, typ)
        logger.info(f"bundler.box :: {arg=} + {typ=} ==> {type_tag=}")
        boxed.append(type_tag)
    logger.info(f"{boxed=}")
    return bundler.pack(boxed, formal_parameters)


def test_1_pack_single_positional_int(bundler):
    arguments = ["1"]
    formal_parameters: aigr.OptionalTypedParameterList =(aigr.TypedParameter(name='_dummy', type=CCTypes.int),)
    expected = '[CC_B_int(1)], {}'

    txt=box_and_pack(bundler, arguments, formal_parameters)

    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"
    verify_ValidPython(txt)


def test_2_pack_some_positional_ints(bundler):
    arguments = ["1", "3/2", "42"]
    formal_parameters: aigr.OptionalTypedParameterList = (
        aigr.TypedParameter(name='_dummy', type=CCTypes.int),
        aigr.TypedParameter(name='_dummy', type=CCTypes.int),
        aigr.TypedParameter(name='_dummy', type=CCTypes.int),)
    expected = '[' + (
        'CC_B_int(1), ' +
        'CC_B_int(3/2), ' +
        'CC_B_int(42)' ) + '], {}'

    txt=box_and_pack(bundler, arguments, formal_parameters)

    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"
    verify_ValidPython(txt)
