# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle.aigr import AIGR

T = PTH.TypeVar("T", bound=AIGR)                            # pragma: no mutate

class _Scaffolder(PTH.Generic[T]):
    _nodeCls = AIGR                                         # Baseclass for node, set in SubClasses
    __slots__ = ("_node",)                                  # pragma: no mutate

    def __init__(self, node: T):
        if type(self) is _Scaffolder:
            raise TypeError("Only use subclasses of Scaffolder - e.f ScaffolderNode")
        if not isinstance(node, self._nodeCls):
            raise TypeError(f"{self.__class__.__name__} can only wrap AIGR-subclasses of {self._nodeCls}, not {node}")
        self._node: T = node

    @property
    def node(self) -> T:
        return self._node

    def __getattr__(self, item: str) -> PTH.Any:
        """Delegate unknown attributes/methods to the real node."""
        return getattr(self._node, item)

    def __repr__(self):
        return f"<Scaffolder({self._node!r})>"                         # pragma: no mutate



