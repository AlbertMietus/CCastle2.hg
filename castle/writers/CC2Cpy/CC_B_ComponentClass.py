# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from .CCbase import *
from .CC_B_ComponentInterface import CC_B_ComponentInterface
from castle.auxiliary.pack import mk_tuple

CC_Component: TypeAlias = 'CC_Component' # Forward ref                          # pragma: no mutate

@dataclass
class CC_B_ComponentClass(CC_Base):
    metaclass="NULL"                         # //NULL for now, later: meta-class
    interface: CC_B_ComponentInterface
    _: KW_ONLY
    data_members: Sequence[CC_TypedParameter]=() # (own) Data-members
    handlers:     Sequence[CC_Handler] =()       # EventHanders, DataHandler, StreamHandlers, and all-other-protocolHandlers
    methods:      Sequence[CC_Method]  =()       # All kind of "internal only" callable(s)

    def _name(self): 					return self.interface.name
    def _ports(self):					return self.interface.ports
    def _in_ports(self):                return (p for p in self._ports() if p.isInPort())

    def portray_interface_name(self): 	return f'cc_CI_{self._name()}'
    def portray_Typedef_CompName(self):	return f'CC_C_{self._name()}'
    def portray_methods_name(self):		return f'cc_S_{self._name()}_methods'

    def render(self, prepend:str="", indent:str="   ") ->str:
        """.. note:: The order of generated code is relevant!

              As the CC_B_ComponentClass (variable) refers to CC_C_$CompName (typedef) [by sizeof()],
              we need to call render_Typedef_CompName first!"""
        return ( "\n"+
            self.render_Typedef_CompName(prepend=prepend, indent=indent) + "\n" +
            self.render_Fill_MethodHandlers(prepend=prepend, indent=indent) + "\n" +
            "\n".join(self.render_Fill_PortHandlers(p, prepend=prepend, indent=indent) for p in self._in_ports()) + "\n" +
            self.render_callables(prepend=prepend, indent=indent) + "\n" +   # handlers & methods (implementation) XXX TODO
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


    def render_callables(self, prepend:str="", indent:str="   ") ->str:
        return """\
/** TODO: render_callables::
     all Event/Data/Stream-handlers and local ("internal") methods/functions.

    This are a lot of (tobe static) C-function implementations, like
    * CC_C_Sieve*  CC_Mi_Sieve__init(CC_C_Sieve* self, int prime) ...
    * CC_C_Sieve*  CC_E_Sieve__SimpleSieve_input__try(CC_C_Sieve* self, CC_OutPortType sender, int try) ...
    * etc (one for every event in every input-port, plus the local ones

    Those functions are collected in CC_B_methodHandler-array and CC_B_eventHandler-arrays (aka dispatch-tables).
    those are NOW generated here*/"""






    def render_Fill_MethodHandlers(self, prepend:str="", indent:str="   ") ->str:
        retval = []
        retval.append(f'{prepend}CC_B_methodHandler cc_S_{self._name()}_methods[] = {{')
        ### XXX TODO:: loop over base_classes

        for m in self.methods:
            retval.append(f'{prepend}{indent}(CC_B_methodHandler)CC_Mi_{self._name()}__{m.name},')

        retval.append(f'}};')
        return '\n'.join(retval)+"\n"





    def render_Fill_PortHandlers(self, port, prepend:str="", indent:str="   ") ->str:
        retval = []

        retval.append(f'CC_B_methodHandler cc_S_Sieve_try[] = {{')

        retval.append(f"""/* TODO: ``render_Fill_PortHandlers(port={port})``
                             the local/internal functions & methods
                             Note: `cc_S_Sieve_try` is hardcoded
                          */""")
        retval.append(f'}};')
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
