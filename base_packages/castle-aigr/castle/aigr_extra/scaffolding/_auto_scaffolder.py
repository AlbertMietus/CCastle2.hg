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

    _direct_map:    PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]] = {} # node_cls -> scaffolder_cls; 1:1 permanent mapping
    _inherited_map: PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]] = {} 


    def __new__(cls, node: AIGR) -> _Scaffolder:  # type: ignore[misc]
        if not isinstance(node, AIGR):                                  # defensive programming
            raise TypeError(f"AutoScaffolder requires an AIGR node, got {type(node).__name__!r}")
        return cls._scaffolder_for(node)(node)



    @classmethod
    def _scaffolder_for(cls, node: AIGR) -> type[_Scaffolder]:
        """Return the scaffolder class for node.

           Use the maps, as a cache, or resolve() -- and update the cache"""
        node_cls = type(node)

        try:
            return cls._direct_map[node_cls]
        except KeyError:
            pass
        try:
            return cls._inherited_map[node_cls]
        except KeyError:
            scaffolder = cls._resolve(node_cls)
            if scaffolder._nodeCls is node_cls:
                cls._direct_map[node_cls] = scaffolder
            else:
                cls._inherited_map[node_cls] = scaffolder
        return scaffolder





        
    @classmethod
    def _resolve(cls, node_cls: type[AIGR]) -> type[_Scaffolder]:
        """Walk node_cls.mro() to find the most specific matching Scaffolder."""

        scaffolders: dict[type, type[_Scaffolder]]
        scaffolders = {s._nodeCls: s for s in cls.descendants_from(_Scaffolder, exclude=lambda s: issubclass(s, AutoScaffolder))}

        for candidate_cls in node_cls.mro():
            if candidate_cls in scaffolders:
                return scaffolders[candidate_cls]

        raise TypeError(f"No Scaffolder found for node type: {node_cls.__name__!r}")

    @classmethod
    def descendants_from(cls, base: type[_Scaffolder], *, exclude: None|PTH.Callable[[type], bool] = None) -> set[type[_Scaffolder]]:
        """Return all descendants of base, optionally filtered by exclude predicate."""
        result = set()
        for sub in base.__subclasses__():
            if exclude and exclude(sub):
                continue
            result.add(sub)
            result |= cls.descendants_from(sub, exclude=exclude)
        return result
