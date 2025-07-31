# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints

from castle.aigr import AIGR, AIGRNode

T = PTH.TypeVar("T", bound=AIGR)


class _Scaffolder(PTH.Generic[T]):
    __slots__ = ("_node",)
    _nodeCls = AIGR # Baseclass for node, set in SubClasses

    def __init__(self, node: T):
        if type(self) is _Scaffolder:
            raise TypeError("Only use subclasses of Scaffolder - e.f ScaffolderNode")
        if not isinstance(node, self._nodeCls):
            raise TypeError(f"Scaffolder can only wrap AIGR-subclasses of {self._nodeCls}, not {node}")
        self._node: T = node

    @property
    def node(self) -> T:
        return self._node

    def __getattr__(self, item: str) -> PTH.Any:
        """Delegate unknown attributes/methods to the real node."""
        return getattr(self._node, item)

    def __repr__(self):
        return f"<Scaffolder({self._node!r})>"



class ScaffolderNode(_Scaffolder):
    _nodeCls = AIGRNode

    def set_parent(self, parent: PTH.Union[_Scaffolder, AIGRNode]) -> _Scaffolder[T]:
        node = self.node
        parent_node = parent.node if isinstance(parent, _Scaffolder) else parent
        node.parent = parent_node
        return self  # for chaining
