# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy.transformers.namespace import _replace_extention
from castle.TESTDOUBLES.aigr.HelloWorlds.elemental import HelloWorld


def test_1_replace_extention():
    # The default extention has become .py, not .rpy
    assert _replace_extention('test_1')                 == 'test_1.py'
    assert _replace_extention('test_2', new_ext='.rpy') == 'test_2.rpy'
    assert _replace_extention('test_3.Castle')          == 'test_3.py'
    assert _replace_extention('test_4.Moat')            == 'test_4.py'
    assert _replace_extention('test_5.foo')             == 'test_5.foo.py'
