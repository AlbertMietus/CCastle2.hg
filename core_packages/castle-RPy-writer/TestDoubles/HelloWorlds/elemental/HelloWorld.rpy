# -*-python-*-
# (C) Albert Mietus, 2025. Part of Castle/CCastle project
#========================================================
# This is a manually crafted "translation" from `elemental/HelloWorld.Castle`
# Once day, the RPy writer will generate a simulair file, based on the AIGR TestDouble.
# See the package:  TestDoubles-HelloWorlds, and the files
# - CastleCode/elemental/HelloWorld.Castle 							(CastleCode)
# - castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py 	(AIGR)


from castle.writers.RPy_buildin import base
from castle.writers.RPy_buildin import buildin

from castle.writers.RPy_buildin.HACK import std   #XXX


"""///CastleCode ToDo
@impliciet(Main) ...    port std<bidir>:std
///end"""
cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(
    name = "Elemental_HelloWorld",
    inherit_from   = std.cc_CI_Main,
    ports          = [])


class CC_Elemental_HelloWorld(buildin.CC_B_Component): # Generated class;
    """///CastleCode
    @impliciet(Main)
    implement Elemental_HelloWorld
    {///"""

    def __init__(self, arglist):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init(arglist=arglist)

    def _castle_init(self, arglist):
        pass
        # XXX ToDO: update CC_B_Component._castle_init() to handle arglist

    def HelloWorld(self, arglist):
        """///Castlecode
        HelloWorld(str:label) {
           print("Hello {label} World")
        }"""

        label=arglist[0]
        print("Hello %s World" % (label))

    def std_invoke__std(self, arglist):
        """///Castlecode
         invoke() on self.std {
           HelloWorld("Elemental")
        }"""

        self.HelloWorld(['Elemental'])
#///Castlecode:
# } /* Elemental_HelloWorld */



cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )


cc_S_Elemental_HelloWorld_std = {
    'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std
    }

