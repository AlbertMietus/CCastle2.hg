# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID

from .namespaces import ScaffolderNameSpace
from ._scaffolder import _Scaffolder


class ScaffolderComponentImplementation(ScaffolderNameSpace):
    _nodeCls :type = aigr.ComponentImplementation

    def register_EventHandler(self, node :aigr.EventHandler, asName :PTH.Optional[ID|str]=None): # XXX Or register__handlers XXX
        logger.info(f".register_EventHandler: {node=} {asName=} {self=} XXX")
        if asName is not None and not asName == node.name:
            logger.error("It's wrong to register EventHandler (%s) with a diffent name (%s). Ignoring that ...", node.name, asName)
        self.node.handlers.append(node)

    def auto_register(self):
        self.auto_register_handlers()

    def auto_register_handlers(self):
        """Do not call directly!
          Even dou the name of (Event/Data/...) handlers aren't registered on the namespaces of a comp,
          their 'outer_ns' should point to comp"""
        
        for h in self.node.handlers:
            if h.outer_ns:
                log_at_level = logger.warning if not ( h.outer_ns is self.node) else logger.debug
                log_at_level("outer_ns is already set (to: %s), it will be lost (set to: %s)", named_node.outer_ns, self.node)
            h.outer_ns = self.node

        
