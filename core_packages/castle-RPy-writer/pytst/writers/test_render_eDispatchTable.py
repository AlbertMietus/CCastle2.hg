# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr.components import EventDispatchTable

from castle.aigr import ID

from .. import chainDict_renderer
from ..verify import *
from .mocks import *
from castle.aigr_extra.blend import mangle_event_handler

@pytest.fixture
def demoTable(mockComp, mockPort, mockEvents):
    table = EventDispatchTable(component=mockComp)
    table.register_event(port_name=mockPort.name, event_name=mockEvents[0].name,
                             handler_name=ID(mangle_event_handler(protocol='an', event='other', port='name')))

    return table

Expected_demo_Chain="""\
cc_S_MockComp_MockPort = buildin.machinery.ChainedDict(map={
    MockEvent_1 : an_other__name,
    },
    parent=None)
"""

@pytest.mark.xfail(reason="Desing of 'EventDispatchTable' needs update: can't determine the parent")
def test_demo(demoTable, chainDict_renderer):
    result = chainDict_renderer.render(demoTable)
    print_out(result, label='demoTable - parent is wrong')

    verify_line_by_line(Expected_demo_Chain, result)
