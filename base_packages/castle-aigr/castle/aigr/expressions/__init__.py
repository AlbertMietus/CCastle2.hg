# (C) Albert Mietus, 2024. Part of Castle/CCastle project


#from dataclasses import dataclass

from .. import AIGR

#@dataclass
class _expression(AIGR): pass #_kids = AIGR._kids

from .OpExpr import *
from .calls import *