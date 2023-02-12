# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

__all__ = ['CC_B_ComponentInterface', 'CC_Port', 'CC_PortDirection', 'CC_B_ComponentClass']

from enum import Enum

from .CCbase import *
from castle.auxiliary.pack import mk_tuple
from castle.auxiliary.abcd import ABCD

CC_Component: TypeAlias = 'CC_Component' # Forward ref                          # pragma: no mutate

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
class CC_B_ComponentInterface(CC_Base):
    name: str
    based_on: Sequence[CC_Component]=()                                         # pragma: no mutate
    _: KW_ONLY
    ports: Sequence[CC_Port] =()                                                # pragma: no mutate

    def __post_init__(self):
        self.based_on = mk_tuple(self.based_on)
        self.ports = mk_tuple(self.ports)

    def no_of_ports(self, inherited=False, mine=True) ->int:
        count = 0
        if inherited:
            for b in self.based_on:
                count += b.no_of_ports(inherited=True)
        if mine:
            count += len(self.ports)
        return count

    def render(self, prepend:str="", indent:str="   ") ->str:
        return self.render_Fill_Interface(prepend=prepend, indent=indent)

    def render_Fill_Interface(self, prepend:str="", indent:str="   ") ->str:          ## struct CC_B_ComponentInterface `cc_CI_$name` = ...
        name = f'cc_CI_{self.name}'
        based_on_link = f'&cc_CI_{self.based_on[0].name}' if self.based_on else "NULL"

        retval = []
        retval.append(f'{prepend}struct CC_B_ComponentInterface {name} = {{')
        retval.append(f'{prepend}{indent}.name          = "{self.name}",')
        retval.append(f'{prepend}{indent}.inherit_from  =  {based_on_link},')
        retval.append(f'{prepend}{indent}.length        =  {len(self.ports)},')
        retval.append(f'{prepend}{indent}.ports = {{')
        start_port_no = self.no_of_ports(inherited=True, mine=False)            # pragma: no mutate on inherited/mine
        for no,port in enumerate(self.ports, start_port_no):                    # Loop over 'own' ports
            retval.append(f'{prepend}{indent*2}{{')
            retval.append(f'{prepend}{indent*3}.portNo    =  {no},')
            retval.append(f'{prepend}{indent*3}.protocol  =  {port.portray_typePtr()},')
            retval.append(f'{prepend}{indent*3}.direction =  {port.direction.portray_name()},')
            retval.append(f'{prepend}{indent*3}.name      = "{port.name}",')
            retval.append(f'{prepend}{indent*3}.part_of   = &{name} }},')
        retval.append(f'{prepend}{indent}}},')   # end of ports
        retval.append(f'{prepend}}} ;')  # end of struct

        return '\n'.join(retval)+"\n"

########################################################################################################################
##################################### BUSY ### XXX ### BUZY ############################################################
########################################################################################################################




@dataclass
class CC_Function(ABCD, CC_Base):               # ABC
    name: str
    _ : KW_ONLY
    type: type                            # the return type of the callable
    body=None;                            # XXX Add the (AST of the) body LATER


@dataclass
class CC_Handler(CC_Function):            # ABC Can be an event of data/stream -- with or without paramters
    _ : KW_ONLY
    portID: CC_Port

@dataclass
class CC_EventHandler(CC_Handler):
    _ : KW_ONLY
    parameterTuple: "ToBeDone"

@dataclass
class CC_Method(CC_Function): pass
class CC_ClassMethod(CC_Method): pass
class CC_ElementMethod(CC_Method): pass      #Or CC InstanceMethod??


@dataclass
class CC_B_ComponentClass(CC_Base):
    metaclass="NULL"                         # //NULL for now, later: meta-class
    interface: CC_B_ComponentInterface
    handlers:  Sequence[CC_Handler] =()    # EventHanders, DataHandler, StreamHandlers, and all-other-protocolHandlers
    methods:   Sequence[CC_Method]  =()    # All kind of "internal only" callable(s)

    def render(self, prepend:str="", indent:str="   ") ->str:
        return self.render_Fill_ComponentClass(prepend=prepend, indent=indent)


    def render_Fill_ComponentClass(self, prepend:str="", indent:str="  ") ->str:          ## struct CC_B_ComponentClass cc_C_$name {...}
        name = self.interface.name
        interface_name = f'cc_CI_{name}'
        comp_TypeName  = f'CC_C_{name}'
        methods_name   = f'cc_B_{name}_methods'

        retval = []
        retval.append(f'{prepend}struct CC_B_ComponentClass  cc_C_{self.interface.name} = {{')
        retval.append(f'{prepend}{indent}.isa           = {self.metaclass},')
        retval.append(f'{prepend}{indent}.interface     = &{interface_name},')
        retval.append(f'{prepend}{indent}.instance_size = sizeof({comp_TypeName}),')
        retval.append(f'{prepend}{indent}.methods       = {methods_name},')
        retval.append(f'{prepend}}};')

        return '\n'.join(retval)+"\n"

    def render_CompName(self, prepend:str="", indent:str="  ") ->str:                     ## typedef struct CC_C_$CompName
        pass
