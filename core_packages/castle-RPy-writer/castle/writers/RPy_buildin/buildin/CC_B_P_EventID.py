from .. import _debug

class CC_B_P_EventID(_debug.DebugMixIn):
    def __init__(self, name, seqNo, parameters=[], part_of=None):
        self.name = name
        self.seqNo = seqNo
        self.parameters=parameters
        self.part_of = part_of

