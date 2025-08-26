# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID, NamedNode,  errors

from . import ScaffolderNode
from ._scaffolder import _Scaffolder

class ScaffolderNameSpace(ScaffolderNode):
    _nodeCls:type = aigr.namespaces._NameSpace

    def register(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        if isinstance(named_node, _Scaffolder):
            logger.error("It's wrong to register wrapped nodes, like %s - unwrapping it and continuing with fingers crosses", named_node)
            named_node = named_node.node # unwrap ...

        # For NOW: hardcoded, XXX/ToDo: use visitor with ` _find_method_by_mro`
        if isinstance(named_node, aigr.NamedNode):             # A NameSpace (NS) can only register NamedNode(s) in it NS, so ....
            self.register_NamedNode(named_node, asName)
        else:
            assert False, f"Can only register 'NamedNode', not {named_node}"

    def register_NamedNode(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        name = ID(asName) if asName else PTH.cast(ID, named_node.name)
        if name in self.node._ns:
            old = self.node._ns[name]
            logger.warning(f"The '{name}'-node is already in this namespace; -- it will be lost." +
                           f"Removed: {old}. New: {named_node}")
        self.node._ns[str(name)] = named_node

    def __len__(self):
        return len(self.node._ns)




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

    def _findNode(self, name :ID) ->PTH.Optional[NamedNode]:
        """Return the NamedNode with the specified ID, or None.
           It looks in 'this' namespace, and in outer_ns's when they exist.
           All public interfaces will use this method."""
        node = self.node._ns.get(str(name), None)
        if node is None:
            logger.debug("Can't find %s locally: %s -- try outer_ns: %s", name, tuple(f"{k}:{type(k).__name__}" for k in self.node._ns.keys()), self.node.outer_ns)
        if node is None and self.node.outer_ns:
            node = ScaffolderNameSpace(self.node.outer_ns)._findNode(name)
        logger.debug("Find %s in %s\n\t-> %s", name, self, node)
        return node


    def findNode(self, name :ID|str) ->PTH.Optional[NamedNode]:
        if not isinstance(name, ID): name=ID(name)
        return self._findNode(name) # self is a Scaffolder!


    def getID(self, name :ID) ->NamedNode: #Or raise NameError
        """Return the NamedNode with the specified name (aka ID), or raised an NameError:AttributeError.
           See :method:`findNode` for an alternative"""
        if not isinstance(name, ID): name=ID(name)
        node = self._findNode(name) # self on Scaffolder!
        if node is None:
            raise errors.NameError(f"No node named {name} in NS:{getattr(self,'name','')}")
        return node


    def search(self, dottedName :ID|str) ->PTH.Optional[NamedNode]:
        """Search the namespace for the 1st part of `dottedName`, then that NS for the next part, etc. And return the "deepest" node, or None"""

        parts = dottedName.split('.',maxsplit=1) # parts is [<name>, (<name>.)*] parts[1] can be absent, parts[0] always exist
        logger.debug("Search %s of %s (len=%s) in %s", parts[0], dottedName, len(parts), self)
        node = self.findNode(parts[0]) # self is Scaffolder!
        if node is None: # Not found:
            return None
        if len(parts) == 1: # Found it
            return node
        try:
            return ScaffolderNameSpace(node).search(parts[1])                              #XXXXtype: ignore[union-attr] # Assume a NS, else raise
        except AttributeError: #node isn't a search'able/namespace --> Not found --> return None
            return None

    def find_byType(self, cls:type) ->dict[ID, NamedNode]:
        return {name: PTH.cast(NamedNode, value) for name, value in self.node._ns.items() if isinstance(value, cls)}

    def list_names(self) -> tuple[ID, ...]:
        return tuple(self.node._ns.keys())

