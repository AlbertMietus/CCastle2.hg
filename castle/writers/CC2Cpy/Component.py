# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

__all__ = ['CC_B_ComponentInterface', ]

from enum import Enum

from .CCbase import *
CC_Component: TypeAlias = 'CC_Component' # Forward ref

class CC_PortDirection(Enum):
    Unknown = CC_B_PortDirectionIs_UNKNOWN   = 0
    In      = CC_B_PortDirectionIs_in        = 1
    Out     = CC_B_PortDirectionIs_out       = 2
    BiDir   = CC_B_PortDirectionIs_bidirect  = 3 # Not supported yet
    Master  = CC_B_PortDirectionIs_master    = 4 # Not supported yet
    Slave   = CC_B_PortDirectionIs_slave     = 5 # Not supported yet

    def render(self):                                                 ### CC_B_PortDirectionIs_{self.name}'
        return f'CC_B_PortDirectionIs_{self.name}'

@dataclass
class CC_Port(CC_Base):
    name: str
    _ : KW_ONLY
    direction: CC_PortDirection =  CC_PortDirection.Unknown
    type: type

    def render(self) ->str:                                           ### <port name>
        return f'cc_P_{self.type if isinstance(self.type, str) else self.type.name}'

class CC_B_ComponentInterface(CC_Base):pass
## @dataclass
## class CC_B_ComponentInterface(CC_Base):
##     name: str
##     based_on: Optional[CC_Component]=()
##     _: KW_ONLY
##     ports: Sequence[CC_Port] =()

##     def __post_init__(self):
##         self.based_on = mk_tuple(self.based_on)
##         self.ports = mk_tuple(self.ports)

##     def no_of_ports(self, inherired=False, mine=True) ->int:
##         count = 0
##         if inherired:
##             for b in self.based_on:
##                 count += b.no_of_ports(inherired=True)
##         if mine:
##             count += len(self.ports)
##         return count

##     def render(self, prepend:str="", indent="   ") ->str:
##         self.render_struct(prepend=prepend, indent=indent)

##     def render_struct(self, prepend:str="", indent="   ") ->str:                                   ## struct CC_B_ComponentInterface cc_CI_${name} ...
##         """
##         .. todo::

##            - Move `CC_B_ComponentInterface.render()` into a Rendering subclass-delegate
##            - refactor & test: spilt into parts
##            - optional: Use Jinja ipv f-strings
##            - make name/prefix  (``f'cc_CI_{self.name}``) in a getter oid
##            """
##         name = f'cc_CI_{self.name}'
##         based_on_link = f'&cc_CI_{self.based_on[0].name}' if self.based_on[0] else "NULL"

##         retval = []
##         retval.append(f'{prepend}struct CC_B_ComponentInterface {name} = {{')
##         retval.append(f'{prepend}{indent}.name          = "{self.name}",')
##         retval.append(f'{prepend}{indent}.inherit_from  = {based_on_link},')
##         retval.append(f'{prepend}{indent}.length        = {len(self.ports)},')
##         retval.append(f'{prepend}{indent}.ports = {{')

##         #loop over ports ...
##         for n,p in enumerate(self.ports, self.no_of_ports(inherired=True, mine=False)):
##             retval.append(f'{prepend}{(indent*3)[:-2]}{{ .portNo    = {n}, ')
##             retval.append(f'{prepend}{indent*3}.protocol  = &{p.render()}, ')
##             retval.append(f'{prepend}{indent*3}.direction = {p.direction.render()}, ')
##             retval.append(f'{prepend}{indent*3}.name      = "{p.name}", ')
##             retval.append(f'{prepend}{indent*3}.part_of   = &{name} }} ,')
##         retval.append(f'{prepend}{indent}}}')   # end of ports
##         retval.append(f'{prepend}}} ;')  # end of struct

##         return '\n'.join(retval)+"\n"
