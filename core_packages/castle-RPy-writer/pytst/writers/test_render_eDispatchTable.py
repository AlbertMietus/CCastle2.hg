# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr.components import EventDispatchTable
from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr import ID



from .. import my_renderer
from ..verify import *

@pytest.fixture
def Mock_comp():
    return aigr.ComponentImplementation(ID('Mock'),
                                        interface=aigr.ComponentInterface(ID('Mock'),
                                                                          ports=aigr.Port('a_Port', direction='X', type='X') ))

@pytest.fixture
def demoTable(Mock_comp):
    table = EventDispatchTable(component=Mock_comp)
    table.register_event(ID('a_port'), ID('an_event'), ID('the_handler'))
    return table


def test_demo(demoTable, my_renderer):
    txt=my_renderer.render(demoTable)
    #print_out(txt, label='demoTable')

    verify_line_by_line("""\
cc_S_Mock_a_port = buildin.machinery.ChainedDict(map={
    an_event : the_handler,
    },
    parent=base.cc_S_Component_a_port)
\n""",
    str(txt))
