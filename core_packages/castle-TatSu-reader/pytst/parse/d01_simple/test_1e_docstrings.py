# (C) Albert Mietus, 2026; Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1a_DocString_1line(castle_parser):
    txt='"""DocMe :-)"""'
    got = castle_parser(txt, start='docstring')
    logger.debug(f"{txt=} ==> {got=}")
    assert isinstance(got, aigr.fString) and got.value == txt[3:-3]

def test_1b_DocString_1line_variants(castle_parser):
    for txt in (
        '"""DocMe :-)"""',
        "'''DocMe :-)'''",
          '"DocMe :-)"',
          "'DocMe :-)'" ):
        got = castle_parser(txt, start='docstring')
        logger.debug(f"{txt=} ==> {got=}")
        assert isinstance(got, aigr.fString) and got.value == 'DocMe :-)'

def test_2a_DocString_MultiLine(castle_parser):
    txt='"""\nDocMe\n :-)\n"""'
    got = castle_parser(txt, start='docstring')
    logger.debug(f"{txt=} ==> {got=}")
    assert isinstance(got, aigr.fString) and got.value == txt[3:-3]

def test_2b_DocString_MultiLine_variants(castle_parser):
    doc="""\
    More
    Docs
    """
    TD, TS = '"""', "'''"
    for txt in (
            TD + doc + TD,
            TS + doc + TS):
        got = castle_parser(txt, start='docstring')
        logger.debug(f"{txt=} ==> {got=}")   #XXX debug
        assert isinstance(got, aigr.fString) and got.value == doc


#Note: Testing docstrings 'in' the language is tested in those feature -- when the AIGR can handle them

#def test_XXX_DocComponent(castle_parser): pass
#def test_XXX_DocImplement(castle_parser): pass
#def test_XXX_DocProtocol(castle_parser): pass
