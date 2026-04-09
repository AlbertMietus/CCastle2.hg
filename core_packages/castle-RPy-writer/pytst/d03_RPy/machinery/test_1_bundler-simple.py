# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from .fixtures import bundler
from .verify import *

from castle import aigr


def test_1a_pack_single_positional_string(bundler):
    arguments = (aigr.Argument(value=aigr.fString(value="Just a demo")),)
    formal_parameters = (aigr.TypedParameter(name='a', type=aigr.types.string),)
    expected = '[CC_B_string("Just a demo")], {}'

    txt = bundler.pack(arguments=arguments, formal_parameters=formal_parameters)
    verify_ValidPython(txt)

    assert str(txt) == expected, f"Got {txt=}, when packing {arguments=} -- {expected=}"


@pytest.mark.skip(reason="aigr literal int not yet available; intent: pass int value 1")
def test_1b_pack_single_positional_int(bundler):
    arguments = (aigr.Argument(value=1),)                                    # pseudo: replace with aigr.Constant(1) or similar
    formal_parameters = (aigr.TypedParameter(name='a', type=aigr.types.int),)
    txt = bundler.pack(arguments=arguments, formal_parameters=formal_parameters)
    verify_ValidPython(txt)
    assert 'CC_B_int' in str(txt)
