# -*-python-*-
# (C) Albert Mietus, 2025. Part of Castle/CCastle project
#========================================================
# This is a manually crafted "translation" from `elemental/HelloWorld.Castle`
# Once day, the RPy writer will generate a simulair file, based on the AIGR TestDouble.
# See the package:  TestDoubles-HelloWorlds, and the files
# - CastleCode/elemental/HelloWorld.Castle 							(CastleCode)
# - castle/TESTDOUBLES/aigr/HelloWorlds/elemental/HelloWorld.py 	(AIGR)

# Hi-lock: (("///.*$" (0 (quote hi-pink) prepend)))

from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC import base
from castle.writers.RPy.CC.HACK import std   #XXX

from MACHINERY import MACHINERY

"""///CastleCode ToDo
GAM: This code is "missing (or auto ...?
component Elemental_HelloWorld : Component {}
///end"""
cc_CI_Elemental_HelloWorld = buildin.CC_B_ComponentInterface(
    name = "Elemental_HelloWorld",
    inherit_from   = std.cc_CI_Main,
    ports          = [])



class CC_Elemental_HelloWorld(buildin.CC_B_Component): # Generated class;
    """///CastleCode
    implement Elemental_HelloWorld
    {///"""

    def __init__(self, *args):
        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)
        self._castle_init(*args)

    def HelloWorld(self, label):
        """///Castlecode
        HelloWorld(str:label) {
           print("Hello {label} World")
        }"""
        print("Hello %s World -- machinery:%s, base:%s" % (label, MACHINERY, cc_CI_Elemental_HelloWorld.inherit_from.name))

    def std_invoke__std(self):            #GAM `std::invoke` is an great candidate for the Main component's port `std`
        """///Castlecode
         invoke() on self.std {
           HelloWorld("Elemental")
        }"""

        self.HelloWorld('''Elemental''')
#///Castlecode:
# } /* Elemental_HelloWorld */



cc_C_Elemental_HelloWorld = buildin.CC_B_ComponentClass(
    interface = cc_CI_Elemental_HelloWorld,
    )

# if MACHINERY == 'list' or MACHINERY == 'default':
#     CC_P_Power_On = 1                        # XXX ToDo: move to ..
#     cc_S_Elemental_HelloWorld_power = [
#         None,
#         CC_Elemental_HelloWorld.Power_powerOn__power,
#         ]
# elif MACHINERY == 'tuple':
#     cc_S_Elemental_HelloWorld_power = (
#         None,
#         CC_Elemental_HelloWorld.Power_powerOn__power,
#     )
# elif MACHINERY == 'dict':
#     cc_S_Elemental_HelloWorld_power = {
#         'CC_P_Power_On' : CC_Elemental_HelloWorld.Power_powerOn__power,
#         }
# else:
#     assert False, "Set 'MACHINERY'!"


if MACHINERY == 'list' or MACHINERY == 'default':
    pass
elif MACHINERY == 'tuple':
    pass
elif MACHINERY == 'dict':
    cc_S_Elemental_HelloWorld_std = {
        'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std
        }
else:
    assert False, "Set 'MACHINERY'!"


