# -*-python-*-
# (C) Albert Mietus, 2025. Part of Castle/CCastle project
#========================================================
# This is the driver to run the manually crafted "translation" from `elemental/HelloWorld.Castle`

from HelloWorld import *

def demo(argv):
    main_elm = CC_Elemental_HelloWorld(arglist=[])
    cc_S_Elemental_HelloWorld_std['CC_P_std_invoke'](main_elm, [])
    return 0

def target(*args):
  return demo, None

import sys
if __name__ == '__main__':
  import sys
  demo(sys.argv)
