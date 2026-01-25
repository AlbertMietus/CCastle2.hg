# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *


def test_1_aName_as_ID_is_aName(castle_parser):
    txt="aName"
    name = castle_parser(txt, start='ID')
    logger.debug(f"{txt=} ==> {name=} -- {type(name)=}")

    assert isinstance(name, str)
    assert name == txt


def test_2_shortName_as_qualRef_is_IDlist(castle_parser):
    txt="shortName"
    IDlist = castle_parser(txt, start='qualRef')
    logger.debug(f"{txt=} ==> {IDlist=}")

    verify_ID_list(IDlist, txt.split('.'))


def test_3a_dottedName_as_qualRef_is_IDlist(castle_parser):
    txt="dotted.name"
    IDlist = castle_parser(txt, start='qualRef')
    logger.debug(f"{txt=} ==> {IDlist=}")
    verify_ID_list(IDlist, txt.split('.'))

def test_3b_dottedName_as_qualRef_is_IDlist(castle_parser):
    txt="self.name"
    IDlist = castle_parser(txt, start='qualRef')
    logger.debug(f"{txt=} ==> {IDlist=}")
    verify_ID_list(IDlist, txt.split('.'))

def test_3c_selfDotted_as_qualRef_is_IDlist(castle_parser):
    txt=".name"
    IDlist = castle_parser(txt, start='qualRef')
    logger.debug(f"{txt=} ==> {IDlist=} -- {type(IDlist)=}")
    verify_ID_list(IDlist, "self.name".split('.'))




def verify_ID_list(IDlist, names):
    assert isinstance(IDlist, list),       f"Expecting a list, got: {type(IDlist)=} :: {IDlist}"
    assert len(IDlist) is len(names),      f"Not the same number of IDs/names: {IDlist} {names}"
    for i, name in enumerate(IDlist):
        assert isinstance(name, aigr.ID),  f"part {i} is not an ID: {name}"
        assert name == names[i],           f"part {i} is wrong name {name=} != {names[i]=} -- {names}"
