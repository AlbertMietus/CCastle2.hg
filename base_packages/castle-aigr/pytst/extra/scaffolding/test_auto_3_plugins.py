# (C) Albert Mietas 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from itertools import count

from castle.aigr import AIGR
from castle.aigr_extra.scaffolding import AutoScaffolder
from castle.aigr_extra.scaffolding._scaffolder import _Scaffolder

class BaseNode(AIGR):               """Stable base node -- always present, like a built-in."""
class BaseScaffolder(_Scaffolder):  _nodeCls = BaseNode

class PluginMock:
    _seq = count(1)                                            # unique sequence number
    def __init__(self):
        self.seq = next(self._seq)
    def _mk_pair(self):
        self.nodeCls = type(f'PluginNode_{self.seq}', (BaseNode,), {})
        self.scaffolderCls = type(f'PluginScaffolder_{self.seq}', (BaseScaffolder,), {'_nodeCls': self.nodeCls})
    def load(self):
        self._mk_pair()
        logger.info(f"Loaded {self.__class__.__qualname__} no {self.seq}")
    def verify_fromPlugin(self, obj):
        "assert/verify `obj` is an instance from this plugin"
        assert isinstance(obj, (self.nodeCls, self.scaffolderCls)), f"{obj} is not form plugin-no {self.seq}"
        return True

@pytest.fixture
def plugin_loader():
    return PluginMock()


def test_1_plugin_node_is_found_and_base_is_unaffected(plugin_loader):
    ref =  AutoScaffolder(BaseNode())
    assert isinstance(ref, BaseScaffolder) # verify only

    plugin_loader.load()

    wrapped = AutoScaffolder(plugin_loader.nodeCls())
    assert isinstance(wrapped, plugin_loader.scaffolderCls), f"{wrapped=}, but expected {type(plugin_loader.scaffolderCls).__qualname__}"
    assert plugin_loader.verify_fromPlugin(wrapped)

def test_2_check_independ_plugins(plugin_loader):
    plugin_loader.load()
    wrapped = AutoScaffolder(plugin_loader.nodeCls())

    other_plugin = PluginMock(); other_plugin.load()
    with pytest.raises(AssertionError):
        other_plugin.verify_fromPlugin(wrapped)
