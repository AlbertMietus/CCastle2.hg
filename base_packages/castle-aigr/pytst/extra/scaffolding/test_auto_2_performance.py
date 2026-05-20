# (C) Albert Mietas 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from dataclasses import dataclass
from castle.aigr import AIGR
from castle.aigr_extra.scaffolding import AutoScaffolder
from castle.aigr_extra.scaffolding._scaffolder import _Scaffolder


MAX= 10 # an arbitrary number; any MAX>1 will do.

@dataclass
class DirectNode(AIGR):               """Node with a direct 1:1 Scaffolder."""
class DirectScaffolder(_Scaffolder):  _nodeCls = DirectNode

class InheritedNode(DirectNode):      """Node with no own Scaffolder -- falls back to DirectScaffolder."""


class SpyAutoScaffolder(AutoScaffolder):
    """Spy subclass recording calls to `_resolve`, to observe how often it is called.

       Use it like AutoScaffolder(), with 2 extra spy interfaces `reset()` and `scan_count()`"""

    _scan_log: list = []

    @classmethod
    def _resolve(cls, node_cls):                   # Override to spy on resolution
        cls._record_scan()
        return super()._resolve(node_cls)

    @classmethod
    def _record_scan(spy):                       # pyright: ignore[reportSelfClsParameterName] -- spy is better then cls
        spy._scan_log.append(1) # trivial value

    @classmethod
    def reset(spy):                              # pyright: ignore[reportSelfClsParameterName] -- spy is better then cls
        """Reset spy state and clear the dispatch cache -- call before each test to ensure isolation."""
        spy._scan_log.clear()
        AutoScaffolder._direct_map.clear()
        AutoScaffolder._inherited_map.clear()

    @classmethod
    def scan_count(spy) -> int:                  # pyright: ignore[reportSelfClsParameterName] -- spy is better then cls
        """Number of times the scaffolder tree was scanned."""
        #return len([n for n in spy._scan_log if issubclass(n, node_cls)])
        return len(spy._scan_log)


@pytest.fixture()
def AutoScaffolderSpy():
    SpyAutoScaffolder.reset()
    return SpyAutoScaffolder


def test_1_repeated_DirectScaffolder_scans_only_once(AutoScaffolderSpy):
    AutoScaffolderSpy(DirectNode())                # will trigger the scan
    inital_count = AutoScaffolderSpy.scan_count()
    assert inital_count == 1                       # verify the scan is triggered

    for n in range(1, MAX):
        SpyAutoScaffolder(DirectNode())
        count = AutoScaffolderSpy.scan_count()
        assert count == inital_count, f"Expected no extra scans, but {count=} for {n=} extra lookup"


def test_2_repeated_InheritedScaffolder_scans_only_once(AutoScaffolderSpy):
    AutoScaffolderSpy(InheritedNode())             # will trigger the scan
    inital_count = AutoScaffolderSpy.scan_count()
    assert inital_count == 1                       # verify the scan is triggered

    for n in range(1, MAX):
        SpyAutoScaffolder(InheritedNode())
        count = AutoScaffolderSpy.scan_count()
        assert count == inital_count, f"Expected no extra scans, but {count=} for {n=} extra lookup"

@pytest.mark.skip
def test_99_Fast_and_Correct():
    """When testing the cache is working, we should also show the result is correct -- implement/improve soon"""
    assert False

@pytest.mark.skip(reason="ToDo: after we support O(1) dispatch for inherited (non 1:1) matches")
def test_999_inherited_match_scans_once_regardless_of_call_count():
    """Same guarantee as test_2, but for a node with no direct 1:1 Scaffolder."""
    assert False
