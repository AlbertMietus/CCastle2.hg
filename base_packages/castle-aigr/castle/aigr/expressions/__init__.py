# (C) Albert Mietus, 2024. Part of Castle/CCastle project


from .. import AIGRNode

#@dataclass
class _expression(AIGRNode): pass #_kids = AIGR._kids

from .operator_expressions import *
from .calls import *
from .literals import *
