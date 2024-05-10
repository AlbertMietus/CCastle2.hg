 # (C) Albert Mietus, 2024. Part of Castle/CCastle project


from .. import AIGR

#from dataclasses import dataclass
#@dataclass
class _statement(AIGR): pass #_kids = AIGR._kids

from .simple import *
from .flow import *
from .compounds import *
from .defs import *
from .callables import *
