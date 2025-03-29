# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This file contains AIGR-classes to model (all kind of) namespaces, including "scopes". A namespace can be named, or unamed.

There are several kind of namespaces, like:
 * ``Source_NS`` : roughly, the file that contains (Castle) code.
 * ``Scope``     : an (unamed) namespace like the body of a function, class, component ect
 * ``SubScope``  : roughly anything between '{'  and '}' which defines names.

.. note::

   * Many namespaces have a name (where the name is registered in the outer NS).
   * That dataclasses is called NamedSpace (with a _d_) and use NamedNode as a MixIn
   * Unnamed namedspace are often called a scope
"""

from __future__ import annotations

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .nodes import NamedNode,  ID
from .base import AIGR
from .base import errors


@dataclass
class _NameSpace(AIGR):
    """This models a namespace and/or scope (baseclass).

    It contained *"named nodes"* that should be :method:`register()`ed and can be found by :method:`getID()` and/or :method:`findNode()`.

    Most namespace have a ``outer_ns`` which is also used to lookup names. Howver, qua interface it is optional.
    """
    _: KW_ONLY
    outer_ns   :PTH.Optional[_NameSpace]=None
    _dict      :PTH.Dict[ID, NamedNode]=dc_field(init=None, default_factory=lambda: dict()) #type: ignore[call-overload]


    def register(self, named_node :NamedNode, asName :PTH.Optional[ID|str]=None):
        name = ID(asName) if asName else PTH.cast(ID, named_node.name)

        logger.debug(f"register: <{type(named_node).__name__}:{named_node.name}> as {name} in <{type(self).__name__}:{getattr(self, 'name', '_UnNamed_')}>")

        if name in self._dict:
            old = self._dict[name]
            logger.warning(f"The '{name}'-node is already in this namespace; -- it will be lost." +
                           f"Removed: {old}. New: {named_node}")
        self._dict[name] = named_node



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
###
###

    def _findNode(self, name :ID) ->PTH.Optional[NamedNode]:
        """Return the NamedNode with the specified ID, or None.
           It looks in 'this' namespace, and in outer_ns's when they exist.
           All public interfaces will use this method."""

        node = self._dict.get(name, None)
        if node is None and self.outer_ns:
            node = self.outer_ns._findNode(name)
        return node

    def findNode(self, name :ID|str) ->PTH.Optional[NamedNode]:
        if not isinstance(name, ID): name=ID(name)
        return self._findNode(name)


    def getID(self, name :ID) ->NamedNode: #Or raise NameError
        """Return the NamedNode with the specified name (aka ID), or raised an NameError:AttributeError.
           See :method:`findNode` for an alternative"""
        if not isinstance(name, ID): name=ID(name)
        node = self._findNode(name)
        if node is None:
            raise errors.NameError(f"No node named {name} in NS:{getattr(self,'name','')}")
        return node

    def search(self, dottedName :ID) ->PTH.Optional[NamedNode]:
        """Search the namespace for the 1st part of `dottedName`, then that NS for the next part, etc. And return the "deepest" node, or None"""

        parts = dottedName.split('.',maxsplit=1) # parts is [<name>, (<name>.)*] parts[1] can be absent, parts[0] always exist
        node = self.findNode(parts[0])
        if len(parts) == 1:
            return node
        try:
            return node.search(parts[1])                              #type: ignore[union-attr] # Assume a NS, else raise
        except AttributeError: #node isn't a search'able/namespace --> Not found --> return None
            return None

    def find_byType(self, cls:type) ->dict[ID, NamedNode]:
        return {name: node for name, node in self._dict.items() if isinstance(node, cls)}

    def list_names(self) -> tuple[str]:
        return tuple(self._dict.keys())

@dataclass
class NamedSpace(NamedNode, _NameSpace):
    """A ``NamedSpace`` is a namedspace with a name ...."""



@dataclass
class Source_NS(NamedSpace):
    """This namespace is used for CCastle source files (so: *.Moat- & *.Castle-files). That filename is stored in ``source``"""
    _: KW_ONLY
    source       :PTH.Optional[str]=None

@dataclass
class _Target_NS(_NameSpace):
    """This ABSTARCT namespace is used to "store" AIGR-parts that will rendered into one *low-level* code-file.
       Typical, each Backend.Writer will subclass this class for the specifics for that language."""
    _: KW_ONLY
    target_file     :PTH.Optional[str]=None


@dataclass
class Scope(_NameSpace):
    """An body (```{ ....}```) has it own namespace, as it defines a scope. But many names (``ID``s) in that namespace
    are defines (registered) in an outer namespace . Therefore we have this special namespace *Scope* dataclass"""
    _: KW_ONLY
    outer_ns : _NameSpace

class _hasScope(Scope):
    """This Mixin adds a (sub)scope to an Class, and 'forward' the namespace-API to that scope-namespace
    Typical, the class to which this Mixin is added has a 'aigr.Body' but that is not mandatory"""

    def _register_parameters(self, post_init=False):
        """CONVINIANT FUNCTION: when `self` has parameters, register them in the scope.
           Usually called by __post_init__()"""

        if post_init:
            logger.debug(f"Auto register parameters -- post_init: {post_init}")
        if getattr(self, 'parameters', False):
            logger.debug(f"{type(self)} has parameters: self.parameters -- {self}")
            for p in self.parameters:
                self.register(p)

