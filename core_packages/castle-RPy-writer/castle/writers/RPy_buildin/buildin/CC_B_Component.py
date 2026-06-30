from .. import _debug

class CC_B_Component(_debug.DebugMixIn):
    """"This is the 'not generated' base-class of all generated clases"""
    def __init__(self, isa):
        self.isa = isa

    def _debug_attr_(self, name_only=True):
        # Same order as __init__
        # Don't call _debug.DebugMixIn._debug_attr_
        return ("isa="  + self.isa._debug_(name_only=name_only))

    def _castle_init(self, *args):
        """This function is called by __init__, and holds the code of CastleCode's init"""
        pass

    def _debug_name(self):
        return 'isa.interface->' + self.isa.interface._debug_name()


