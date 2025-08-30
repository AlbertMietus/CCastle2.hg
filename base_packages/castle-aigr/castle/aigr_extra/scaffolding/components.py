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
        if asName is not None and not asName == node.name:
            logger.error("It's wrong to register EventHandler (%s) with a diffent name (%s). Ignoring that ...", node.name, asName)
        self.node.handlers.append(node)

