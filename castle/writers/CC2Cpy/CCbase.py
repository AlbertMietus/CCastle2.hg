# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project


from typing import TypeAlias, ClassVar, Optional
from dataclasses import dataclass, field as dc_field, KW_ONLY
from collections.abc import Sequence # Use for typing

from castle.auxiliary.abcd import ABCD

from enum import Enum


class CC_Base: pass

@dataclass
class CC_TypedParameter(CC_Base):
    """This is many a helper class/struct to combine a parameter: a name and an type"""
    name: str
    type: type


CC_TypedParameterTuple: TypeAlias = Sequence[CC_TypedParameter]

class CC_PortDirection(Enum):
    CC_B_PortDirectionIs_UNKNOWN  = Unknown   = 0
    CC_B_PortDirectionIs_in       = In        = 1
    CC_B_PortDirectionIs_out      = Out       = 2
    CC_B_PortDirectionIs_bidirect = BiDir     = 3 # Not supported yet
    CC_B_PortDirectionIs_master   = Master    = 4 # Not supported yet
    CC_B_PortDirectionIs_slave    = Slave     = 5 # Not supported yet

    def portray_name(self):                                                        ### CC_B_PortDirectionIs_{self.name}'
        return f'{self.name}'

@dataclass
class CC_Port(CC_Base):
    name: str
    _ : KW_ONLY
    direction: CC_PortDirection =  CC_PortDirection.Unknown
    type: type

    def portray_name(self) ->str:                                           ### <port name>
        return f'{self.name}'

    def portray_typePtr(self) ->str:                                           ### <port type> e.g a protocol
        if isinstance(self.type, CC_Base):
            return f'&{self.type.portray_name()}'
        elif self.type is None:
            return "NULL"
        else:
            from warnings import warn
            tn = self.type if isinstance(self.type, str) else self.type.__name__
            warn(f"Using string (or other non CC_Base types) port.types (for >>{tn}<<) is not wise", DeprecationWarning, stacklevel=2)
            return f'&cc_P_{tn}'


@dataclass
class CC_Function(ABCD, CC_Base):               # ABC
    name: str
    _ : KW_ONLY
    type: type=None                      # the return type of the callable
    body=None                            # XXX Add the (AST of the) body LATER


@dataclass
class CC_Handler(CC_Function):            # ABC Can be an event of data/stream -- with or without parameters
    _ : KW_ONLY
    port: CC_Port

@dataclass
class CC_EventHandler(CC_Handler):
    _ : KW_ONLY
    parameterTuple: CC_TypedParameterTuple=()

@dataclass
class CC_Method(CC_Function, ABCD):
    _ : KW_ONLY
    parameterTuple: CC_TypedParameterTuple=()

class CC_ClassMethod(CC_Method): pass
class CC_ElementMethod(CC_Method): pass      #Or CC InstanceMethod??

