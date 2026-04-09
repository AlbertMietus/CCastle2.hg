# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""CastleCode

----Simple/Single: a SingleDummy implements both events of mockProtocol and inherits nothing---
protocol mockProtocol : EventProtocol {
   fakeEvent_a();
   fakeEvent_b();
}

component SingleDummy {
   port mockProtocol <in>: MockPort;
}

implement SingleDummy {
   mockProtocol.fakeEvent_a on .MockPort {....} # ==> callable_H1
   mockProtocol.fakeEvent_b on .MockPort {....} # ==> callable_H2
}

---Child: One own handler, and inherits one from it parent: SingleDummy---
component Child:SingleDummy {
   port mockProtocol <in>: MockPort; ///GAM: is it needed/allowed to repeat?
}

implement Child {
   mockProtocol.fakeEvent_a on .MockPort {....} # ==> callable_H3
   # fakeEvent_b is inherited from SingleDummy

"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import ID
from castle.writers.RPy.writer.machinery import Machinery
from castle.writers.RPy.aigr import EventDispatchTable



@pytest.fixture
def machinery() ->Machinery:
    return Machinery(hint="chained_dict")                                    # type: ignore[reportAbstractUsage, abstract]

@pytest.fixture
def singleTable() ->tuple[EventDispatchTable, str]:
    """Returns the EventDispatchTable & expected text for 'SingleDummy: one without a parentTable"""

    map = {
        (ID("mockProtocol"), ID("fakeEvent_a")): ID("callable_H1"),
        (ID("mockProtocol"), ID("fakeEvent_b")): ID("callable_H2"),
    }
    table = EventDispatchTable(comp=ID("SingleDummy"), port=ID("MockPort"), map=map, parentTable=None)

    expectedTxt = """\
cc_S_SingleDummy_MockPort = buildin.machinery.ChainedDict(map={
    'CC_P_mockProtocol_fakeEvent_a' : CC_SingleDummy.callable_H1,
    'CC_P_mockProtocol_fakeEvent_b' : CC_SingleDummy.callable_H2,
    },
    parent=None)
\n"""

    return table, expectedTxt


@pytest.fixture
def childTable(singleTable) ->(EventDispatchTable, str):
    """EventDispatchTable & expected text for 'Child' with parentTable 'SingleDummy'"""

    map = {
        (ID("mockProtocol"), ID("fakeEvent_a")): ID("callable_H3"),
    }
    table = EventDispatchTable(comp=ID("Child"), port=ID("MockPort"), map=map, parentTable=singleTable[0])

    expectedTxt = """\
cc_S_Child_MockPort = buildin.machinery.ChainedDict(map={
    'CC_P_mockProtocol_fakeEvent_a' : CC_Child.callable_H3,
    },
    parent=cc_S_SingleDummy_MockPort)
\n"""

    return table, expectedTxt
