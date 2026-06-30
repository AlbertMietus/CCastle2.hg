# (C) Albert Mietus 2025, Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                        # Python TypeHints

from castle import aigr
from . import ScaffolderNode

class ScaffolderBody(ScaffolderNode):
    _nodeCls = aigr.Body
    _kids_fields: frozenset[str] = frozenset({'statements'})


    def __len__(self):
        return len(self.node.statements)

    def __getitem__(self, index):
        "get one statement of the (real) body)"
        return self.node.statements[index]

    def expand(self, *s):
        "Add one or more statement to the (real) Body"
        self.node.statements +=s


