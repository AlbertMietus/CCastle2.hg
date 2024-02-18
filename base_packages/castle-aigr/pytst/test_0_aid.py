# (C) Albert Mietus, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import aid

def test_Argument_with_NoName():
    a = aid.Argument(value=1)

    assert a.name == None
    assert a.value == 1
