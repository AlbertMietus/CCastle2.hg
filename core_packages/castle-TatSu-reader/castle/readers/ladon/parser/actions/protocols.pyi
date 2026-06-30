# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.protocols``.
# Hand-maintained companion to protocols.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class Protocols:
    """TatSu semantic-action mixin for Castle protocol and event-definition rules.

    Mixed into :class:`~..castle_actions.CastleActions`; handles the
    ``event_definition`` and ``event_protocol`` grammar rules.
    """

    def event_definition(self, ast: PTH.Any) -> aigr.Event:
        """Reduce ``event_definition``: return an :class:`~castle.aigr.Event`."""
        ...

    def event_protocol(self, ast: PTH.Any) -> aigr.EventProtocol:
        """Reduce ``event_protocol``: return an :class:`~castle.aigr.EventProtocol`.

        Raises ``AssertionError`` if the protocol carries typed parameters
        (not yet supported in AIGR).
        """
        ...
