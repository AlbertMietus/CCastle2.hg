# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Generic Tests for  DispatchTables; see `test_eDispatchTables.py` testing event dispatchtables"""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle.aigr.components import dispatch_tables
from castle.aigr import ID


def test_1a_whenInit_CompPortIsSet():
    table = dispatch_tables._DispatchTable(comp=ID('DummyComp'), port=ID("MockPort"))
    assert table.comp == "DummyComp",        f"Any DispatchTable should be associated with a Comp -Found {table.comp}"
    assert table.port == "MockPort",         f"Any DispatchTable should be associated with a Port -Found {table.port}"
    assert isinstance(table.comp, ID),  f"The comp should be an ID; now: type={type(table.comp)}"
    assert isinstance(table.port, ID),       f"The port should be an ID; now: type={type(table.port)}"

def test_1b_InitWithoutPort_willFail():
    try:
        _= dispatch_tables._DispatchTable()
        assert False, "port is essential"
    except TypeError: pass

def test_1c_InitWithoutNamedPortParm_willFail():
    try:
        _= dispatch_tables._DispatchTable(ID("MockPort"))
        assert False, "port is a KW-only parm"
    except TypeError: pass

