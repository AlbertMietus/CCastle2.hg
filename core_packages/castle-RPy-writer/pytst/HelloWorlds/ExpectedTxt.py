# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Some pieces of text, that are expected in some test when using the RPy-writer to render Elemental_HelloWorld (see TestDoubles for input)"""

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

    def std_invoke__std(self, ):
        self.HelloWorld('''Elemental''')
\n\n"""


EXPECTED_DispatchTables = """\
cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )
\n"""


HACK_PRE="""\
#hack (pre)
from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC import base

from castle.writers.RPy.CC.HACK import std   #XXX
from MACHINERY import MACHINERY
\n
"""

HACK_POST="""\
#hack (post)
if MACHINERY == 'dict':
    cc_S_Elemental_HelloWorld_std = buildin.machinery.ChainedDict(map={
        'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std
        },
        parent=None)
else:
    assert False, "Set 'MACHINERY'!"
#end hack
\n"""

EXPECTED_unit = HACK_PRE + EXPECTED_ComponentInterface + EXPECTED_CompImplementation  + EXPECTED_DispatchTables + HACK_POST

