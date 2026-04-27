# (C) Albert Mietus 2025, 2026 Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID

from . import ScaffolderNameSpace

class ScaffolderCallable(ScaffolderNameSpace):
    _nodeCls = aigr.statements.callables._callable
    _kid_fields:  frozenset[str] = frozenset({'body'})
    _attr_fields: frozenset[str] = frozenset({'parameters'})

    def auto_register(self):
        self.auto_register_parameters()

    def auto_register_parameters(self):
        node = PTH.cast(aigr.statements.callables._callable, self.node)
        if getattr(self, 'parameters', False):
            my_ns = ScaffolderNameSpace(node)

            logger.debug("auto_register_parameters: %s", node.parameters)
            for p in node.parameters:
                my_ns.register(p)

