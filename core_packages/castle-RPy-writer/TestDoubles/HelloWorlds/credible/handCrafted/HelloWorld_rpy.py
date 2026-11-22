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
    """GAM: Each individual 'Credible' element has its own instantiation of this class
            It save element values, and "class methods"; including the ones of CC_B_Component"""

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible)
        self._castle_init(*args)

    def _castle_init(self, *args):
        pass


    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def SetLabel_set__hello(self, pos, named):
        label=pos[0]
        self.HelloWorld(label)            #GAM no bundling (BUGFIX)


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
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible_HelloWorld)
        self._castle_init(*args)

    def _castle_init(self, *args):
        self.credible = CC_Credible(*args)

    def std_invoke__std(self, pos, named):
        """///CastleCode         # XXX TODO (in RPy)
              .credible.hello.set("credible") // trigger internal port """
        print (''''WRONG! cc_S_Credible_hello is hardcoded
               the table should be found via self.credible -> ???
               Probally 'CC_B_Component'
               ''')
        print(f"XXX\t {self.credible=}")
        print(f"XXX\t {self.credible.isa=}")
        print(f"XXX\t {self.credible.isa.interface=}")
        print(f"XXX\t {self.credible.isa.methods=}")
        print(f"XXX\t {self.credible.isa.isa=}")
        
        print(f"XXX\t\t {self.credible.isa.interface.name=}")
        print(f"XXX\t\t {self.credible.isa.interface.inherit_from=}")
        print(f"XXX\t\t {self.credible.isa.interface.ports=}")
        
        print(f"XXX\t\t\t {self.credible.isa.interface.ports[0].name=}")
        print(f"XXX\t\t\t {self.credible.isa.interface.ports[0].portNo=}")
        print(f"XXX\t\t\t {self.credible.isa.interface.ports[0].protocol=}")
        print(f"XXX\t\t\t {self.credible.isa.interface.ports[0]._direction=}")
        print(f"XXX\t\t\t {self.credible.isa.interface.ports[0].part_of=}")
        

        return cc_S_Credible_hello['CC_P_SetLabel_set'](self.credible, pos=['credible',], named=None)


cc_C_Credible_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible_HelloWorld,
    )

cc_S_Credible_HelloWorld_std = buildin.machinery.ChainedDict(map={
    'CC_P_std_invoke' : CC_Credible_HelloWorld.std_invoke__std,
    },
    parent=None)


def demo(argv):
    main_elm = CC_Credible_HelloWorld()
    cc_S_Credible_HelloWorld_std['CC_P_std_invoke'](main_elm, pos=None, named=None)
    return 0

def target(*args):
  return demo, None

import sys
if __name__ == '__main__':
  import sys
  demo(sys.argv)
