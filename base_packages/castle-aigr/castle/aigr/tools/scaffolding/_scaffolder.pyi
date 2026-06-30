# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding._scaffolder``.
# Hand-maintained "manual autodoc" companion to _scaffolder.py.

import typing as PTH
from castle.aigr import AIGR as AIGR

logger: PTH.Any

class _Scaffolder:
    """Abstract base wrapper around an AIGR node, adding tooling behaviour.

    A scaffolder *wraps* a node (``.node``) and transparently delegates any
    unknown attribute/method to it, so a wrapped node can be used almost like
    the node itself while gaining the scaffolding API (tree walking, name
    registration, ...). Do not instantiate ``_Scaffolder`` directly -- use a
    concrete subclass (e.g. :class:`ScaffolderNode`) or
    :class:`AutoScaffolder`.
    """

    _nodeCls: type
    """The AIGR base class a subclass is allowed to wrap (checked in ``__init__``)."""

    __slots__: PTH.ClassVar[tuple[str, ...]]

    def __init__(self, node: AIGR) -> None: ...

    @property
    def node(self) -> PTH.Any:
        """The wrapped (real) AIGR node."""
        ...

    def __getattr__(self, item: str) -> PTH.Any:
        """Delegate unknown attributes/methods to the wrapped node."""
        ...

    def auto_register(self) -> None:
        """Auto-register this node's details (e.g. names). Default: do nothing.

        Concrete scaffolders override this to register parameters, handlers, etc.
        """
        ...
