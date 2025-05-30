# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                 # Python TypeHints  - not for RPython
Unspecified = PTH.Any

from .enums import CC_ProtocolKind

from .. import _debug


class CC_B_Protocol(_debug.DebugMixIn):
    def __init__(self, name, parameters=None, inherit_from=None, base_arguments=None, kind=None, events=[]):  # type: (Unspecified, Unspecified, Unspecified, Unspecified, PTH.Optional[CC_ProtocolKind], Unspecified) -> None
        assert kind or inherit_from, "Either set kind, or use base-Protocol that has it"
        self.name = name
        self.parameters = parameters
        self.inherit_from = inherit_from
        self.base_arguments = base_arguments
        self._kind = kind if kind else self.inherit_from.kind
        self.events = events

    @property
    def length(self):
        return len(self.events)

    @property
    def kind(self): # type: () -> int
        k = self._kind if self._kind else self.inherit_from.kind
        if k is None: # Strange, but to be sure ...
            k = CC_ProtocolKind._unset
            logger.error("Protocol '%s' has None as kind, which strange; silently using '_unset' instead -- still strange", self.name)
        return CC_ProtocolKind.to_number(k)

    @property
    def kind_name(self): # type: () -> str
        k = self._kind
        return CC_ProtocolKind.to_string(k)

    def _debug_attr_(self, name_only=True):
        event_str = "[\n\t"
        for e in self.events:
            event_str += e._debug_(name_only=True)
        event_str +="]"
        return ("name="               + self.name
                + ", parameters="     + (repr(self.parameters) if not _debug.isRP else '<XXX_RP>')
                + ", inherit_from="   + _debug._obj_name(self.inherit_from)
                + ", base_arguments=" + (repr(self.base_arguments) if not _debug.isRP else '<XXX_RP>')
                + ", kind="           + self.kind_name
                + ", length="         + str(self.length)
                + ", events="         + event_str)


