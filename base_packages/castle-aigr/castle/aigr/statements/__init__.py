 # (C) Albert Mietus, 2024. Part of Castle/CCastle project


from .. import AIGR, AIGRNode

#from dataclasses import dataclass

#@dataclass
class _statement(AIGRNode): pass

from .simple import *
from .flow import *
from .compounds import *
from .defs import *
from .callables import *
