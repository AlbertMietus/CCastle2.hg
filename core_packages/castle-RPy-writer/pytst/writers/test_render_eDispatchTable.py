# (C) Albert Mietus, 2025. Part of Castle/CCastle project


"""///CastleCode
protocol stubProtocol : EventProtocol {
   DummyEvent_1();
   DummyEvent_2();
}
component simple {
   port stubProtocol<in>: MockPort;
}
component child:simple {
   port stubProtocol<in>: MockPort; ///GAM: is it needed/allowd to repeat?
}
implement simple {
stubProtocol.DummyEvent_1 on .MockPort {....} // Does something
}
implement child {
stubProtocol.DummyEvent_1 on .MockPort {....} // Does something else:-)
}
"""


import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from .. import chainDict_renderer
from ..verify import *

from .demoTables import * # fixtures and  <Expected>



@pytest.mark.xfail(reason="Design of 'EventDispatchTable' needs update: can't determine the parent")
def test_simpeTable(simpleTable, chainDict_renderer):
    result = chainDict_renderer.render(simpleTable)
    print_out(result, label='demoTable - parent is wrong')
    verify_line_by_line(Expected_4_simpleTable, result)

@pytest.mark.skip("see above: design ...")
def test_childTable(childTable, chainDict_renderer):
    result = chainDict_renderer.render(childTable)
    print_out(result, label='demoTable - parent is wrong')
    verify_line_by_line(Expected_4_childTable, result)
