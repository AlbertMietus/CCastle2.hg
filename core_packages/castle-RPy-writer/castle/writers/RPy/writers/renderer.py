# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from ..base.visitors import Visitor
from . walker import Walker

TextBlock = PTH.Optional[str|Block]

class Renderer(Visitor):
    _defaultType=str

    walker = Walker() # XXXX

    def _CC_cls_prefix(self, name):			return 'CC_'   + str(name)
    def _cc_C_elm_prefix(self, name):		return 'cc_C_' + str(name)
    def _cc_CI_elm_prefix(self, name):		return 'cc_CI_' + str(name)
    def _CompBase(self):      				return 'buildin.CC_B_Component'


    def render(self, node: aigr.AIGR) ->str:
        txt = Block()
        txt += self.visit(node)
        subnodes = self.walker.visit(node)
        for next_node in subnodes if subnodes else []:
            txt += self.render(next_node)
        txt += self.depart(node)
        return str(txt)

    def visit_ComponentImplementation(self, node) -> TextBlock:
        gen_cls_name = self._CC_cls_prefix(node.name)
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        comp = Block((
            f"class {gen_cls_name}({self._CompBase()}):",
            f"",))
        init = Block(f"def __init__(self, *args):")
        init.sub(Block((
            f"buildin.CC_B_Component.__init__(self, isa={isa_elm_name})", # XXX isa
            f"self._castle_init(*args)",
            f"")))
        comp.sub(init)
        comp += ""
        return comp

    def depart_ComponentImplementation(self, node) -> TextBlock:
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        elm = Block(f"{isa_elm_name} = buildin.CC_B_ComponentClass(")
        ind = Block(f"interface = {self._cc_CI_elm_prefix(node.name)},")
        elm.sub(ind)
        elm += f")"
        elm += ""
        return elm

    def visit_Method(self, node) -> TextBlock:
        method_name = str(node.name)
        parms = ', '.join(str(p.name) for p in node.parameters)
        meth = Block(f"def {method_name}(self, {parms}):")
        body = Block(f'XXX')
        meth.sub(body)
        return meth

    def visit_Call(self, node) -> TextBlock:
        callable= self.visit(node.callable)
        args=", ".join(str(self.visit(a)) for a in node.arguments) # XXX
        return f'{callable}({args})'



    def visit_Constant(self, node) -> TextBlock:
        if node.type == aigr.types.string:
            return f"f'''{node.value}'''"
        elif isinstance(node.type, aigr.types._buildinNumber):
            return f"{node.value}"
        else:
            assert False, f"visit_Constant is not done  ... type={node.type}"

    def visit_ID(self, node) -> TextBlock: # GAM: Nog niet overal gebruikt (bijna niet)
        return str(node)
