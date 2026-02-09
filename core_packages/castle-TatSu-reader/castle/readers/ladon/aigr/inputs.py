# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from pathlib import Path

from castle.aigr.namespaces import _NameSpace
from castle.aigr_extra.scaffolding import ScaffolderNameSpace

@dataclass
class FileNS(_NameSpace):
    """A temporally (nameless) namespace to store the 'namedNodes' in a file, before the `Source_NS` is build"""
    name = "TEMP"

class ScaffolderFileNS(ScaffolderNameSpace):
    _nodeCls :type =FileNS

    def __iter__(self):
        for e in self.node._ns.values():
            yield e

