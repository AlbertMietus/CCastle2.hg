# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

import pytest

from castle.aigr import ID
from castle.writers.RPy.writer.machinery import Machinery
from castle.writers.RPy.writer.machinery import M_DC_chained_dict
from castle.writers.RPy.aigr import EventDispatchTable

from .. import my_renderer
from .. import verify_line_by_line, print_out

@pytest.fixture
def machinery() ->Machinery:
    return Machinery(hint="chained_dict")

@pytest.fixture
def simpleTable() ->EventDispatchTable: # Note: does not use std names!
    """returns e-table ``cc_S_{comp}_{port}` with some simple IDs"""
    table = EventDispatchTable(_comp=ID("C1"), _port=ID("P1"), map={ID("E1"):"H1", ID("E2"):"H2"})
    expected = """\
cc_S_C1_P1 = buildin.machinery.ChainedDict(map={
    'E1' : H1,
    'E2' : H2,
    },
    parent=None)
\n"""
    return table, expected

def test_1_hint_gives_chainned_dict_machinery(machinery):
    explicit = M_DC_chained_dict()
    assert type(machinery) is type(explicit)


def test_2_render(machinery, my_renderer, simpleTable):
    table, expected = simpleTable
    blck = machinery.render_EventDispatchTable(renderer=my_renderer, node=simpleTable[0])
    verify_line_by_line(expected, str(blck))
