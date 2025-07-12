# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field

from .dispatch_tables import _DispatchTable

from castle import aigr
from castle.aigr import ID

@dataclass
class EventDispatchTable(_DispatchTable):
    """An EventDispatchTable is, like any _DispatchTable, a mapping from incoming events (within a protocol) to a Eventhandler.

    .. note::

       An (event) dispatch-table is always for related to *one* (input) port. The kind of `Port` and the type of
       dispatch-table should match !

       .. important::

       For now, this relation is not completely modeled.

       * Possible we can use an (XLST/DOM alike) "parent/child" relation. (<node>/.., or ancestor(node)) of
         node.closest(<type>) in JS
       * Or, we can simple add a .port field (type: ID).

       For now, we use the .port:ID trick in _DispatchTable

    The aigr version is a data-structure (aka dataclass); it does not have (real) methods. There can be builders to created it.
    |BR|
    Similar, one can use wrappers to read it."""

    _: KW_ONLY
    map: PTH.Optional[dict[ID, str]] = dc_field(default_factory= lambda: dict())




##Oldau## @dataclass
##OLD## class EventDispatchTable(_DispatchTable):
##OLD##     """The EventDispatchTable maps port+event -> eventhandler. All 3 are IDs

##OLD##     Remember, the AIGR is a data-structure, it does not have "pointers"!
##OLD##     |BR|
##OLD##     Therefor a dispatch-table must IDs, which can be a dottedName or a mangled-name;
##OLD##     the later is typically used for an eventhandler.

##OLD##     Also notice, an ID can have `_Context`, like `Ref` which can "reference" to the real thing. (the 'Def' ID).
##OLD##     This may be used, but one should not thrust it

##OLD##     .. error:: See .../castle-aigr/designNotes/warning.html (BUSY on that)

##OLD##     """

##OLD##     def __init__(self, **kwargs):
##OLD##         super().__init__(**kwargs)
##OLD##         self._registration_byPort: Dict[ID, Dict[ID, ID]] = {} # Dict[port-name, Dict[event-name, handler-name]]

##OLD##     def __len__(self):
##OLD##         return sum(len(port_registrations) for port_registrations in self._registration_byPort.values())

##OLD##     def register_event(self, port_name:ID,  event_name:ID, handler_name:ID):
##OLD##         port_registration = self._registration_byPort.setdefault(port_name,{})
##OLD##         if port_registration.get(event_name):
##OLD##             logger.warning("Overwriting event-handler for port=%s, event=%s, becomes %s; was: %s",
##OLD##                             port_name, event_name, handler_name, port_registration.get(event_name))
##OLD##         else:
##OLD##             logger.debug("Register an event-handler for port=%s, event=%s :: %s", port_name, event_name, handler_name)
##OLD##         port_registration[event_name] = handler_name

##OLD##     def find_byNames(self, port_name:ID,  event_name:ID) -> ID|None:
##OLD##         """Return the registered event_name, or None"""
##OLD##         try:
##OLD##             port_registration = self._registration_byPort[port_name]
##OLD##             handler_name = port_registration[event_name]
##OLD##         except KeyError as err:
##OLD##             logger.debug("No event-handler for port=%s, event=%s; due KeyError: %s", port_name, event_name, err)
##OLD##             return None
##OLD##         return handler_name

##OLD##     def list_ports(self):
##OLD##         """Return all port-names, for which events are registered"""
##OLD##         return list(self._registration_byPort.keys())

##OLD##     def list_events_for_port(self, port_name:ID):
##OLD##         """Return all event-names, that are registered for the given port"""
##OLD##         try:
##OLD##             port_registration = self._registration_byPort[port_name]
##OLD##             return list(port_registration.keys())
##OLD##         except KeyError as err:
##OLD##             logger.debug("Nothing to list for port=%s; due KeyError: %s", port_name, err)
##OLD##             return ()# empty 'list'


# LocalWords:  eventhandler dottedName EventDispatchTable
