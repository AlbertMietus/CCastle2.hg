# (C) Albert Mietus, 2025. Part of Castle/CCastle project

assert False, "I think this code is dead --GAM; 5 Oct 2025"
###########################################################

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID


from .mocks import *

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
