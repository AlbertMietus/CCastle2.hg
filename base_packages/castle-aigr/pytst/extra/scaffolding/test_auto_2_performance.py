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


class SpyAutoScaffolder(AutoScaffolder):
    """Spy subclass recording calls to `_search`, to be able how often it is called.

       Use it like AutoScaffolder(), with 2 extra spy interfaces `reset()` and `count()`"""

    _scan_log: list = []

    @classmethod
    def _search(cls, node_cls):                    # Override original one
        cls._record_scan()
        return super()._search(node_cls)

    @classmethod
    def _record_scan(spy):
        spy._scan_log.append(1) # arbitrary value - only len() is relevant (now)

    @classmethod
    def reset(spy):
        """Reset spy state and clear the dispatch cache -- call before each test to ensure isolation."""
        spy._scan_log.clear()
        AutoScaffolder._direct_map.clear()

    @classmethod
    def scan_count(spy) -> int:
        """Number of times the scaffolder tree was scanned."""
        return len(spy._scan_log)


@pytest.fixture()
def AutoScaffolderSpy():
    SpyAutoScaffolder.reset()
    return SpyAutoScaffolder


def test_1b_repeated_calls_scan_only_once(AutoScaffolderSpy):
    AutoScaffolderSpy(DirectNode()) # will trigger the scan
    inital_count =  AutoScaffolderSpy.scan_count()
    assert inital_count == 1 # verify the scan in triggered

    for n in range(1, MAX):
        SpyAutoScaffolder(DirectNode())
        count = AutoScaffolderSpy.scan_count()
        assert count == inital_count, f"Expected no extra scans, but {count=} for {n=} extra lookup"



@pytest.mark.skip(reason="ToDo: after we support O(1) dispatch for inherited (non 1:1) matches")
def test_999_inherited_match_scans_once_regardless_of_call_count():
    """Same guarantee as test_1a/1b, but for a node with no direct 1:1 Scaffolder."""
    assert False
