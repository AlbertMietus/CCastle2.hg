# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.readers.ladon.parser.actions.components``.
# Hand-maintained companion to components.py.

import typing as PTH
from castle import aigr

logger: PTH.Any


class Components:
    """TatSu semantic-action mixin for Castle component, port, and handler rules.

    Mixed into :class:`~..castle_actions.CastleActions`; maps the grammar
    rules ``component_definition``, ``implement_component``, ``port_line``,
    ``port_direction``, ``event_handler``, and ``method`` to their AIGR
    counterparts.
    """

    def component_definition(self, ast: PTH.Any) -> aigr.ComponentInterface:
        """Reduce ``component_definition``: return a :class:`~castle.aigr.ComponentInterface`."""
        ...

    def implement_component(self, ast: PTH.Any) -> aigr.ComponentImplementation:
        """Reduce ``implement_component``: return a :class:`~castle.aigr.ComponentImplementation`.

        Calls :meth:`_implement_component_addLocals` to register local
        functions and members in the component's scope.
        """
        ...

    def _implement_component_addLocals(
        self,
        wrapped_comp: PTH.Any,
        ast: PTH.Any,
    ) -> None:
        """Register local functions and members into *wrapped_comp*'s namespace."""
        ...

    def port_line(self, ast: PTH.Any) -> aigr.Port:
        """Reduce ``port_line``: return a :class:`~castle.aigr.Port`."""
        ...

    def port_direction(self, ast: PTH.Any) -> aigr.PortDirection:
        """Reduce ``port_direction``: parse the direction string and return the matching enum value."""
        ...

    def event_handler(self, ast: PTH.Any) -> aigr.EventHandler:
        """Reduce ``event_handler``: return an :class:`~castle.aigr.EventHandler`.

        Mangles the protocol/event/port triple via
        ``castle.aigr_extra.blend.mangle_event_handler`` to produce the
        handler's canonical AIGR name.
        """
        ...

    def method(self, ast: PTH.Any) -> aigr.Method:
        """Reduce ``method``: return a :class:`~castle.aigr.Method`."""
        ...

    def _callable(self, callable: PTH.Any, ast: PTH.Any) -> PTH.Any:
        """Post-process a callable node: run auto_register() via its scaffolder."""
        ...
