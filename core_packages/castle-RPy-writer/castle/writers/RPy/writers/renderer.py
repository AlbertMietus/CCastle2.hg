# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from ..base.visitors import Visitor
from . walker import Walker
from ..aid.convert import fString_2_modulo


TextBlock = PTH.Optional[str|Block]

class Renderer(Visitor):
    _defaultType=str

    walker = Walker() # XXXX

    def _CC_cls_prefix(self, name):			return 'CC_'   + str(name)
    def _cc_C_elm_prefix(self, name):		return 'cc_C_' + str(name)
    def _cc_CI_elm_prefix(self, name):		return 'cc_CI_' + str(name)
    def _CompBase(self):      				return 'buildin.CC_B_Component'


    def render(self, node: aigr.AIGR) ->str:
        """"`render` is the main entrypoint.
        It will call ``visit_*`` for `node`; where the class of `node` determines the ``*-suffix``.

        Typically, those visitors will
        - render the node itself
        - call render_subNodes() to render those subnodes
          - which uses the `walker` to find all subnodes
            (but not always, as some are "fixed"
        - call the depart_<node> visitor (when relevant -- default a no-op)

        `render()` will always return a str --whereas the visitors return a TextBlock -- by converting it to a str
        """

        logger.debug("Going to render %s", node)
        txt = Block()
        txt += self.visit(node)
        return str(txt)


    def render_subNodes(self, node)-> Block:
        subnodes = self.walker.visit(node)
        if not subnodes:
            return None

        txt = Block()
        logger.debug("render_subNodes: %s" , subnodes)
        for next_node in subnodes if subnodes else []:
            txt += self.visit(next_node)
        return txt


    def visit_ComponentImplementation(self, node) -> TextBlock:
        gen_cls_name = self._CC_cls_prefix(node.name)
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        comp = Block((
            f"class {gen_cls_name}({self._CompBase()}):",
            f"",))
        init = Block(f"def __init__(self, *args):")
        init.sub(Block((
            f"buildin.CC_B_Component.__init__(self, isa={isa_elm_name})", # XXX isa
            f"#XXX: init instance vars -- ToDo",
            f"self._castle_init(*args)",)))
        comp.sub(init)
        return comp

    def depart_ComponentImplementation(self, node) -> TextBlock:
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        elm = Block(f"{isa_elm_name} = buildin.CC_B_ComponentClass(")
        ind = Block(f"interface = {self._cc_CI_elm_prefix(node.name)},")
        elm.sub(ind)
        elm += f")"
        elm += ""
        return elm

    def _render_def(self, node) ->Block:
        callable_name = str(node.name)
        parms = ', '.join(str(p.name) for p in node.parameters)
        return Block(f"def {callable_name}(self, {parms}):")

    def visit_Method(self, node) -> TextBlock:
        txt = self._render_def(node)
        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_EventHandler(self, node) -> TextBlock:
        txt = self._render_def(node)
        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_VoidCall(self, node) -> TextBlock:
        return self.render_subNodes(node)

    def visit_Call(self, node) -> TextBlock:
        callable= node.callable
        try:
            context  = callable.context
            reference = context.reference
            base = 'self.' if isinstance(reference, aigr.Method) else ''
        except AttributeError:
            base = ''
            reference= '[|absend]|'

        args=", ".join(str(self.visit(a)) for a in node.arguments) # XXX
        txt = f'{base}{callable}({args})'
        return txt


    def visit__literal(self, node) -> TextBlock:
        if node.type == aigr.types.string or node.type is None:
            return f"f'''{node.value}'''"
        elif isinstance(node.type, aigr.types._buildinNumber):
            return f"{node.value}"
        else:
            assert False, f"visit_Constant is not done  ... type={node.type}"


    def visit_fString(self, node) -> TextBlock:
        formater = node.formater; assert formater, "the fString.formater should be set in aigr"
        string, args = fString_2_modulo(node.value)
        return f'''"{string}" % ({", ".join(str(arg) for arg in args)},)'''


    def visit_ID(self, node) -> TextBlock: # GAM: Nog niet overal gebruikt (bijna niet)
        return str(node)
