# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from .namespaces import ScaffolderNameSpace

class ScaffolderComponentImplementation(ScaffolderNameSpace):
    _nodeCls = aigr.ComponentImplementation



