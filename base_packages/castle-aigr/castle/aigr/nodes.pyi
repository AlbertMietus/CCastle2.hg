# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.nodes``.
# Hand-maintained "manual autodoc" companion to nodes.py.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from . import AIGR as AIGR, AIGRNode as AIGRNode, ID as ID, Def as Def
from .aid import Argument as Argument

logger: PTH.Any

@dataclass
class NamedNode(AIGRNode):
    """An :class:`AIGRNode` that carries a ``name`` (the common base of named nodes).

    Pass the ``name`` as the first positional argument; a plain ``str`` is
    automatically wrapped into a defining :class:`ID` (``ID(name, Def())``).
    Most structural nodes (events, protocols, ports, components, ...) derive
    from this.
    """
    name: ID | str
    _: KW_ONLY
    parent: PTH.Optional[AIGR] = ...
    def __post_init__(self) -> None: ...

@dataclass
class Specialise(NamedNode):
    """A node that *specialises* another named node with concrete ``arguments``.

    Used for generics-like reuse: it points at the ``based_on`` node and the
    sequence of :class:`Argument` it is specialised with. When no name is given
    a descriptive one is synthesised.
    """
    _: KW_ONLY
    based_on: NamedNode
    arguments: PTH.Sequence[Argument]
    def __post_init__(self) -> None: ...
