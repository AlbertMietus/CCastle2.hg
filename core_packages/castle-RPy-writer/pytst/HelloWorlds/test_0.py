# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers import RPy


from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World


def test_0_dummy_HW():
    "Just check the aigr-TestDouble can be read"
    assert isinstance(Hello_World, aigr.Source_NS),  f"Unexpected class: {Hello_World}"
    assert Hello_World.name == 'HelloWorld'

def test_0_RPy_unit():
    DUMMY='file.name'
    f = RPy.aigr.RPy_unit(target_file=DUMMY, name=DUMMY)
    assert f.target_file == DUMMY
    assert f.name == DUMMY
