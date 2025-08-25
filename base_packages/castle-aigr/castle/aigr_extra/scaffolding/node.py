# (C) Albert Mietus 2025, Part of Castle/CCastle project


import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle.aigr import AIGRNode
from ._scaffolder import _Scaffolder

class ScaffolderNode(_Scaffolder):
    _nodeCls:type = AIGRNode

    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> PTH.Self:
        node = self.node
        parent_node = parent.node if isinstance(parent, _Scaffolder) else parent
        node.parent = parent_node
        return self  # for chaining
