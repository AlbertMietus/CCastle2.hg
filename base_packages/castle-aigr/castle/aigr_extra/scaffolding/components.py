# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID

from .namespaces import ScaffolderNameSpace
from ._scaffolder import _Scaffolder

_TYPE=aigr.EventHandler
class ScaffolderComponentImplementation(ScaffolderNameSpace):
    _nodeCls :type = aigr.ComponentImplementation

    ## XXX &C&P ScaffolderNameSpace    
    def register(self, node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None): 
        if isinstance(node, _Scaffolder):
            logger.error("It's wrong to register wrapped nodes, like %s - unwrapping it and continuing with fingers crosses", node)
            node = node.node # unwrap ...

        # For NOW: hardcoded, XXX/ToDo: use visitor with ` _find_method_by_mro`
        if isinstance(node, _TYPE):             # XXX
            self.register_EventHandler(node, asName)
        else:
            super().register(node, asName)


    def register_EventHandler(self, node :aigr.EventHandler, asName :PTH.Optional[ID|str]=None): # XXX Or register__handlers XXX
        if asName is not None and not asName == node.name:
            logger.error("It's wrong to register EventHandler (%s) with a diffent name (%s). Ignoring that ...", node.name, asName)
        self.node.handlers.append(node)

