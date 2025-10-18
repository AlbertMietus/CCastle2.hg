# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

class Portray:
    """Portray is an auxility class of Renderer to convert AIGR "names" into the RPY names.

    Mostly, this is prefixing names and/or converting "names" to strings"""

    def __init__(self, renderer):
        self._renderer = renderer

    def prefix(self, prefix:str, name:str) ->str:
        parts=str(name).split('.')
        ns, n = ".".join(parts[:-1]), parts[-1]
        if ns:
            ns+="."
        return ns+prefix+n

    def CC_cls_prefix(self, name:str):                     return self.prefix('CC_',    name)                # generated cls for Component
    def cc_C_elm_prefix(self, name:str):                   return self.prefix('cc_C_',  name)                # element (instantiated Component)
    def cc_CI_elm_prefix(self, name:str):                  return self.prefix('cc_CI_', name)                # component-interface
    def cc_S_dispatchTable(self, comp:str, port:str):      return self.prefix('cc_S_',  f'{comp}_{port}')    # (event) dispatch-table
    def CC_P_eventTrigger(self, protocol:str, event:str):  return self.prefix('CC_P_', f'{str(protocol)}_{str(event)}') #key in dispatch-table
    def callDef_name(self, name:str):                      return self.prefix('', name)                      # A callable/function
    def CompBase(self):                                    return 'buildin.CC_B_Component'
