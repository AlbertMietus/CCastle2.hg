# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding._auto_scaffolder``.
# Hand-maintained "manual autodoc" companion to _auto_scaffolder.py.

import typing as PTH
from castle.aigr import AIGR as AIGR
from ._scaffolder import _Scaffolder as _Scaffolder

logger: PTH.Any

class AutoScaffolder(_Scaffolder):
    """Pick and build the most specific :class:`_Scaffolder` for any AIGR node.

    Use it exactly like a concrete scaffolder -- ``AutoScaffolder(node)`` -- but
    the returned instance is *never* an ``AutoScaffolder``: it is the most
    specific scaffolder subclass whose ``_nodeCls`` matches the node's type
    (resolved along the node's MRO, results cached). Raises ``TypeError`` when
    no scaffolder matches.
    """

    _nodeCls: type
    _direct_map: PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]]
    """Cache of exact node-type -> scaffolder-type matches."""
    _inherited_map: PTH.ClassVar[dict[type[AIGR], type[_Scaffolder]]]
    """Cache of node-type -> scaffolder-type matches found via the MRO."""

    def __new__(cls, node: AIGR) -> _Scaffolder: ...  # type: ignore[misc]

    @classmethod
    def descendants_from(cls, base: type[_Scaffolder], *, exclude: None | PTH.Callable[[type], bool] = ...) -> set[type[_Scaffolder]]:
        """Return all (recursive) subclasses of *base*, optionally filtered by *exclude*."""
        ...

    @classmethod
    def _resolve(cls, node_cls: type[AIGR]) -> type[_Scaffolder]:
        """Walk ``node_cls.mro()`` and return the most specific matching scaffolder class.

        This is the resolution hook; subclasses may override it (e.g. to spy on
        or alter look-up). Raises ``TypeError`` when nothing matches.
        """
        ...
