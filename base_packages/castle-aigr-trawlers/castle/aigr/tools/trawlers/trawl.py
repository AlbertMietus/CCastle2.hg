# (C) Albert Mietus, 2026. Part of Castle/CCastle project

from __future__ import annotations
import typing as PTH                                                                                  # Python TypeHints

from castle.aigr import AIGR, AIGRNode


class Trawl:
    """Fluent navigation for AIGR(Node) trees."""

    def __init__(self, node: AIGR) -> None:
        self._nodes: tuple[AIGR, ...] = (node,)

    @classmethod
    def _of(cls, nodes: tuple[AIGR, ...]) -> Trawl:
        "private factory"
        instance = cls.__new__(cls)
        instance._nodes = nodes
        return instance

    def exists(self) -> bool:
        return bool(self._nodes)

    def one(self) -> PTH.Optional[AIGR]:
        return self._nodes[0] if self._nodes else None

    def all(self) -> tuple[AIGR, ...]:
        return self._nodes

    def up(self, steps: int = 1) -> Trawl:
        nodes = self._nodes
        for _ in range(steps):
            nodes = _step_up(nodes)
        return Trawl._of(nodes)


def _step_up(nodes: tuple[AIGR, ...]) -> tuple[AIGR, ...]:
    return tuple(
        n.parent for n in nodes
        if isinstance(n, AIGRNode) and n.parent is not None
    )
