# (C) Albert Mietus 2026, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler
from castle.aigr.tools.scaffolding import ScaffolderNameSpace

from . import elemental

EH_NAME = mangle_event_handler(protocol='std', event='invoke', port='std')

@pytest.fixture
def call2_HelloWord(elemental):
    x = ScaffolderNameSpace(elemental).search('Elemental_HelloWorld')
    print("x/Elemental_HelloWorld:", x)
    hs = x.handlers; assert hs # Check only
    for h in hs:
        if h.name == EH_NAME:
            assert isinstance(h, aigr.EventHandler) # Check only
            assert h.body and isinstance(h.body.statements[0], aigr.VoidCall) # Check only
            return h.body.statements[0].call
    assert False, f"Can't find EventHandler: {EH_NAME} in {hs}"


def test_1_selfCall(call2_HelloWord):
    name = call2_HelloWord.callable
    # The asserts are a bit "dubble up" -- but increments helps in debuging
    assert 'self' in name
    assert 'self.' in name
    assert name.startswith("self."), f"Calling {name=} should be a calling self -- {call2_HelloWord=}"
