from .. import _debug


class CC_B_C_PortID(_debug.DebugMixIn):
    def __init__(self, name, portNo, protocol, direction, part_of):
        self.name = name
        self.portNo = portNo
        self.protocol = protocol
        self.direction = direction
        self.part_of = part_of

    def _debug_attr_(self, name_only=True):
        return ( "name="          + self.name
                + ", portNo="     + str(self.portNo)
                + ", protocol="   + _debug._obj_name(self.protocol)
                + ", direction="  + self.direction_name
                + ", part_of="    + _debug._obj_name(self.part_of))

    @property
    def direction_name(self):
        dir = self.direction
        for name,_int in PortDirection.items():
            if dir == _int: return name
        return "<error>"


CC_B_PortDirectionIs_UNKNOW   = 0 # Error
CC_B_PortDirectionIs_in       = 1
CC_B_PortDirectionIs_out      = 2
CC_B_PortDirectionIs_bidirect = 3 # No yet supported
CC_B_PortDirectionIs_master   = 4 # No yet supported
CC_B_PortDirectionIs_slave    = 5 # No yet supported

PortDirection = {
    'CC_B_PortDirectionIs_UNKNOW'   : CC_B_PortDirectionIs_UNKNOW,
    'CC_B_PortDirectionIs_in'       : CC_B_PortDirectionIs_in,
    'CC_B_PortDirectionIs_out'      : CC_B_PortDirectionIs_out,
    'CC_B_PortDirectionIs_bidirect' : CC_B_PortDirectionIs_bidirect,
    'CC_B_PortDirectionIs_master'   : CC_B_PortDirectionIs_master,
    'CC_B_PortDirectionIs_slave'    : CC_B_PortDirectionIs_slave,
    }
