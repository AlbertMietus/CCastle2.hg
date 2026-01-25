# (C) Albert Mietus, 2026; Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1a_DocString_1line(castle_parser):
    txt='"""DocMe :-)"""'
    got = castle_parser(txt, start='docstring')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.fString) and got.value == txt[3:-3]

def test_1b_DocString_1line_variants(castle_parser):
    for txt in (
        '"""DocMe :-)"""',
        "'''DocMe :-)'''",
          '"DocMe :-)"',
          "'DocMe :-)'" ):
        got = castle_parser(txt, start='docstring')
        logger.info(f"{txt=} ==> {got=}")   #XXX debug
        assert isinstance(got, aigr.fString) and got.value == 'DocMe :-)'


