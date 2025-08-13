# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID

from .namespaces import ScaffolderNameSpace

class ScaffolderComponentImplementation(ScaffolderNameSpace):
    _nodeCls = aigr.ComponentImplementation

    #def register(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):pass # XXX disable ScaffolderNameSpace.register

    def register_event(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        ...

