# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from . import *

def test_1a_empty_method(castle_parser):
    txt = """HelloWorld(label :string) {}"""
    method = castle_parser(txt, start='method')
    logger.debug(f"{txt=} ==> {method=}")

    assert isinstance(method, aigr.Method) and  method.name == 'HelloWorld'
    assert len(method.parameters) == 1
    assert method.parameters[0].name == 'label' and method.parameters[0].type == 'string', f"{method.parameters[0]=}"
    assert isinstance(method.body, aigr.Body),  f"{method.body=}"
    assert len(method.body.statements) == 0,    f"{method.body.statements=}"
    assert method.returns is None,              f"{method.returns=}"


def test_1b_method_returns(castle_parser):
    txt = """foo() ->int {}"""
    method = castle_parser(txt, start='method')
    logger.info(f"{txt=} ==> {method=}")   # XXX info->debug

    assert method.returns == 'int',              f"{method.returns=}"
    assert len(method.body.statements) == 0,    f"{method.body.statements=}"

def test_2a_method_1Statements(castle_parser):
    txt = """method() { call(); }"""
    method = castle_parser(txt, start='method')
    logger.info(f"{txt=} ==> {method=}")

    body = method.body
    assert isinstance(body, aigr.Body),  f"{method.body=}"
    verify_VC_statements(body.statements, ["call"])

def test_2a_method_2Statements(castle_parser):
    txt = """method() { call_1() ; call_2(); }"""
    method = castle_parser(txt, start='method')
    logger.info(f"{txt=} ==> {method=}")

    body = method.body
    assert isinstance(body, aigr.Body),  f"{method.body=}"
    verify_VC_statements(body.statements, ['call_1', 'call_2'])



def verify_VC_statements(statements, names):
    assert len(statements) == len(names),           f"{statements=} vs {names=}"
    for stmt, name in zip(statements, names):
        assert isinstance(stmt, aigr.VoidCall),     f"{stmt=}"
        assert isinstance(stmt.call, aigr.Call),    f"Expecting a Call; got:  {stmt.call=}"
        assert isinstance(stmt.call.callable, ID),  f"Expecting a (func) name/ID; got:  {stmt.call.callable=}"
        assert isinstance(stmt.call.callable, ID) and (stmt.call.callable == name), f"stmt.call.callable"
        assert len(stmt.call.arguments) == 0, f"{stmt.call.arguments=}"

