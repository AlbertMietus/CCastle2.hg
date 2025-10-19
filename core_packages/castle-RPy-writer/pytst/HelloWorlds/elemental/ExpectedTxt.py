# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Some pieces of text, that are expected in some test when using the RPy-writer to render
   Elemental_HelloWorld (see TestDoubles for input)"""

EXPECTED_ComponentInterface = """\
cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(
    name         = "Elemental_HelloWorld",
    inherit_from = base.cc_CI_Component,
    ports        = (),
    )
\n"""


EXPECTED_CompImplementation_only = """\
class CC_Elemental_HelloWorld(buildin.CC_B_Component):

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init(*args)


    def HelloWorld(self, label):
        print("Hello %s World" % (label,))

    def std_invoke__std(self, ):
        self.HelloWorld('''Elemental''')
\n\n"""


EXPECTED_CompClass  = """\
cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )
\n"""

EXPECTED_DispatchTables="""\
cc_S_Elemental_HelloWorld_std = buildin.machinery.ChainedDict(map={
    'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std,
    },
    parent=None)
"""


EXPECTED_FileHeader="""\
from castle.writers.RPy_buildin import buildin
from castle.writers.RPy_buildin import base
\n
\n"""


EXPECTED_CompImplementation_depart   = EXPECTED_CompClass + EXPECTED_DispatchTables
EXPECTED_CompImplementation          = EXPECTED_CompImplementation_only  + EXPECTED_CompImplementation_depart +"\n"

EXPECTED_unit = EXPECTED_FileHeader + EXPECTED_ComponentInterface + EXPECTED_CompImplementation

