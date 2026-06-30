# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.castle_actions``.
# Hand-maintained companion to castle_actions.py.

import typing as PTH
from .actions.names import Names
from .actions.parms_and_args import ParmsArgs
from .actions.protocols import Protocols
from .actions.components import Components
from .actions.meta import Meta
from .actions.literals import Literals
from .actions.files import Files
from .actions.body import Body

logger: PTH.Any


class DefaultActions:
    """Base TatSu semantic-action class providing a passthrough ``_default`` handler.

    Decorated with :func:`~.actions._debug.add_debug_logging` so every call
    emits a DEBUG log line.  ``_default`` is the fallback TatSu invokes for
    any grammar rule that has no dedicated handler in the actions object.
    """

    def _default(self, ast: PTH.Any) -> PTH.Any:
        """Return *ast* unchanged (identity fallback for unhandled grammar rules)."""
        ...


class CastleActions(
    DefaultActions,
    Names,
    ParmsArgs,
    Protocols,
    Components,
    Meta,
    Literals,
    Files,
    Body,
):
    """Composite TatSu semantics object that handles all Castle grammar rules.

    Combines every action mixin via multiple inheritance; each mixin maps a
    group of grammar rules to AIGR nodes.  This class is the single object
    passed to TatSu as ``parser.semantics``.

    The action mixins follow the Interface Segregation Principle: one mixin
    per grammar rule group.  The full rule groups are:

    * :class:`~.actions.Names`       -- identifiers and qualified references
    * :class:`~.actions.ParmsArgs`   -- parameters and arguments
    * :class:`~.actions.Protocols`   -- protocol and event definitions
    * :class:`~.actions.Components`  -- components, ports, handlers, methods
    * :class:`~.actions.Meta`        -- rewriter/meta rules (placeholder)
    * :class:`~.actions.Literals`    -- literal values
    * :class:`~.actions.Files`       -- top-level file rule
    * :class:`~.actions.Body`        -- statement bodies and void calls

    Normally constructed automatically inside :class:`~..castle_parser.CastleParser`;
    pass an explicit instance only when you need to customise action behaviour::

        from castle.readers.ladon.parser.castle_actions import CastleActions
        from castle.readers.ladon.parser.castle_parser import CastleParser

        parser = CastleParser(actions=CastleActions())
    """

    pass
