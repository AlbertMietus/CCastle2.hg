# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest


import castle.writers.RPy.transformers
from castle.TESTDOUBLES.aigr.HelloWorlds.elemental import HelloWorld




def test_0_dummy():
    assert HelloWorld, "Expect an module"
    for name in getattr(HelloWorld, 'ALL'):
         assert getattr(HelloWorld,name), f"All objects in ALL should exist, including {name}"

