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

       Raises TypeError when no matching Scaffolder exists."""

    _nodeCls: type = type(None)                                         # AutoScaffolder does not match any AIGR node
    _direct_map: PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]] = {} # node_cls -> scaffolder_cls; 1:1 permanent mapping

    def __new__(cls, node: AIGR) -> _Scaffolder:
        if not isinstance(node, AIGR): # defensive programming
            raise TypeError(f"AutoScaffolder requires an AIGR node, got {type(node).__name__!r}")

        scaffolder_cls = cls._find_for(type(node))
        return scaffolder_cls(node)

    @classmethod
    def _find_for(cls, node_cls: type[AIGR]) -> type[_Scaffolder]:
        """Return the most specific _Scaffolder subclass for node_cls.

           When we found a direct (1:1) earlier, we use it (it can never change).
           otherwise we search for it"""

        if node_cls in cls._direct_map:
            return cls._direct_map[node_cls]
        else:
            return cls._search(node_cls)

    @classmethod
    def _search(cls, node_cls: type[AIGR]) -> type[_Scaffolder]:
        """Walk node_cls.mro() to find the most specific matching Scaffolder."""
        scaffolders = cls.descendants_from(_Scaffolder, exclude=lambda s: issubclass(s, AutoScaffolder))

        for candidate_cls in node_cls.mro():
            for scaffolder in scaffolders:
                if scaffolder._nodeCls is candidate_cls:
                    if candidate_cls is node_cls:                            # 1:1 direct match -- safe to cache permanently
                        cls._direct_map[node_cls] = scaffolder
                    return scaffolder

        raise TypeError(f"No Scaffolder found for node type: {node_cls.__name__!r}")

    @classmethod
    def descendants_from(cls, base: type, *, exclude: None|PTH.Callable[[type], bool] = None) -> set[type]:
        """Return all descendants of base, optionally filtered by exclude predicate."""
        result = set()
        for sub in base.__subclasses__():
            if exclude and exclude(sub):
                continue
            result.add(sub)
            result |= cls.descendants_from(sub, exclude=exclude)
        return result
