# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub (signatures + usage docs) for ``castle.aigr.tools.scaffolding.components``.
# Hand-maintained "manual autodoc" companion to components.py.

import typing as PTH
from castle import aigr as aigr
from castle.aigr import ID as ID
from .namespaces import ScaffolderNameSpace as ScaffolderNameSpace

logger: PTH.Any

class ScaffolderComponentImplementation(ScaffolderNameSpace):
    """Scaffolder for a :class:`castle.aigr.statements.ComponentImplementation`.

    Adds event-handler registration: handler names are *not* stored in the
    component namespace, but each handler's ``outer_ns`` is linked to the
    component on :meth:`auto_register`.
    """

    _nodeCls: type
    _kids_fields: frozenset[str]
    _attr_fields: frozenset[str]
    _link_fields: frozenset[str]

    def register_EventHandler(self, node: aigr.EventHandler, asName: PTH.Optional[ID | str] = ...) -> None:
        """Append an :class:`EventHandler` to the component's ``handlers`` list."""
        ...

    def auto_register(self) -> None:
        """Link every handler's ``outer_ns`` to this component (see :meth:`auto_register_handlers`)."""
        ...

    def auto_register_handlers(self) -> None:
        """Set ``outer_ns`` of each handler to the wrapped component. Do not call directly."""
        ...
