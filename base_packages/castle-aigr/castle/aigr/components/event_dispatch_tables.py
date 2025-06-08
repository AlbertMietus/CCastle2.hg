# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from .dispatch_tables import _DispatchTable

from castle import aigr
from castle.aigr import ID

##GAM: XXX/ToDo: Make it a dataclass. EventDispatchTable is part if the aigr, it shouldn't have (major) methods!!
class EventDispatchTable(_DispatchTable):
    """The EventDispatchTable maps port+event -> eventhandler. All 3 are IDs
    Remember, the AIGR is a data-structure, it does not have "pointers"!

    Therefor a dispatch-table must IDs, which can be a dottedName or a mangled-name;
    the later is typically used for an eventhandler.

    Also notice, an ID can have `_Context`, like `Ref` which can "reference" to the real thing. (the 'Def' ID).
    This may be used, but one should not thrust it."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._registration_byPort: Dict[ID, Dict[ID, ID]] = {} # Dict[port-name, Dict[event-name, handler-name]]

    def __len__(self):
        return sum(len(port_registrations) for port_registrations in self._registration_byPort.values())

    def register_event(self, port_name:ID,  event_name:ID, handler_name:ID):
        port_registration = self._registration_byPort.setdefault(port_name,{})
        if port_registration.get(event_name):
            logger.warning("Overwriting event-handler for port=%s, event=%s, becomes %s; was: %s",
                            port_name, event_name, handler_name, port_registration.get(event_name))
        else:
            logger.debug("Register an event-handler for port=%s, event=%s :: %s", port_name, event_name, handler_name)
        port_registration[event_name] = handler_name

    def find_byNames(self, port_name:ID,  event_name:ID) -> ID|None:
        """Return the registered event_name, or None"""
        try:
            port_registration = self._registration_byPort[port_name]
            handler_name = port_registration[event_name]
        except KeyError as err:
            logger.debug("No event-handler for port=%s, event=%s; due KeyError: %s", port_name, event_name, err)
            return None
        return handler_name

    def list_ports(self):
        """Return all port-names, for which events are registered"""
        return list(self._registration_byPort.keys())

    def list_events_for_port(self, port_name:ID):
        """Return all event-names, that are registered for the given port"""
        try:
            port_registration = self._registration_byPort[port_name]
            return list(port_registration.keys())
        except KeyError as err:
            logger.debug("Nothing to list for port=%s; due KeyError: %s", port_name, err)
            return ()# empty 'list'


# LocalWords:  eventhandler dottedName EventDispatchTable
