# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers import RPy


from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

@pytest.fixture
def eTable():
    impl = Hello_World.findNode('Elemental_HelloWorld')
    assert False, "XXX ToDo: return the (Event)DispatchTable ..."

def test_0(eTable):
    assert False, "The AIGR (of elemental HW) has no EventDispatchTable"
