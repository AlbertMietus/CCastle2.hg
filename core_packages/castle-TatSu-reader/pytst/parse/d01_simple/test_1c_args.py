# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1_argumentTuple_1Name(castle_parser):
    txt="(Main)"
    args= castle_parser(txt, start='argumentTuple')
    logger.debug(f"{txt=} ==> {args=}")

    assert isinstance(args, list)
    assert len(args) == 1

    arg = args[0]
    assert isinstance(arg, aigr.Argument)
    assert arg.name is None
    assert isinstance(arg.value, aigr.Constant)
    assert arg.value.value == 'Main'

