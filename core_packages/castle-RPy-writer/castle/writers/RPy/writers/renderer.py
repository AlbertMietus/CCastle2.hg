# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

from castle import aigr
from ..base.visitors import Visitor

class Renderer(Visitor):

    def CC_cls_prefix(self, name):		return 'CC_'   + str(name)
    def cc_elm_prefix(self, name):		return 'cc_C_' + str(name)
    def CompBase(self):      			return 'buildin.CC_B_Component'

    def render(self, node: aigr.AIGR) ->str:
        txt = ""
        txt += self.visit(node)
        #txt += XXX subnodes
        txt += self.depart(node)
        return txt

    def visit_ComponentImplementation(self, node) -> str:
        gen_cls_name = self.CC_cls_prefix(node.name)
        isa_elm_name = self.cc_elm_prefix(node.name)
        return (
            f"class {gen_cls_name}({self.CompBase()}):\n"
            f"\n"
            f"    def __init__(self, *args):\n"
            f"        buildin.CC_B_Component.__init__(self, isa={isa_elm_name})\n" # XXX isa
            f"        self._castle_init(*args)\n"
            f"\n")

    def depart_ComponentImplementation(self, node) -> str:
        isa_elm_name = self.cc_elm_prefix(node.name)
        return (
            f"{isa_elm_name} = buildin.CC_B_ComponentClass(\n"
            f"    name = \"{node.name}\",\n"
            f")\n"
            f"\n")

