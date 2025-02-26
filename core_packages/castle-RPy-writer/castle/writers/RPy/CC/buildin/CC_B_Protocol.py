from .. import _debug

class CC_B_Protocol(_debug.DebugMixIn):
    def __init__(self, name, parameters=None, inherit_from=None, base_arguments=None, kind=None, events=[]):
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
    def kind(self):
        return self._kind if self._kind else self.inherit_from.kind

    @property
    def kind_name(self):
        kind = self.kind
        for name,_int in ProtocolKind.items():
            if kind == _int: return name
        return "<error>"


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

CC_B_ProtocolKindIs_Unknown = 0
CC_B_ProtocolKindIs_Event   = 1
CC_B_ProtocolKindIs_Data    = 2
CC_B_ProtocolKindIs_Stream  = 3
#...

ProtocolKind = {
    'CC_B_ProtocolKindIs_Unknown' : CC_B_ProtocolKindIs_Unknown,
    'CC_B_ProtocolKindIs_Event'   : CC_B_ProtocolKindIs_Event,
    'CC_B_ProtocolKindIs_Data'    : CC_B_ProtocolKindIs_Data,
    'CC_B_ProtocolKindIs_Stream'  : CC_B_ProtocolKindIs_Stream,
    }
