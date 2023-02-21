# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project


import logging; logger = logging.getLogger(__name__)

from .CCbase import *
from castle.auxiliary.pack import mk_tuple

CC_Component: TypeAlias = 'CC_Component' # Forward ref                          # pragma: no mutate


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

    def find_port_by_name(self, name:str) -> CC_Port:
        return next(p for p in self.ports if p.name==name)

    def render(self, prepend:str="", indent:str="   ") ->str:
        return (
            self.render_Fill_Interface(prepend=prepend, indent=indent)\
            )

    def render_Fill_Interface(self, prepend:str="", indent:str="   ") ->str:              ## struct CC_B_ComponentInterface `cc_CI_$name` = ...
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

