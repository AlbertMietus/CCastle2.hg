# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from . import *

def test_1_VoidCall_NoArgs(castle_parser):
    txt = """GoForIt();"""
    got = castle_parser(txt, start='statement')
    logger.debug(f"{txt=} ==> {got=}")

    verify_VoidCall(got, 'GoForIt')

def test_2_VoidCall_StrArgs(castle_parser):
    txt = """QAZ('foo');"""
    got = castle_parser(txt, start='statement')
    logger.debug(f"{txt=} ==> {got=}")

    verify_VoidCall(got, 'QAZ', args=[
        #Name type
        (None, aigr.fString, "foo")
        ])


def test_3_VoidCall_StrStr(castle_parser):
    txt = """QAZ(p1='foo', p2='bar');"""
    got = castle_parser(txt, start='statement')
    logger.debug(f"{txt=} ==> {got=}")

    verify_VoidCall(got, 'QAZ', args=[
        #Name type
        ('p1', aigr.fString, "foo"),
        ('p2', aigr.fString, "bar"),
        ])


def test_4(castle_parser):
    txt = """print("Hello {label} World");"""
    got = castle_parser(txt, start='statement')
    logger.debug(f"{txt=} ==> {got=}")

    verify_VoidCall(got, 'print', args=[
        #Name type
        (None, aigr.fString, 'Hello {label} World')
        ])


def verify_VoidCall(stmt, name, args=None):
    assert isinstance(stmt, aigr.VoidCall),     f"{stmt=}"
    assert isinstance(stmt.call, aigr.Call),    f"Expecting a Call; got:  {stmt.call=}"
    assert isinstance(stmt.call.callable, ID),  f"Expecting a (func) name/ID; got:  {stmt.call.callable=}"
    assert isinstance(stmt.call.callable, ID) and (stmt.call.callable == name), f"stmt.call.callable"
    if args is not None:
        assert len(stmt.call.arguments) == len(args),  f"Expected {len(args)} arguments, Got {len(stmt.call.arguments)=} -- {stmt.call.arguments}"
        for exp, got in zip(args, stmt.call.arguments):
            assert isinstance(got, aigr.Argument)
            assert got.name  == exp[0]
            assert isinstance(got.value, exp[1])
            if len(exp) >2 : # with (fstring)-value
                assert got.value.value == exp[2]


def test_99_DottedCall(castle_parser):
    txt = """dotted.call();"""
    got = castle_parser(txt, start='statement')
    logger.debug(f"{txt=} ==> {got=}")

    assert isinstance(got, aigr.VoidCall) and isinstance(got.call, aigr.Call)
    callable = got.call.callable
    assert isinstance(callable, (tuple, list)) and len(callable) == 2
    assert callable[0] == 'dotted' and callable[1] == 'call'
