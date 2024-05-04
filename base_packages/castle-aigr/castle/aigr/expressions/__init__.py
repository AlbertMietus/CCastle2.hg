# (C) Albert Mietus, 2024. Part of Castle/CCastle project


from .. import AIGR

#@dataclass
class _expression(AIGR): pass #_kids = AIGR._kids

from .operator_expressions import *
from .calls import *
