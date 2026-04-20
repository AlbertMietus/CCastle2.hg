# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
from castle import aigr

class Portray:
    """Portray is an auxility class of Renderer to convert AIGR "names" into the RPY names.

    Mostly, this is prefixing names and/or converting "names" to strings"""

    def __init__(self, renderer):
        self._renderer = renderer

    ###
    ### Some builtin-class-names
    ###

    def BuildInComponent(self):                             return 'buildin.CC_B_Component'
    def BuildInProtocol(self):                              return 'buildin.CC_B_Protocol'
    def BuildInComponentInterface(self):					return 'buildin.CC_B_ComponentInterface'

    ###
    ### Convert (node)names:str to RPY-names with prefixes
    ###

    def CC_cls_prefix(self, name:str):                      return self.prefix('CC_',    name)                # generated cls for Component
    def cc_C_elm_prefix(self, name:str):                    return self.prefix('cc_C_',  name)                # element (instantiated Component)
    def cc_CI_elm_prefix(self, name:str):                   return self.prefix('cc_CI_', name)                # component-interface
    def cc_S_dispatchTable(self, comp:str, port:str):       return self.prefix('cc_S_',  f'{comp}_{port}')    # (event) dispatch-table
    def CC_P_eventTrigger(self, protocol:str, event:str):   return self.prefix('CC_P_', f'{str(protocol)}_{str(event)}') #key in dispatch-table
    def callDef_name(self, name:str):                       return self.prefix('', name)                      # A callable/function
    def CC_ProtocolName_prefix(self, name:str):             return self.prefix('cc_P_', name)

    def prefix(self, prefix:str, name:str) ->str:
        parts=str(name).split('.')
        ns, n = ".".join(parts[:-1]), parts[-1]
        if ns:
            ns+="."
        return ns+prefix+n

    def default_component(self):                            return 'base.cc_CI_Component'         # XXX

    ###
    ### Convert AIGR-nodes to txt:str
    ###

    def Port2Protocol(self, port: aigr.Port) ->str:                       # XXXX Move to render
        if not isinstance(port.type, aigr.Protocol):
            raise NotImplementedError(f"Only Protocol-Ports are supported. Not: {port}")
        protocol :aigr.Protocol = port.type
        assert protocol.name is not None
        return self.CC_ProtocolName_prefix(protocol.name)

    def PortDirection(self, port: aigr.Port) ->str:
        aigr2buildin = {
            aigr.PortDirection.Unknown : 'Unknown',   # Should not happen:-)
            aigr.PortDirection.In      : 'In',
            aigr.PortDirection.Out     : 'Out',
            aigr.PortDirection.Bidir   : 'BiDir',     # Not supported yet
            aigr.PortDirection.Master  : 'Master',    # Not supported yet
            aigr.PortDirection.Slave   : 'Slave',     # Not supported yet
            }
        return 'buildin.CC_PortDirection' +'.' + aigr2buildin[port.direction]


