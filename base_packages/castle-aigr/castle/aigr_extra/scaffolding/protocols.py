# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from . import ScaffolderNode

class ScaffolderProtocol(ScaffolderNode):
    _nodeCls = aigr.Protocol
    # DataProtocol & StreamProtocol ...

class ScaffolderEventProtocol(ScaffolderProtocol):
    _nodeCls = aigr.EventProtocol

    """ XXX Moving methods from aigr.EventProtocol to Scaffolder... status: Just started (Copy/Past)"""


    #Note: ``.based_on`` can be an `EventProtocol`, or 'Specialise' (see Generics), which can have events.
    #    But it can also be another Protocol; typical ``_RootProtocol`` ...
    #    which has NO events, NOR the methods of EventProtocol!

    def eventIndex(self, event: aigr.Event) -> int:   # Is this needed?
        """Return the index-number (zero-bases) of the given `event`. (including inherited once)
           Scans the events in the 'based_on' protocol(s) also,"""
        # Note: the number can be higher as len(self.events)!

        if isinstance(self.node.based_on, aigr.EventProtocol):
            based_on = ScaffolderEventProtocol(self.node.based_on)
            try:
                return based_on.eventIndex(event)
            except ValueError: # not inherited
                pass 
            inherited_events = based_on._noEvents()
        else:
            inherited_events = 0 # No base
        return inherited_events + self.events.index(event)


    def _noEvents(self) ->int:
        """ (internal) find the total number of events (also inherit once)"""

        if isinstance(self.node.based_on, aigr.EventProtocol):
            based_on = ScaffolderEventProtocol(self.node.based_on)
            inherited = based_on._noEvents()
            logger.debug(f'{self.name} has inherited {inherited} events')
        else:
            inherited = 0

        no_events = inherited + len(self.node.events)
        logger.debug(f'{self.name} has {no_events} events (in total)')
        return no_events

