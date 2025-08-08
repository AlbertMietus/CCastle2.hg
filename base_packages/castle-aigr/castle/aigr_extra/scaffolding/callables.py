# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from castle.aigr import ID, NamedNode,  errors

from . import ScaffolderNameSpace

class ScaffolderNamedCallable(ScaffolderNameSpace):
    #_nodeCls :PTH.Type = aigr.statements.callables._Named_callable
    _nodeCls = aigr.statements.callables._Named_callable
