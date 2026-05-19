# (C) Albert Mietus 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle.aigr import AIGR
from ._scaffolder import _Scaffolder


class AutoScaffolder(_Scaffolder):
    """Finds and returns the most specific Scaffolder for a given AIGR node.

       Usage is identical to any concrete Scaffolder::

           wrapped = AutoScaffolder(node)

       The returned instance is never an AutoScaffolder -- it is the most specific
       _Scaffolder subclass whose ``_nodeCls`` matches the node's type, following
       the node's MRO for specificity.

       Raises TypeError when no matching Scaffolder exists. """

    _nodeCls:type  = type(None) # AutoScaffolder does not mach any AIGR node
    _direct_map: PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]] = {}

    def __new__(cls, node: AIGR) -> _Scaffolder:
        if not isinstance(node, AIGR):
            raise TypeError(f"AutoScaffolder requires an AIGR node, got {type(node).__name__!r}")

        scaffolder_cls = cls._find_for(type(node))
        return scaffolder_cls(node)

    @classmethod
    def _find_for(cls, node_cls: type) -> type[_Scaffolder]:
        """Return the most specific _Scaffolder subclass for node_cls.

        Checks the 1:1 cache first. On a miss, walks node_cls.mro() and caches
        the result when a direct match is found (scaffolder._nodeCls is node_cls).
        """
        if node_cls in cls._direct_map:
            return cls._direct_map[node_cls]

        for candidate_cls in node_cls.mro():
            for scaffolder in cls._collect_scaffolders():
                if scaffolder._nodeCls is candidate_cls:
                    if candidate_cls is node_cls:        # 1:1 direct match -- safe to cache permanently
                        cls._direct_map[node_cls] = scaffolder
                    return scaffolder

        raise TypeError(f"No Scaffolder found for node type: {node_cls.__name__!r}")

    @classmethod
    def _collect_scaffolders(cls) -> list[type[_Scaffolder]]:
        """Return all concrete _Scaffolder subclasses, excluding AutoScaffolder."""

        #return [s for s in cls._all_subclasses(_Scaffolder) if s is not cls]
        return [s for s in cls._all_subclasses(_Scaffolder) if not issubclass(s, AutoScaffolder)]
    
    @classmethod
    def _all_subclasses(cls, root: type) -> set[type]:
        """Recursively collect all subclasses of root."""
        result = set(root.__subclasses__())
        for sub in list(result):
            result |= cls._all_subclasses(sub)
        return result
