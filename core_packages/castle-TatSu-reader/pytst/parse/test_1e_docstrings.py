# (C) Albert Mietus, 2026; Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1_DocString(castle_parser):
    txt='"""DocMe :-)"""'
    got = castle_parser(txt, start='docstring')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.fString) and got.value == txt[3:-3]
