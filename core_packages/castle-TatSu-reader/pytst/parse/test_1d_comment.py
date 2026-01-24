# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_0_NoComment(castle_parser):
    txt="just_a_test"
    got = castle_parser(txt, start='nameID')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.ID) and got == 'just_a_test'

def test_1a_endlineComment(castle_parser):
    txt="just_a_test // this is a comment"
    got = castle_parser(txt, start='nameID')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.ID) and got == 'just_a_test'

def test_1b_someLineComments(castle_parser):
    txt="""\
// LEADING COMMENT:: will work when `@@eol_comments` & `@@comments` is set (correctly)
    just_a_test // this becomes a nameID
// ANOTHER COMMENT
"""
    got = castle_parser(txt, start='nameID')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.ID) and got == 'just_a_test'

def test_2_pythonStyleComment(castle_parser):
    txt="""\
#LEADING COMMENT:: will work when `@@eol_comments` & `@@comments` is set (correctly)
    just_a_test # this becomes a nameID
#ANOTHER COMMENT"""
    got = castle_parser(txt, start='nameID')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.ID) and got == 'just_a_test'

def test_3_multiLineComment(castle_parser):
    txt="""\
/*One line */
just_a_test /* this becomes a nameID */
/*
  A long
  comment
*/  
"""
    got = castle_parser(txt, start='nameID')
    logger.info(f"{txt=} ==> {got=}")   #XXX debug
    assert isinstance(got, aigr.ID) and got == 'just_a_test'
