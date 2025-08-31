# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block
from castle.monorail.base.visitors import Visitor

from ..aid.convert import fString_2_modulo
from . walker import Walker
from . machinery import Machinery

TextBlock = PTH.Optional[str|Block]

class Renderer(Visitor):
    _defaultType=str                      #used in Visitor, to return a default value of the right type

    def __init__(self, walker:PTH.Optional[Walker]=None, machinery:PTH.Optional[Machinery]=None, **kw):
        super().__init__(**kw)
        self.walker = walker if walker else Walker()
        self.machinery = machinery if machinery else Machinery() # type: ignore[abstract] # Machinery-baseclass selects a subclass ad instance that one.
        logger.debug("Using Machinery: %s,\t and Walker: %s", self.machinery,  self.walker)


    @staticmethod
    def _prefix(prefix:str, id) ->str:
        parts=str(id).split('.')
        ns, n = ".".join(parts[:-1]), parts[-1]
        if ns :ns+="."
        return ns+prefix+n

    def _CC_cls_prefix(self, name):			    return self._prefix('CC_',    name)                # generated cls for Component
    def _cc_C_elm_prefix(self, name):		    return self._prefix('cc_C_',  name)                # element (instantiated Component)
    def _cc_CI_elm_prefix(self, name):		    return self._prefix('cc_CI_', name)                # component-interface
    def _cc_S_dispatchTable(self, comp, port):  return self._prefix('cc_S_',  f'{comp}_{port}')    # (event) dispatch-table
    def _CompBase(self):      				    return 'buildin.CC_B_Component'


    def render(self, node: aigr.AIGR) ->str:
        """"`render` is the main entrypoint.
        It will call ``visit_*`` for `node`; where the class of `node` determines the ``*-suffix``.

        Typically, those visitors will
        - render the node itself
        - call render_subNodes() to render those subnodes
          - which uses the `walker` to find all subnodes
            (but not always, as some are "fixed")
        - call the self depart() -- another visitor, which default to no-op

        `render()` will always return a str --whereas the visitors return a TextBlock -- by converting it to a str."""

        logger.debug("Going to render %s", node)
        txt = Block()
        txt += self.visit(node)
        return str(txt)


    def render_subNodes(self, node)-> PTH.Optional[Block]:
        subnodes = self.walker.visit(node)
        if not subnodes:
            logger.debug("%s.render_subNodes: No subnodes --- node:" , type(node).__name__, node)
            return None

        txt = Block()
        logger.debug("%s.render_subNodes (len=%s)-> %s ---node: %s" ,  type(node).__name__, len(subnodes), subnodes, node)
        for next_node in subnodes if subnodes else []:
            txt += self.visit(next_node)
        return txt

    def visit_ComponentInterface(self, node)			-> TextBlock:
        interface_name = self._cc_CI_elm_prefix(node.name)
        txt = Block(f'{interface_name} = buildin.CC_B_ComponentInterface(')
        txt.sub(Block((
            (f'name         = "{node.name}",'),
            (f'inherit_from = {self._cc_CI_elm_prefix(node.based_on.name)},'), ## XXXX
            (f'ports        = {tuple(node.ports)},'),
            (f')'),
            )))
        return txt


    def visit_ComponentImplementation(self, node)		-> TextBlock:
        gen_cls_name = self._CC_cls_prefix(node.name)
        isa_elm_name = self._cc_C_elm_prefix(node.name)

        txt = Block((
            f"class {gen_cls_name}({self._CompBase()}):",
            f"",))

        init = Block(f"def __init__(self, *args):")
        init.sub(Block((
            f"buildin.CC_B_Component.__init__(self, isa={isa_elm_name})", # XXX isa
            f"self._castle_init(*args)",)))
        txt.sub(init)

        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt


    def depart_ComponentImplementation(self, node)		-> TextBlock:
        isa_elm_name = self._cc_C_elm_prefix(node.name)
        elm = Block(f"{isa_elm_name} = buildin.CC_B_ComponentClass(")
        ind = Block(f"interface = {self._cc_CI_elm_prefix(node.name)},")
        ind += ")"
        elm.sub(ind)
        return elm

    def _render_def(self, node) ->Block:
        callable_name = str(node.name)
        parms = ', '.join(str(p.name) for p in node.parameters)
        return Block(f"def {callable_name}(self, {parms}):")

    def visit_Method(self, node)						->  TextBlock:
        txt = self._render_def(node)
        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_EventHandler(self, node)					->  TextBlock:
        txt = self._render_def(node)
        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_Body(self, node)							->  TextBlock:
        txt = Block(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_VoidCall(self, node)						->  TextBlock:
        txt =  self.render_subNodes(node)
        txt += self.depart(node)
        return txt

    def visit_Call(self, node)							->  TextBlock:
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

    def visit__literal(self, node)						->  TextBlock:
        if node.type == aigr.types.string or node.type is None:
            return f"'''{node.value}'''"
        elif isinstance(node.type, aigr.types._buildinNumber):
            return f"{node.value}"
        else:
            assert False, f"visit_Constant is not done  ... type={node.type}"

    def visit_fString(self, node)						->  TextBlock:
        formater = node.formater; assert formater, "the fString.formater should be set in aigr"
        string, args = fString_2_modulo(node.value)
        if len(args) == 0:
            return f'''"{string}"'''
        return f'''"{string}" % ({", ".join(str(arg) for arg in args)},)'''

    def visit_ID(self, node)							->  TextBlock: # GAM: Nog niet overal gebruikt (bijna niet)
        return str(node)

    def visit_EventDispatchTable(self, node)			->  TextBlock:
        return self.machinery.render_EventDispatchTable(self, node)


    def visit_RPy_unit(self, node)						->  TextBlock:
        txt = Block()
        txt += """\
#hack (pre)
from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC import base

from castle.writers.RPy.CC.HACK import std   #XXX
from MACHINERY import MACHINERY
\n""" # XXX HACK of default?
        txt += self.render_subNodes(node)

        txt += """\
#hack (post)
if MACHINERY == 'dict':
    cc_S_Elemental_HelloWorld_std = {
        'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std
        }
else:
    assert False, "Set 'MACHINERY'!"
#end hack
"""
        return txt
