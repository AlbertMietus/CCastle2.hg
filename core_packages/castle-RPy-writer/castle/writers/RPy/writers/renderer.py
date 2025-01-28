# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from ..base.visitors import Visitor

INDENT =' '*4
def indent(block: PTH.Sequence[str]|str, level: int, asStr=False)-> PTH.Sequence[str] | str:
    if isinstance(block, str):
        block = block.splitlines()
    _indent = INDENT * level
    block = [_indent + line for line in block]
    return '\n'.join(block)+'\n' if asStr else block


class Renderer(Visitor):

    def _CC_cls_prefix(self, name):			return 'CC_'   + str(name)
    def _cc_C_elm_prefix(self, name):		return 'cc_C_' + str(name)
    def _cc_CI_elm_prefix(self, name):		return 'cc_CI_' + str(name)
    def _CompBase(self):      				return 'buildin.CC_B_Component'

    def render(self, node: aigr.AIGR) ->str:
        txt = ""
        txt += self.visit(node)
        #txt += XXX subnodes
        txt += self.depart(node)
        return txt

    def visit_ComponentImplementation(self, node) -> str:
        gen_cls_name = self._CC_cls_prefix(node.name)
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        return (
            f"class {gen_cls_name}({self._CompBase()}):\n"
            f"\n"
            f"    def __init__(self, *args):\n"
            f"        buildin.CC_B_Component.__init__(self, isa={isa_elm_name})\n" # XXX isa
            f"        self._castle_init(*args)\n"
            f"\n")

    def depart_ComponentImplementation(self, node) -> str: #XXX Is this strcuture  needed?
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        return (
            f"{isa_elm_name} = buildin.CC_B_ComponentClass(\n"
            f"    interface = {self._cc_CI_elm_prefix(node.name)},\n"
            f")\n"
            f"\n")

    def visit_Method(lf, node) -> str:
        method_name = str(node.name)
        parms = ', '.join(str(p.name) for p in node.parameters)
        block = (
            f"def {method_name}(self, {parms}):",
            f'XXX',
            )
        return indent(block, level=1, asStr=True)

