# (C) Albert Mietus 2025,2026 Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from . import ScaffolderNode

class ScaffolderProtocol(ScaffolderNode):
    _nodeCls:type = aigr.Protocol
    _link_fields: frozenset[str] = frozenset({'based_on'})
    _attr_fields: frozenset[str] = frozenset({'typedParameters'})

    def wrapped_base(self) -> PTH.Optional["ScaffolderProtocol"]:
        wrapCls=type(self)
        based_on = self.node.based_on
        if isinstance(based_on, aigr.Specialise):                            ### XXX I dont't like this
            based_on = based_on.based_on

        # Only wrap when base_on has same type as the wrapped type
        wrapped = wrapCls(based_on) if (type(based_on) is type(self.node)) else None
        logger.debug("wrapCls=%s, wrapped: %s (return) -- base_on: %s; self: %s", wrapCls, wrapped, based_on, self)
        return wrapped


class ScaffolderEventProtocol(ScaffolderProtocol):
    #_nodeCls: PTH.Type = aigr.EventProtocol
    _nodeCls = aigr.EventProtocol
    _kid_fields: frozenset[str] = frozenset({'events'})

    #Note: ``.based_on`` can be an `EventProtocol`, or 'Specialise' (see Generics), which can have events.
    #    But it can also be another Protocol; typical ``_RootProtocol`` ...
    #    which has NO events, NOR the methods of EventProtocol!

    def eventIndex(self, event: aigr.Event) -> int:  # Or ValueError
        """Return the index-number (zero-bases) of the given `event`. (including inherited once)
           Scans the events in the 'based_on' protocol(s) also,"""
        # Note: the number can be higher as len(self.events)!

        wrapped_base = self.wrapped_base() # Can be None -> AttributeError below -> no inherited events
        try:
            return wrapped_base.eventIndex(event)                             # type: ignore [union-attr]
        except AttributeError: # No .eventIndex
            inherited_events = 0
        except ValueError: # `event` is not inherited
            inherited_events = wrapped_base._noEvents()                            # type: ignore [union-attr]

        return inherited_events + self.node.events.index(event) # Or ValueError


    def _noEvents(self) ->int:
        """ (internal) find the total number of events (also inherit once)"""

        wrapped_base = self.wrapped_base() # Can be None -> AttributeError below -> no inherited events
        try:
            inherited_events = wrapped_base._noEvents() # type: ignore [union-attr]
        except AttributeError as e: #  No ._noEvents()
            logger.info("AttributeError: %s -- wrapped_base: %s ", e, wrapped_base )
            inherited_events = 0
        logger.debug(f'{self.name} has inherited {inherited_events} events')
        no_events = inherited_events + len(self.node.events)
        logger.debug(f'{self.name} has {no_events} events (in total)')
        return no_events

