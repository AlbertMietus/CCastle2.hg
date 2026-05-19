# (C) Albert Mietus 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle.aigr import AIGR
from ._scaffolder import _Scaffolder


class AutoScaffolder(_Scaffolder):
    """Finds and returns the most specific Scaffolder for a given AIGR node.

    Usage is identical to any concrete Scaffolder::

        wrapped = AutoScaffolder(node)

    The returned instance is never an AutoScaffolder -- it is the most specific
    _Scaffolder subclass whose ``_nodeCls`` matches the node's type, following
    the node's MRO for specificity.

    Raises TypeError when no matching Scaffolder exists.
    """

    def __new__(cls, node: AIGR) -> _Scaffolder:
        if not isinstance(node, AIGR):
            raise TypeError(f"AutoScaffolder requires an AIGR node, got {type(node).__name__!r}")

        scaffolder_cls = _find_for(type(node))
        return scaffolder_cls(node)


def _find_for(node_cls: type) -> type[_Scaffolder]:
    """Return the most specific _Scaffolder subclass for node_cls.

    Walks node_cls.mro() in order -- most specific first -- and returns
    the first Scaffolder that declares that exact type as its _nodeCls.
    Skips AutoScaffolder itself.
    """
    all_scaffolders = _collect_scaffolders()

    for candidate_cls in node_cls.mro():
        for scaffolder in all_scaffolders:
            if scaffolder._nodeCls is candidate_cls:
                return scaffolder

    raise TypeError(f"No Scaffolder found for node type: {node_cls.__name__!r}")


def _collect_scaffolders() -> list[type[_Scaffolder]]:
    """Return all concrete _Scaffolder subclasses, excluding AutoScaffolder."""
    return [
        cls for cls in _all_subclasses(_Scaffolder)
        if cls is not AutoScaffolder
    ]


def _all_subclasses(cls: type) -> set[type]:
    """Recursively collect all subclasses of cls."""
    result = set(cls.__subclasses__())
    for sub in list(result):
        result |= _all_subclasses(sub)
    return result
