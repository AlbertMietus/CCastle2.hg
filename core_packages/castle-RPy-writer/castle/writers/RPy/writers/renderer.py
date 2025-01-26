# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from ..base.visitors import Visitor

class Renderer(Visitor):

    CC_cls_prefix = 'CC_'
    CC_elm_prefix = 'cc'
    CompBase      = 'buildin.CC_B_Component'

    def render(self, node: aigr.AIGR) ->str:
        return self.visit(node)

    def visit_ComponentImplementation(self, node) -> str:
        gen_cls_name = self.CC_cls_prefix + str(node.name)
        return (
            f"class {gen_cls_name}({self.CompBase}):\n"
            "\n"
            "    def __init__(self, *args):\n"
            "        buildin.CC_B_Component.__init__(self, isa=cc_C_Elemental_HelloWorld)\n" # XXX isa
            "        self._castle_init(*args)\n"
            "\n")

