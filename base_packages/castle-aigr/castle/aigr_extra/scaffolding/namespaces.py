# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID

from . import ScaffolderNode

class ScaffolderNameSpace(ScaffolderNode):
    _nodeCls = aigr.namespaces._NameSpace

    def register(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):  #### Move to "builder"
        name = ID(asName) if asName else PTH.cast(ID, named_node.name)
        if name in self.node._dict:
            old = self.node._dict[name]
            logger.warning(f"The '{name}'-node is already in this namespace; -- it will be lost." +
                           f"Removed: {old}. New: {named_node}")
        self.node._dict[name] = named_node

    def __len__(self):
        return len(self.node._dict)



