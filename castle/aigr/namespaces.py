# (C) Albert Mietus, 2023. Part of Castle/CCastle project

"""This file contains AIGR-classes to model (all kind of) NameSpaces.

There are several NameSpaces: the most prominent one is the ``Source_NS``, roughly the file that contains the (Castle) code.
"""
from __future__ import annotations

__all__ = ['NameSpace', 'Source_NS', 'GENERATED']

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field


from . import AIGR, _Marker

class GENERATED(_Marker):pass


class NamedNode(AIGR): pass # Move up, name:str is part of it
class NameError(AttributeError):pass

@dataclass
class NameSpace(AIGR):
    """This models a namespace (like a file, see ``Source_NS``).

    It contained *"named nodes"* that should be :method:`register()`ed and can be found by :method:`getID()` and/or :method:`findNode()`.

    XXX More"""

    name       :str
    _: KW_ONLY
    _dict      :dict=dc_field(init=None, default_factory=lambda: dict())

    def register(self, named_node :NamedNode):
        name = named_node.name
        if name in self._dict:
            old=self._dict[name]
            logger.warning(f"The '{name}'-node is already in this namespace; -- it will be lost." +
                           f"Removed: {old}. New: {named_node}")

        self._dict[name] = named_node
        named_node.ns = self


    def findNode(self, name :str) ->PTH.Optional(NamedNode):
        """Return the NamedNode with the specified name (aka ID), or None.
           See :method:`getID` for an alternative"""
        return self._dict.get(name, None)


    def getID(self, name :str) ->NamedNode: #Or raise NameError
        """Return the NamedNode with the specified name (aka ID), or raised an NameError:AttributeError.
           See :method:`findNode` for an alternative"""
        node = self.findNode(name)
        if node is None:
            raise NameError(f"No node named {name} in NS:{self.name}")
        return node

    def search(self, dottedName :str) ->PTH.Optional(NamedNode):
        """Search the namespace for the 1st part of `dottedName`, then that NS for the next part, etc. And return the "deepest" node, or None"""

        parts = dottedName.split('.',maxsplit=1) # parts is [<name>, (<name>.)*] parts[1] can be absent, parts[0] always exist
        node = self.findNode(parts[0])
        if len(parts) == 1:
            return node
        try:
            return node.search(parts[1])
        except AttributeError: #node isn't a search'able/NameSpace --> Not found --> return None
            return none

@dataclass
class Source_NS(NameSpace):
    _: KW_ONLY
    source       :str
