from .. import _debug

class CC_B_OutPort(_debug.DebugMixIn):

    def __init__(self):
        self.connection = None            # ref to a  CC_B_Component-subclass (the generated classes)
        self.handlers = []                # CC_B_eDispatchTable = list of CC_B_eventHandler(s)


    def _debug_attr_(self, name_only=True):
            if self.handlers:
                # RPython: .join for as loop does not work
                _str="["
                for n, h in enumerate(self.handlers):
                    _str += "%d:%s " % (n, _debug.handler_name(h))
                _str += "]"
            else:
                _str = "[]"
            return "connection=" + (self.connection._debug_() if self.connection else "NIL") + ", handlers=" + _str
