# (C) Albert Mietus 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import AIGR
from castle.aigr_extra.scaffolding import AutoScaffolder
from castle.aigr_extra.scaffolding._scaffolder import _Scaffolder


class StubBase(AIGR):             """Just an AIGR subclass, for testing -- with (test) Scaffolder"""
class StubChild(AIGR):            """Direct subclass of StubBase -- has its own scaffolder."""
class StubGrandChild(StubChild):  """A subclass of StubChild -- no own Scaffolder should fall back to StubChildScaffolder."""
class DummyOrphan(AIGR):          """AIGR subclass without a Scaffolder at all"""

class StubBaseScaffolder(_Scaffolder):   _nodeCls = StubBase
class StubChildScaffolder(_Scaffolder):  _nodeCls = StubChild


def test_0a_mocks_are_subclasses():
    assert issubclass(StubBase, AIGR)
    assert issubclass(StubChild, AIGR)
    assert issubclass(StubGrandChild, AIGR)
    assert issubclass(DummyOrphan, AIGR)

def test_0b_stubScaffolders_are_Scaffolders():
    assert issubclass(StubBaseScaffolder, _Scaffolder)
    assert issubclass(StubChildScaffolder, _Scaffolder)

def test_0c_AutoScaffolder_is_Scaffolder():
    assert issubclass(AutoScaffolder, _Scaffolder)


def test_0d_AutoScaffolding_does_not_return_AutoScaffolder_instance():
    wrapped = AutoScaffolder(StubBase())
    assert not isinstance(wrapped, AutoScaffolder), "AutoScaffolder wraps node with a factual Scaffolder, never returning an own instance"

def test_0e_AutoScaffolding_nonAIGR_will_fail():
    with pytest.raises(TypeError):
        AutoScaffolder(42) # type: ignore -- -deliberately wrong type
        pytest.fail("AutoScaffolder works only on AIGR nodes -- like all Scaffolders")

@pytest.mark.parametrize("nodeCls, wrapCls", [(StubBase, StubBaseScaffolder), (StubChild, StubChildScaffolder)])
def test_1_Auto_returns_expected_DirectScaffolder(nodeCls, wrapCls):
    assert isinstance(AutoScaffolder(nodeCls()), wrapCls), f"A {nodeCls.__qualname__} instance should be wraped with direct Scaffolders: {wrapCls.__qualname__}"

def test_2_Auto_returns_bases_Scaffolder(): # When there is no 1:1 direct Scaffolder
    assert isinstance(AutoScaffolder(StubGrandChild()), StubChildScaffolder),  "without 1:1 Scaffolder, use instance"


def test_3_Raise_when_no_Scaffolder_exists(): #Never return a wrong wraper
    with pytest.raises(TypeError):
        AutoScaffolder(DummyOrphan())
        pytest.fail("When no (inherited) Scaffolder exist, raise -- should never happen")

