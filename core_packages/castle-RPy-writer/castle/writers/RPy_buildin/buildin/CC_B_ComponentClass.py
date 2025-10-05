from .. import _debug

class CC_B_ComponentClass(_debug.DebugMixIn):
    """Describes the implemention of a Component; including the a dispatch table of all methods ("function pointers")"""

    def __init__(self, interface, methods=[], isa=None):
        self.interface = interface
        self.methods = methods
        self.isa = isa                   #Meta-class, for now: always None

    def _debug_attr_(self, name_only=True):
        if name_only:
            return _debug._obj_name(self.interface)
        else:
            return ("name="           + _debug._obj_name(self.interface)
                    + ", methods="   + "XXX"
                    + ", isa="       + str(self.isa))

