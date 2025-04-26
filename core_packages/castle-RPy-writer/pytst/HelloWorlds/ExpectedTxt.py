EXPECTED_ComponentInterface = """\
cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(
    name         = "Elemental_HelloWorld",
    inherit_from = base.cc_CI_Component,
    ports        = (),
    )
\n"""

EXPECTED_CompImplementation = """\
class CC_Elemental_HelloWorld(buildin.CC_B_Component):

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init(*args)


    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def Power_powerOn__power(self, max):
        self.HelloWorld('''Elemental''')


cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )

"""

HACK_PRE="""\
#hack (pre)
from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC import base

"""

HACK_POST="""\
#hack (post)
CC_P_Power_On = 1 # XXX ToDo: move to ..
cc_S_Elemental_HelloWorld_power = [
    None,
    CC_Elemental_HelloWorld.Power_powerOn__power,
    ]
#end hack
\n"""

EXPECTED_unit = HACK_PRE + EXPECTED_ComponentInterface + EXPECTED_CompImplementation +HACK_POST

