# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This file contains AIGR-classes to model (all kind of) NameSpaces.

There are several NameSpaces: the most prominent one is the ``Source_NS``, roughly the file that contains the (Castle) code.
"""
from __future__ import annotations

__all__ = ['NameSpace', 'Source_NS']

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .nodes import NamedNode, NameError, ID

from . import AIGR, _Marker


@dataclass
class NameSpace(NamedNode):
    """This models a namespace (like a file, see ``Source_NS``).

    It contained *"named nodes"* that should be :method:`register()`ed and can be found by :method:`getID()` and/or :method:`findNode()`.

    XXX More"""

    _: KW_ONLY
    _dict      :PTH.Dict[ID, NamedNode]=dc_field(init=None, default_factory=lambda: dict()) #type: ignore[call-overload]

    def register(self, named_node :NamedNode, asName:PTH.Optional[ID|str]=None):
        name = ID(asName) if asName else PTH.cast(ID, named_node.name)

        if name in self._dict:
            old = self._dict[name]
            logger.warning(f"The '{name}'-node is already in this namespace; -- it will be lost." +
                           f"Removed: {old}. New: {named_node}")
        self._dict[name] = named_node
        self._register_2ways(named_node)

    def _register_2ways(self, node):
        node.register_in_NS(self)
###
### The following 3 methods are overkill.
### + findNode/getID only lock locally returning None (findNode) or raise NameError on no match
### + search is like findNode, but looks also in subNS'ses
###
### So,
### - ``NS.findNode(name)`` and ``NS.search(name)`` are equivalent
###     (but search calls findNode, and can't be removed. find is also a better name)
###- There is no getID() for dottedName's
###


    def findNode(self, name :ID|str) ->PTH.Optional[NamedNode]:
        """Return the NamedNode with the specified name (aka ID), or None.
           See :method:`getID` for an alternative"""
        if not isinstance(name, ID): name=ID(name)
        return self._dict.get(name, None)


    def getID(self, name :ID) ->NamedNode: #Or raise NameError
        """Return the NamedNode with the specified name (aka ID), or raised an NameError:AttributeError.
           See :method:`findNode` for an alternative"""
        node = self.findNode(name)
        if node is None:
            raise NameError(f"No node named {name} in NS:{self.name}")
        return node

    def search(self, dottedName :ID) ->PTH.Optional[NamedNode]:
        """Search the namespace for the 1st part of `dottedName`, then that NS for the next part, etc. And return the "deepest" node, or None"""

        parts = dottedName.split('.',maxsplit=1) # parts is [<name>, (<name>.)*] parts[1] can be absent, parts[0] always exist
        node = self.findNode(parts[0])
        if len(parts) == 1:
            return node
        try:
            return node.search(parts[1])                              #type: ignore[union-attr] # Assume a NS, else raise
        except AttributeError: #node isn't a search'able/NameSpace --> Not found --> return None
            return None

    def find_byType(self, cls:type) ->dict[ID, NamedNode]:
        return {name: node for name, node in self._dict.items() if isinstance(node, cls)}

    def all_NS(self) ->dict[ID, NamedNode]:
        return self.find_byType(NameSpace)


@dataclass
class Source_NS(NameSpace):
    _: KW_ONLY
    source       :PTH.Optional[str]=None
