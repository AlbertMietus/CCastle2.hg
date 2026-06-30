# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.protocols``.
# Hand-maintained "manual autodoc" companion to protocols.py.

import typing as PTH
from castle import aigr as aigr
from . import ScaffolderNode as ScaffolderNode

logger: PTH.Any

class ScaffolderProtocol(ScaffolderNode):
    """Scaffolder for a :class:`castle.aigr.protocols.Protocol`.

    Knows how to follow the ``based_on`` link (transparently stepping through a
    :class:`castle.aigr.Specialise`) to the base protocol of the *same* type.
    """

    _nodeCls: type
    _link_fields: frozenset[str]
    _attr_fields: frozenset[str]

    def wrapped_base(self) -> PTH.Optional[ScaffolderProtocol]:
        """Return the (same-typed) base protocol wrapped in a scaffolder, or ``None``."""
        ...

class ScaffolderEventProtocol(ScaffolderProtocol):
    """Scaffolder for a :class:`castle.aigr.protocols.EventProtocol`.

    Adds event indexing that accounts for inherited events from ``based_on``
    protocols.
    """

    _nodeCls: type
    _kids_fields: frozenset[str]

    def eventIndex(self, event: aigr.Event) -> int:
        """Return the zero-based index of *event*, counting inherited events first.

        Raises ``ValueError`` if the event is not part of this protocol chain.
        """
        ...

    def _noEvents(self) -> int:
        """Total number of events in this protocol, including inherited ones."""
        ...
