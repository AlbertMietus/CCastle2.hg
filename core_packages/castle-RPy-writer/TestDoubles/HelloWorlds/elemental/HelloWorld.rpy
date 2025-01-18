# -*-python-*-
# (C) Albert Mietus, 2025. Part of Castle/CCastle project
#========================================================
# This is a manually crafted "translation" from `elemental/HelloWorld.Castle`
# Once day, the RPy writer will generate a simulair file, based on the AIGR TestDouble.
# See the package:  TestDoubles-HelloWorlds, and the files
# - CastleCode/elemental/HelloWorld.Castle 							(CastleCode)
# - castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py 	(AIGR)

# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))
# Hi-lock: (("XXX" (0 (quote hi-yellow) prepend)))

from CC import buildin
from CC import base
from CC import machinery
from CC import _debug

#GAM: XXX The component `Elemental_HelloWorld` is also needed
#GAM: XXX That translate to constant like ``cc_C_Elemental_HelloWorld``, which are used below
#GAM: XXX It also set's the number of ports, which is used in __init__: Here none


"""///CastleCode
This code is "missing (or auto ...?
component Elemental_HelloWorld : Component {}
///end"""
cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(
    name = "Elemental_HelloWorld",
    inherit_from   = base.cc_CI_Component,
    ports          = [])




class CC_Elemental_HelloWorld(buildin.CC_B_Component) : # Generated class;
    """///CastleCode
    implement Elemental_HelloWorld
    {///"""

    def __init__(self,  *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init()

    def _castle_init(self):
        """///CastleCode: none"""
        pass

    def HelloWord(self, label):
        """///CastlecodeCOL
        HelloWorld(str:label) {
           print("Hello {label} World")
        }"""
        print(f'''Hello {label} World''')

    def Power_powerOn__power(_dummy__Max):   #///GAM: power-api may change to args of none; max is stange
        """///CastlecodeCOL
        powerOn(max) on self.power {
           HelloWorld("Elemental")
        }"""
        self.HelloWorld('''Elemental''')
#///Castlecode:
# } /* Elemental_HelloWorld */



cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = XXX.cc_CI_Elemental_HelloWorld,   # XXX: namespace
    )

cc_S_Elemental_HelloWorld_power = [
    None,
    Elemental_HelloWorld.powerOn__power,
    ]
