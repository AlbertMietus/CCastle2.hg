from castle.writers.RPy_buildin import buildin
from castle.writers.RPy_buildin import base


#def Machinery_trigger_direct(receiver, event_key, handlers, arglist):
#    handler = handlers[event_key]
#    return handler(receiver, arglist)


cc_P_SetLabel = buildin.CC_B_Protocol(name="SetLabel",
    kind =  buildin.CC_ProtocolKind.Event,
    inherit_from = None,
    events = [])

cc_CI_Credible = buildin.CC_B_ComponentInterface(
    name         = "Credible",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )

cc_CI_Credible.ports.append(
    buildin.CC_B_C_PortID(name="event",
        portNo=-1, # Not used?
        protocol=cc_P_SetLabel,
        direction=buildin.CC_PortDirection.In,
        part_of=cc_CI_Credible))


class CC_Credible(buildin.CC_B_Component):

    def __init__(self, arglist):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible)
        self._castle_init(arglist=[])

    def _castle_init(self, arglist):
        pass

        
    def HelloWorld(self, arglist):
        label=arglist[0]
        print("Hello %s World" % (label,))

    def SetLabel_set__hello(self, arglist):
        label=arglist[0]
        self.HelloWorld(arglist=[label])


cc_C_Credible = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible,
    )

cc_S_Credible_hello = buildin.machinery.ChainedDict(map={
    'CC_P_SetLabel_set' : CC_Credible.SetLabel_set__hello,
    },
    parent=None)

cc_CI_Credible_HelloWorld = buildin.CC_B_ComponentInterface(
    name         = "Credible_HelloWorld",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )

class CC_Credible_HelloWorld(buildin.CC_B_Component):

    def __init__(self, arglist):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible_HelloWorld)
        self._castle_init(arglist=[])

    def _castle_init(self, arglist):
        self.credible = CC_Credible(arglist=arglist)

    def std_invoke__std(self, arglist):
        """///CastleCode         # XXX TODO (in RPy)
              .credible.hello.set("credible") // trigger internal port
        """
        return cc_S_Credible_hello['CC_P_SetLabel_set'](self.credible,['credible',]) # USING arglist:list is KEY


cc_C_Credible_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible_HelloWorld,
    )

cc_S_Credible_HelloWorld_std = buildin.machinery.ChainedDict(map={
    'CC_P_std_invoke' : CC_Credible_HelloWorld.std_invoke__std,
    },
    parent=None)


def demo(argv):
    main_elm = CC_Credible_HelloWorld(arglist=[])
    cc_S_Credible_HelloWorld_std['CC_P_std_invoke'](main_elm,[])
    return 0

def target(*args):
  return demo, None

import sys
if __name__ == '__main__':
  import sys
  demo(sys.argv)
