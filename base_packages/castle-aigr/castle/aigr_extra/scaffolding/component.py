# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import typing as PTH                                        # Python TypeHints

from castle import aigr
from . import ScaffolderNode

class ScaffolderBody(ScaffolderNode):
    _nodeCls = aigr.Body

    def __getitem__(self, index):
        """"Convenient function: return a statements in the body, based on an index (numbering like a list)"""
        return self.node.statements[index]

    def __len__(self):
        return len(self.node.statements)

    def expand(self, *s):
        """Convenient function: add one of more statements to the Body"""
        self.node.statements +=s


