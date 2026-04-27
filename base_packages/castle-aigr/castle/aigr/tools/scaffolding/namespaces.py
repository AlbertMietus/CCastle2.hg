# (C) Albert Mietus 2025, Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import NamedNode,  errors
from castle.aigr import ID, QualID

from castle.monorail.base  import MRO_Dispatch_Mixin
from . import ScaffolderNode
from ._scaffolder import _Scaffolder

class ScaffolderNameSpace(ScaffolderNode, MRO_Dispatch_Mixin): # XXX or Scaffolder_NameSpace
    _nodeCls:type = aigr.namespaces._NameSpace
    _prefixes = ('register',) # For MRO_Dispatch_Mixin

    def register(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        logger.debug("register: named_node=%s asName=%s", named_node, asName)
        if isinstance(named_node, _Scaffolder):
            logger.error("It's wrong to register wrapped nodes, like %s - unwrapping it and continuing with fingers crosses", named_node)
            named_node = named_node.node # unwrap ...

        register_method = self.dispatch_find_method_by_mro(named_node, 'register')
        register_method(named_node, asName)     # type: ignore[misc] # exist always, is there is a default: see below

    def __len__(self):
        return len(PTH.cast(aigr.namespaces._NameSpace, self.node)._ns)


###
###  `find*()`, ` get*() & `search()` -- all via _findNode()
###

    def _findNode(self, name :ID) ->PTH.Optional[NamedNode]:
        """Return the NamedNode with the specified ID, or None.
           It looks in 'this' namespace, and in outer_ns's when they exist.
           All public interfaces will use this method."""
        my_ns = PTH.cast(aigr.namespaces._NameSpace, self.node)._ns
        outer_ns = PTH.cast(aigr.namespaces._NameSpace, self.node).outer_ns

        node  = my_ns.get(name,None)
        if node is None:
            logger.debug("Can't find %s locally: %s -- try outer_ns: %s", name, tuple(f"{k}:{type(k).__name__}" for k in my_ns.keys()), outer_ns)
        if node is None and outer_ns:
            node = ScaffolderNameSpace(outer_ns)._findNode(name)
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
        return {name: PTH.cast(NamedNode, value) for name, value in  PTH.cast(aigr.namespaces._NameSpace, self.node)._ns.items() if isinstance(value, cls)}

    def list_names(self) -> tuple[ID, ...]:
        return tuple( PTH.cast(aigr.namespaces._NameSpace, self.node)._ns.keys())

    def search_qualNames(self ) -> tuple[QualID, ...]:
        """Return all names in this namespace recursively, as QualIDs -- also see: search_dottedNames"""
        return self._search_recursively(_prefix=None)

    def search_dottedNames(self) -> tuple[str, ...]:
        """Return all names in this namespace recursively, as dottedNames -- also see: search_qualNames"""
        quals = self._search_recursively(_prefix=None)
        return tuple(['.'.join(name) for name in quals])

    def _search_recursively(self, *, _prefix: PTH.Optional[QualID]=None, ) ->tuple[QualID, ...]:
        prefix = _prefix or []
        result: list[QualID] = []
        for name, node in PTH.cast(aigr.namespaces._NameSpace, self.node)._ns.items():
            qualID = prefix + [ID(name)]
            result.append(qualID)
            if isinstance(node, aigr.namespaces._NameSpace):
                result.extend(ScaffolderNameSpace(node)._search_recursively(_prefix=qualID))
        return tuple(result)


###
### Some register_* function
### (more are in subclasses)
###
    def _default_register(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        logger.error("Default register for %s is called -- this is often a mistake", type(named_node).__name__, stack_info=True)
        logger.error("XTRA: \n\t self=%s \n\t named_node=%s \n\t asName=%s", self, named_node, asName)


    def register_NamedNode(self, named_node :aigr.NamedNode, asName :PTH.Optional[ID|str]=None):
        logger.debug("register_NamedNode: named_node=%s asName=%s}", named_node, asName)
        name = ID(asName) if asName else PTH.cast(ID, named_node.name)
        my_ns = PTH.cast(aigr.namespaces._NameSpace, self.node)._ns
        if name in my_ns:
            old =my_ns[name]
            logger.warning("The '%s'-node is already in this namespace -- it will be lost. Old=%s. New=%s", name, old, named_node)
        my_ns[name] = named_node


    def _register_NN_and_outer_ns(self, named_node, asName):
        self.register_NamedNode(named_node, asName) # As all named_node's
        # And set .outer_ns - after checking it unset
        if named_node.outer_ns:
            log_at_level = logger.warning if not (named_node.outer_ns is self.node) else logger.debug
            log_at_level("outer_ns is already set (to: %s), it will be lost (set to: %s)", named_node.outer_ns, self.node)
        named_node.outer_ns = self.node


    def register__NameSpace(self, named_node :aigr.namespaces._NameSpace, asName :PTH.Optional[ID|str]=None):
        logger.debug("register__NameSpace -- like register_NamedNode, but also set `outer_ns` in node")
        self._register_NN_and_outer_ns(named_node, asName)


    def register_Method(self, named_node :aigr.Method, asName :PTH.Optional[ID|str]=None):
        logger.debug(".register_Method: named_node=%s asName=%s", named_node, asName)
        self._register_NN_and_outer_ns(named_node, asName)


    def register_ComponentInterface(self, comp: aigr.ComponentInterface, asName :PTH.Optional[ID|str]=None):
        logger.debug("register_ComponentInterface: comp=%s asName=%s", comp, asName)
        name = ID(asName) if asName else PTH.cast(ID, comp.name)
        my_ns = PTH.cast(aigr.namespaces._NameSpace, self.node)._ns

        if name in my_ns:                                           # assume the implementation is registered
            registered = my_ns[name]
            if isinstance(registered, aigr.ComponentImplementation):
                if registered.interface is not None:
                    logger.warning("The interface of ComponentImplementation '%s' is already registered --it will be lost. Old=%s, new=%s",
                                       name, registered.interface.name, comp.name)
                registered.interface = comp
            else:
                logger.warning("Old entry: %s -- will be lost", registered)
                my_ns[name] = comp
        else:
            logger.debug("save comp=%s in NS[%s]", comp, name)
            my_ns[name] = comp                                                                   #Register the interface


    def register_ComponentImplementation(self, comp: aigr.ComponentImplementation, asName :PTH.Optional[ID|str]=None):
        logger.debug("register_ComponentImplementation: comp=%s asName=%s", comp, asName)   #XXX .info->.debug
        name = ID(asName) if asName else PTH.cast(ID, comp.name)
        my_ns = PTH.cast(aigr.namespaces._NameSpace, self.node)._ns

        if name in my_ns: # assume the interface is registered
            registered = my_ns[name]
            if isinstance(registered, aigr.ComponentInterface):
                if comp.interface is not None:
                    logger.warning("The interface of '%s' was set to %s; it will be lost", name, comp.interface)
                logger.info("set interface of %s to %s", comp, registered)
                comp.interface = registered
            else:
                logger.warning(f"The '%s'-node is already in this namespace; -- %s will be lost", name, registered)
                my_ns[name] = comp

        logger.info("save comp=%s in NS([%s]", comp, name)
        my_ns[name] = comp                                                                 # Register the implementation


