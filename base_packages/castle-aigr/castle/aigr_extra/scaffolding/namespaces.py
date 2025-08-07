# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID, NamedNode,  errors

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




### The following 3 methods are overkill.
### + findNode/getID only looks locally returning None (findNode) or raise NameError on no match
### + search is like findNode, but looks also in subNS'ses
###
### So,
### - ``NS.findNode(name)`` and ``NS.search(name)`` are equivalent
###     (but search calls findNode, and can't be removed. find is also a better name)
###- There is no getID() for dottedName's
###
### _findNode() is the basic function, all others call it
###   So, only that needs to be overwritten
###   Possible rename it to _findNode()

    def _findNode(self, name :ID) ->PTH.Optional[NamedNode]:                       #### Move to "builder"
        """Return the NamedNode with the specified ID, or None.
           It looks in 'this' namespace, and in outer_ns's when they exist.
           All public interfaces will use this method."""
        node = self._dict.get(name, None)
        logger.info("Can't find %s locally: %s -- try outer_ns: %s", name, tuple(self._dict.keys()), self.outer_ns)
        if node is None and self.outer_ns:
            node = self.outer_ns._findNode(name)
        return node


    def findNode(self, name :ID|str) ->PTH.Optional[NamedNode]:   ##### Move to "builder"
        if not isinstance(name, ID): name=ID(name)
        return self._findNode(name)


    def getID(self, name :ID) ->NamedNode: #Or raise NameError          #### Move to "builder"
        """Return the NamedNode with the specified name (aka ID), or raised an NameError:AttributeError.
           See :method:`findNode` for an alternative"""
        if not isinstance(name, ID): name=ID(name)
        node = self._findNode(name)
        if node is None:
            raise errors.NameError(f"No node named {name} in NS:{getattr(self,'name','')}")
        return node


    def search(self, dottedName :ID) ->PTH.Optional[NamedNode]: #### Move to "builder"
        """Search the namespace for the 1st part of `dottedName`, then that NS for the next part, etc. And return the "deepest" node, or None"""

        parts = dottedName.split('.',maxsplit=1) # parts is [<name>, (<name>.)*] parts[1] can be absent, parts[0] always exist
        node = self.findNode(parts[0])
        if len(parts) == 1:
            return node
        try:
            return node.search(parts[1])                              #type: ignore[union-attr] # Assume a NS, else raise
        except AttributeError: #node isn't a search'able/namespace --> Not found --> return None
            return None

    def find_byType(self, cls:type) ->dict[ID, NamedNode]: #### Move to "builder"
        return {name: node for name, node in self.node._dict.items() if isinstance(node, cls)}

    def list_names(self) -> tuple[ID, ...]: #### Move to "builder"
        return tuple(self.node._dict.keys())
    
