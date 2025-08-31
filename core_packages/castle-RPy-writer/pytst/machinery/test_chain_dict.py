# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

import pytest

from castle.aigr import ID
from castle.writers.RPy.writer.machinery import Machinery
from castle.writers.RPy.writer.machinery import M_DC_chained_dict

from .. import my_renderer
from .. import verify_line_by_line, print_out

from .hack_DispatchTables import EventDispatchTable   # XXX

myhack = EventDispatchTable(_comp=ID("C1"), _port=ID("P1"), map={ID("E1"):"H1", ID("E2"):"H2"}) # Note: not std names!
#TableName = cc_S_{comp}_{port}
myhack_EXPECT="""\
cc_S_C1_P1 = buildin.machinery.ChainedDict(map={
    'E1' : H1,
    'E2' : H2,
    },
    parent=None)
\n"""


@pytest.fixture
def machinery() ->Machinery:
    return Machinery(hint="chained_dict")

def test_1_hint_gives_chainned_dict_machinery(machinery):
    explicit = M_DC_chained_dict()
    assert type(machinery) is type(explicit)


def test_2_(machinery, my_renderer):
    blck = machinery.render_EventDispatchTable(renderer=my_renderer, node=myhack)
    txt = str(blck)
    #print_out(myhack_EXPECT, label="expect");  print_out(txt, label="result")
    verify_line_by_line(myhack_EXPECT, txt)
