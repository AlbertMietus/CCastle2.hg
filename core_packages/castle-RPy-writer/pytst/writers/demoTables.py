# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

### DispatchTable(s): See remark on EventDispatchTable
#from castle.aigr.components import EventDispatchTable


from .mocks import *

def fakeHandlerName(protocol, event, port):
    return f'__Fake__{protocol}_{event}_on_{port}__HandlerName__'

def gen_Dummy_EventMap(proto, port):
    logger.info('XXXX1a proto: %s; port: %s', proto, port)
    map = {event.name: fakeHandlerName(event=event.name, port=port.name, protocol=proto.name) for event in proto.events}
    logger.info('XXXX2 map: %s', map)
    return map

#@pytest.fixture
#def simpleTable(mockPort, stubProtocol) -> aigr.EventDispatchTable:
#    """A simple EventDispatchTable, with no inherited details."""
#    return EventDispatchTable(map=gen_Dummy_EventMap(stubProtocol, mockPort), _comp=ID('Simple'), _port=mockPort.name)


#@pytest.fixture
#def childTable(mockPort, subStubProtocol) -> aigr.EventDispatchTable:
#    """An EventDispatchTable, with linked to `simpleTable`"""
#    return EventDispatchTable(map=gen_Dummy_EventMap(subStubProtocol, mockPort), _comp=ID('Child'), _port=mockPort.name, _parentTable=ID('Simple'))


Expected_4_simpleTable="""\
cc_S_Simple_MockPort = buildin.machinery.ChainedDict(map={
    DummyEvent_1 : __Fake__StubProtocol_DummyEvent_1_on_MockPort__HandlerName__,
    DummyEvent_2 : __Fake__StubProtocol_DummyEvent_2_on_MockPort__HandlerName__,
    },
    parent=None)\n
"""

Expected_4_childTable="""\
cc_S_Child_MockPort = buildin.machinery.ChainedDict(map={
    DummyEvent_3 : __Fake__SubStubProtocol_DummyEvent_3_on_MockPort__HandlerName__,
    },
    parent=cc_S_Simple_MockPort)\n
"""
