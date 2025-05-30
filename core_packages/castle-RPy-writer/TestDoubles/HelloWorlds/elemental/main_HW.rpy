# -*-python-*-
# (C) Albert Mietus, 2025. Part of Castle/CCastle project
#========================================================
# This is the driver to run the manually crafted "translation" from `elemental/HelloWorld.Castle`

from MACHINERY import MACHINERY
from HelloWorld import *

def demo(argv):

    main_comp = CC_Elemental_HelloWorld
    main_elm  = main_comp()

    # if MACHINERY == 'dict':
    #     cc_S_Elemental_HelloWorld_power['CC_P_Power_On'](main_elm, "__dummy__")
    # else:
    #    cc_S_Elemental_HelloWorld_power[CC_P_Power_On](main_elm, "__dummy__")

    if MACHINERY == 'dict':
        cc_S_Elemental_HelloWorld_std['CC_P_std_invoke'](main_elm)
    else:
        cc_S_Elemental_HelloWorld_std[CC_P_std_invoke](main_elm)

    return 0

def target(*args):
  return demo, None

import sys
if __name__ == '__main__':
  import sys
  demo(sys.argv)
