from castle.writers.RPy_buildin import buildin
from castle.writers.RPy_buildin import base



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

    def __init__(self, *args):
        print('XXX 2')
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible)
        self._castle_init(*args)

    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def SetLabel_set__hello(self, label ):
        self.HelloWorld(label)


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

    def __init__(self, *args):
        print('XXX 1a')
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible_HelloWorld)
        self._castle_init(*args)

    def _castle_init(self, ):
        print('XXX 1b')
        self.credible = CC_Credible()


    def std_invoke__std(self, ):
        """///CastleCode         # XXX TODO (in RPy)
              .credible.hello.set("credible") // trigger internal port
        """
        print('XXX 3')
        handler = cc_S_Credible_hello['CC_P_SetLabel_set']
        elm = self.credible
        handler(elm, 'credible', 'xxx')
        #WRONG# handler(elm, 'credible', )
        #OKE#	self.credible.SetLabel_set__hello('XXX-1 credible')
        #WORKS	elm.SetLabel_set__hello('XXX-2 credible')



cc_C_Credible_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible_HelloWorld,
    )

cc_S_Credible_HelloWorld_std = buildin.machinery.ChainedDict(map={
    'CC_P_std_invoke' : CC_Credible_HelloWorld.std_invoke__std,
    },
    parent=None)


def demo(argv):
    main_elm = CC_Credible_HelloWorld()
    cc_S_Credible_HelloWorld_std['CC_P_std_invoke'](main_elm)
    return 0

def target(*args):
  return demo, None

import sys
if __name__ == '__main__':
  import sys
  demo(sys.argv)
