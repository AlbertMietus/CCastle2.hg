# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr.components import EventDispatchTable
from castle.aigr import ID

from .. import my_renderer
from ..verify import *

@pytest.fixture
def demoTable():
    table = EventDispatchTable()
    table.register_event(ID('port'), ID('event'), ID('handler'))
    return table

@pytest.mark.xfail
def test_0(demoTable, my_renderer):
    txt=my_renderer.render(demoTable)
    print_out(txt, label='demoTable')

    assert False
