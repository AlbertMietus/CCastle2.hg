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
    verify_Body(method.body, statements=0)


def test_1b_method_returns(castle_parser):
    txt = """foo() ->int {}"""
    method = castle_parser(txt, start='method')
    logger.debug(f"{txt=} ==> {method=}")

    assert method.returns == 'int',              f"{method.returns=}"
    assert len(method.body.statements) == 0,     f"{method.body.statements=}"
    verify_Body(method.body, statements=0)

def test_2a_method_1Statements(castle_parser):
    txt = """method() { call(); }"""
    method = castle_parser(txt, start='method')
    logger.debug(f"{txt=} ==> {method=}")
    verify_Body(method.body, statements=1)


def test_2b_method_2Statements(castle_parser):
    txt = """method() { call_1() ; call_2(); }"""
    method = castle_parser(txt, start='method')
    logger.debug(f"{txt=} ==> {method=}")
    verify_Body(method.body, statements=2)



def verify_Body(body, statements=0):
    assert isinstance(body, aigr.Body),          f"Check for Body: {method.body=}"
    assert isinstance(body.statements, list),    f"Check for list: {body.statements=}"
    assert len(body.statements) == statements,   f"check length=={statements}: {body.statements=}"


    from pprint import pformat
    logger.info("XXX: %s", pformat(body))



def test_5a_method_is_localFunc(castle_parser):
    txt = """HelloWorld(label :string) {}"""
    method = castle_parser(txt, start='local_function')
    logger.debug(f"{txt=} ==> {method=}")

    assert isinstance(method, aigr.Method) and  method.name == 'HelloWorld'
    assert len(method.parameters) == 1
    assert method.parameters[0].name == 'label' and method.parameters[0].type == 'string', f"{method.parameters[0]=}"
    verify_Body(method.body, statements=0)

def test_5b_method_is__debug_callable(castle_parser):
    txt = """HelloWorld(label :string) {}"""
    method = castle_parser(txt, start='_debug_callable')
    logger.debug(f"{txt=} ==> {method=}")

    assert isinstance(method, aigr.Method) and  method.name == 'HelloWorld'
    assert len(method.parameters) == 1
    assert method.parameters[0].name == 'label' and method.parameters[0].type == 'string', f"{method.parameters[0]=}"
    verify_Body(method.body, statements=0)
    
