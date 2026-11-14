# (C) Albert Mietus, 2025,25 Part of Castle/CCastle project

"""Some pieces of text, that are expected in some test when using the RPy-writer to render
  Credible HelloWorld (see TestDoubles for input)"""


EXPECTED_FileHeader="""\
from castle.writers.RPy_buildin import buildin
from castle.writers.RPy_buildin import base
\n
\n"""

EXPECTED_Protocol="""\
cc_P_SetLabel = buildin.CC_B_Protocol(name="SetLabel",
    kind = buildin.CC_ProtocolKind.Event,
    inherit_from = None,
    events = [])
\n"""

###
### Credible
###

EXPECTED_Interface_Credible="""\
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
\n\n"""


EXPECTED_Implementation_Credible="""\
class CC_Credible(buildin.CC_B_Component):

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible)
        self._castle_init(*args)


    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def SetLabel_set__hello(self, pos, named):
        label = CC_B_string.unbox(pos[0])

        self.HelloWorld(label)
\n\n"""



EXPECTED_CompClass_Credible  = """\
cc_C_Credible = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible,
    )
\n"""

EXPECTED_DispatchTables_Credible="""\
cc_S_Credible_hello = buildin.machinery.ChainedDict(map={
    'CC_P_SetLabel_set' : CC_Credible.SetLabel_set__hello,
    },
    parent=None)
"""

###
### HW :: Credible_HelloWorld
###

EXPECTED_Interface_HW="""\
cc_CI_Credible_HelloWorld = buildin.CC_B_ComponentInterface(
    name         = "Credible_HelloWorld",
    inherit_from = base.cc_CI_Component,
    ports        = [],
    )
\n"""


EXPECTED_Implementation_HW="""\
class CC_Credible_HelloWorld(buildin.CC_B_Component):

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Credible_HelloWorld)
        self._castle_init(*args)



    def _castle_init(self, *args):
        self.credible = CC_Credible(*args)

    def std_invoke__std(self, pos, named):
        ### XXX ToDo
        return cc_S_Credible_hello['CC_P_SetLabel_set'](self.credible, pos=['credible',], named=None)
\n\n\n"""

EXPECTED_CompClass_HW  = """\
cc_C_Credible_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Credible_HelloWorld,
    )
\n"""

EXPECTED_DispatchTables_HW="""\
cc_S_Credible_HelloWorld_std = buildin.machinery.ChainedDict(map={
    'CC_P_std_invoke' : CC_Credible_HelloWorld.std_invoke__std,
    },
parent=None)
"""

EXPECTED_CompClass_Credible_depart  = EXPECTED_CompClass_Credible + EXPECTED_DispatchTables_Credible
EXPECTED_CompClass_HW_depart        = EXPECTED_CompClass_HW       + EXPECTED_DispatchTables_HW



EXPECTED_Credible = EXPECTED_Implementation_Credible + EXPECTED_CompClass_Credible_depart +"\n"
EXPECTED_HW       = EXPECTED_Implementation_HW       + EXPECTED_CompClass_HW_depart       +"\n"


EXPECTED_unit = EXPECTED_FileHeader + EXPECTED_Protocol + \
  EXPECTED_Interface_Credible + EXPECTED_Credible + \
  EXPECTED_Interface_HW +\
  EXPECTED_HW +\
  "XXX Interface" + "XXX Protocol"
