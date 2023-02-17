# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

__all__ = ['CC_B_ComponentInterface', 'CC_Port', 'CC_PortDirection', 'CC_B_ComponentClass']

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

    def find_port_by_name(self,name:str) -> CC_Port:
        return next(p for p in self.ports if p.name=='try')

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

########################################################################################################################
##################################### BUSY ### XXX ### BUZY ############################################################
########################################################################################################################



@dataclass
class CC_B_ComponentClass(CC_Base):
    metaclass="NULL"                         # //NULL for now, later: meta-class
    interface: CC_B_ComponentInterface
    _: KW_ONLY
    data_members: Sequence[CC_TypedParameter]=() # (own) Data-members
    handlers:     Sequence[CC_Handler] =()       # EventHanders, DataHandler, StreamHandlers, and all-other-protocolHandlers
    methods:      Sequence[CC_Method]  =()       # All kind of "internal only" callable(s)

    def _name(self): 					return self.interface.name
    def portray_interface_name(self): 	return f'cc_CI_{self._name()}'
    def portray_Typedef_CompName(self):	return f'CC_C_{self._name()}'
    def portray_methods_name(self):		return f'cc_S_{self._name()}_methods'

    def render(self, prepend:str="", indent:str="   ") ->str:
        """.. note:: The order of generated code is relevant!

              As the CC_B_ComponentClass (variable) refers to CC_C_$CompName (typedef) [by sizeof()],
              we need to call render_Typedef_CompName first!"""
        return ( "\n"+
            self.render_Typedef_CompName(prepend=prepend, indent=indent) + "\n" +
            self.render_handlers(prepend=prepend, indent=indent) + "\n" +
            self.render_methods(prepend=prepend, indent=indent) + "\n" +
            self.render_(prepend=prepend, indent=indent) + "\n" +
           
            self.render_Fill_ComponentClass(prepend=prepend, indent=indent) + "\n" +
            "\n" )

    def render_Fill_ComponentClass(self, prepend:str="", indent:str="  ") ->str:          ## struct CC_B_ComponentClass cc_C_$name {...}
        interface_name    = self.portray_interface_name()
        Typedef_CompName  = self.portray_Typedef_CompName()
        methods_name      = self.portray_methods_name()

        retval = []
        retval.append(f'{prepend}struct CC_B_ComponentClass  cc_C_{self.interface.name} = {{')
        retval.append(f'{prepend}{indent}.isa           = {self.metaclass},')
        retval.append(f'{prepend}{indent}.interface     = &{interface_name},')
        retval.append(f'{prepend}{indent}.instance_size = sizeof({Typedef_CompName}),')
        retval.append(f'{prepend}{indent}.methods       = {methods_name},')
        retval.append(f'{prepend}}};')

        return '\n'.join(retval)+"\n"

    def render_Typedef_CompName(self, prepend:str="", indent:str="  ") ->str:                     ## typedef struct CC_C_$CompName
        """.. note:: Asume simple inheritance

              :need:`Tools_No_MultipleInheritance-in-1compiler`
              http://docideas.mietus.nl/en/default/CCastle/3.Design/zz.todo.html#Tools_No_MultipleInheritance-in-1compiler"""
        Typedef_CompName  = self.portray_Typedef_CompName()
        retval = []
        retval.append(f'{prepend}typedef struct {{')
        for bc in self._bases_classes():   #XXX
            retval += bc.prerender_CompName_elements(prepend,indent)
        retval += self.prerender_CompName_elements(prepend,indent)
        retval.append(f'}} {Typedef_CompName};')

        return '\n'.join(retval)+"\n"

    def _bases_classes(self) ->Sequence:   #XXX
        return ()                          #XXX WRONG

    def prerender_CompName_elements(self, prepend:str="", indent:str="  ") ->Sequence[str]:
        retval=[]
        logger.debug('.data_members)[%s]:: %s', len(self.data_members), self.data_members)
        for d in self.data_members:
            retval.append(f'{prepend}{indent}{d.type} \t {d.name};')                          # XXX type is not a string
        logger.debug('.handlers)[%s]:: %s', len(self.handlers), self.handlers)
        for h in self.handlers:
            retval.append(f'{prepend}{indent}struct CC_B_OutPort \t {h.port.name};')
        logger.debug('.methods)[%s]:: %s', len(self.methods), self.methods)
        for m in self.methods:
            retval.append(f'{prepend}{indent} /*XXXXX*/')

        logger.debug('\n'+'\n'.join(retval))
        return retval
