# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy.aigr.dispatch_tables``.

import typing as PTH
from dataclasses import dataclass, KW_ONLY
from castle.aigr import AIGR, ID
from castle.aigr.tools.scaffolding._scaffolder import _Scaffolder

ProtocolName: PTH.TypeAlias = ID
"""Type alias: the name of a Castle protocol."""
EventName: PTH.TypeAlias = ID
"""Type alias: the name of a Castle event."""
HandlerName: PTH.TypeAlias = ID
"""Type alias: the name of the event-handler method."""

@dataclass
class _DispatchTable(AIGR):
    """Base class for writer-internal dispatch tables.

    A dispatch table maps *triggers* (event identifiers on a specific port) to
    the handler that processes them.  This information is available in the AIGR
    (via ``ComponentImplementation.handlers``), but is reorganised here for
    convenient code generation.

    These nodes are temporary: they are created during rendering and are not
    part of the persistent AIGR tree.
    """

    _: KW_ONLY
    comp: ID
    """Name of the component that owns this table."""
    port: ID
    """Name of the port this table belongs to."""
    map: PTH.Mapping[PTH.Any, PTH.Any]
    """The trigger -> handler mapping (see concrete subclasses for key/value types)."""
    parentTable: PTH.Optional[ID]
    """Reference to the parent table for inherited handlers (``None`` = no parent)."""


@dataclass
class EventDispatchTable(_DispatchTable):
    """Dispatch table for event handlers.

    Maps ``(ProtocolName, EventName)`` pairs to ``HandlerName``.  Built from a
    ``ComponentImplementation``'s event-handler list by
    :func:`Build_EventDispatchTable`.
    """

    _: KW_ONLY
    map: PTH.Mapping[tuple[ProtocolName, EventName], HandlerName]


class DispatchTable_Scaffolder(_Scaffolder):
    """Scaffolder wrapper for :class:`_DispatchTable` nodes."""
    _nodeCls: type


class EventDispatchTable_Scaffolder(DispatchTable_Scaffolder):
    """Scaffolder wrapper for :class:`EventDispatchTable` nodes."""
    _nodeCls: type


def Build_EventDispatchTable(
    comp: PTH.Any,
    port_name: ID,
) -> EventDispatchTable_Scaffolder:
    """Build an :class:`EventDispatchTable` for *port_name* on *comp*.

    Collects every :class:`castle.aigr.EventHandler` in ``comp.handlers``
    whose port matches *port_name* and assembles a
    ``(protocol, event) -> handler_name`` map.

    Parameters
    ----------
    comp:
        A ``castle.aigr.ComponentImplementation`` node.
    port_name:
        The :class:`ID` of the port to build the table for.

    Returns
    -------
    EventDispatchTable_Scaffolder
        A scaffolded dispatch-table ready for the Machinery renderer.

    Note
    ----
    ``parentTable`` is currently hard-coded to ``None`` (WIP).
    """
    ...
