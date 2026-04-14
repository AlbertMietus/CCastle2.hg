# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from .fixtures import bundler
from .verify import *

from castle import aigr
from castle.aigr import types as CCTypes

@pytest.mark.skip
def test_1_pack_single_positional_demo(bundler):
    arguments = (aigr.Argument(value=aigr.fString(value="Just a demo")),)
    formal_parameters = (aigr.TypedParameter(name='_dummy_', type=aigr.types.string),)
    expected = '[CC_B_string("Just a demo")], {}'
    txt = bundler.pack(arguments=arguments, formal_parameters=formal_parameters)
    logger.debug(f"{arguments=}\n==> {txt=}")
    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"
    verify_ValidPython(txt)

@pytest.mark.skip
def test_2_pack_single_positional_int(bundler):
    arguments = (aigr.Argument(value=aigr.Constant(value=1, type=CCTypes.int)),)
    formal_parameters = (aigr.TypedParameter(name='_dummy', type=CCTypes.int),)
    expected = '[CC_B_int(1)], {}'
    txt = bundler.pack(arguments=arguments, formal_parameters=formal_parameters)
    logger.debug(f"{arguments=}\n==> {txt=}")
    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"
    verify_ValidPython(txt)

