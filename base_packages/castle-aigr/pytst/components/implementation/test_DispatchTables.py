# (C) Albert Mietus, 2025. Part of Castle/CCastle project

""" Generic Tests for  DispatchTables; see `test_eDispatchTables.py` testing event dispatchtables"""

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
import pytest

from castle.aigr.components import dispatch_tables
from castle.aigr import ID

@pytest.mark.skip(reason="Generic dispatchtable tests are not available yet")
def test99_ToDo():
    assert False


def test_1a_whenInit_PortIsSet():
    table = dispatch_tables._DispatchTable(port=ID("MockPort"))
    assert table.port == "MockPort"

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

