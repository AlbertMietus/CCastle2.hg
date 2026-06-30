# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.base.AIGR``.
# Hand-maintained "manual autodoc" companion to AIGR.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY

@dataclass
class AIGR:
    """Abstract root of the *Abstract Intermediate Graph Representation*.

    Every node the compiler manipulates is (eventually) an ``AIGR``. It is
    abstract on purpose: instantiating ``AIGR`` directly raises
    ``NotImplementedError`` -- always build a concrete subclass
    (e.g. :class:`AIGRNode`, ``ID``, an expression or statement node).
    """

    def __new__(cls, *args: PTH.Any, **kwargs: PTH.Any) -> AIGR: ...

@dataclass
class AIGRNode(AIGR):
    """An ``AIGR`` that lives in the tree and therefore has a ``parent``.

    Most structural nodes derive from this. The ``parent`` link is the one
    generic edge every node shares; the node's own data-fields hold its
    children. ``parent`` is keyword-only and defaults to ``None`` (set later,
    e.g. by the scaffolding tools).
    """

    _: KW_ONLY
    parent: PTH.Optional[AIGR] = ...
    """The single structural parent of this node (``None`` until linked)."""
