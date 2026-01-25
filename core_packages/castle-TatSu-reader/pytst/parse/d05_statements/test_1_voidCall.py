# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from . import *

def test_99_method_DottedCall(castle_parser):
    txt = """dotted.call()"""
    got = castle_parser(txt, start='statement')
    logger.info(f"{txt=} ==> {got=}")

    assert isinstance(got, aigr.VoidCall) and isinstance(got.call, aigr.Call)
    callable = got.call.callable
    assert isinstance(callable, (tuple, list)) and len(callable) == 2
    assert callable[0] == 'dotted' and callable[1] == 'call'




def verify_VC_statements(statements, names):
    assert len(statements) == len(names),           f"{statements=} vs {names=}"
    for stmt, name in zip(statements, names):
        assert isinstance(stmt, aigr.VoidCall),     f"{stmt=}"
        assert isinstance(stmt.call, aigr.Call),    f"Expecting a Call; got:  {stmt.call=}"
        assert isinstance(stmt.call.callable, ID),  f"Expecting a (func) name/ID; got:  {stmt.call.callable=}"
        assert isinstance(stmt.call.callable, ID) and (stmt.call.callable == name), f"stmt.call.callable"
        assert len(stmt.call.arguments) == 0, f"{stmt.call.arguments=}"

    
