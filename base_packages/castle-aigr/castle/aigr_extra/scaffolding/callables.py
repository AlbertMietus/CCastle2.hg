# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID, NamedNode,  errors

from . import ScaffolderNameSpace

class ScaffolderCallable(ScaffolderNameSpace):
    _nodeCls = aigr.statements.callables._callable

    def auto_register_parameters(self):
        if getattr(self, 'parameters', False):
            my_ns = ScaffolderNameSpace(self.node)
            logger.debug("auto_register_parameters: %s", self.node.parameters)
            for p in self.node.parameters:
                my_ns.register(p)

