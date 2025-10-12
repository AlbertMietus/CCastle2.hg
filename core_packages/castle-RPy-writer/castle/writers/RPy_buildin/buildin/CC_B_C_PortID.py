# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                 # Python TypeHints
Unspecified = PTH.Any  # Alias for parameters whose type is intentionally left vague

from .enums import CC_PortDirection
from .. import _debug


class CC_B_C_PortID(_debug.DebugMixIn):
    def __init__(self, name, portNo, protocol, direction, part_of):  # type: (Unspecified, Unspecified, Unspecified, CC_PortDirection|int, Unspecified) -> None
        self.name = name
        self.portNo = portNo
        self.protocol = protocol
        self._direction = direction
        self.part_of = part_of

    def _debug_attr_(self, name_only=True):
        return ( "name="          + self.name
                + ", portNo="     + str(self.portNo)
                + ", protocol="   + _debug._obj_name(self.protocol)
                + ", direction="  + self.direction_name
                + ", part_of="    + _debug._obj_name(self.part_of))

    @property
    def direction(self):  # type: () -> int
        return CC_PortDirection.to_number(self._direction)

    @property
    def direction_name(self): # type: () -> str
        return CC_PortDirection.to_string(self._direction)

