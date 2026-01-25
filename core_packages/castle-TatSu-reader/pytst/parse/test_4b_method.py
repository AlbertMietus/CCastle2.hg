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
    txt = """method() { ToDo; }"""
    method = castle_parser(txt, start='method')
    logger.info(f"{txt=} ==> {method=}")

    body = method.body
    assert isinstance(body, aigr.Body),  f"{method.body=}"
    assert len(body.statements) == 1,    f"{body.statements=}"

def test_2a_method_2Statements(castle_parser):
    txt = """method() { XXX; ToDo; }"""
    method = castle_parser(txt, start='method')
    logger.info(f"{txt=} ==> {method=}")

    body = method.body
    assert isinstance(body, aigr.Body),  f"{method.body=}"
    assert len(body.statements) == 2,    f"{body.statements=}"
