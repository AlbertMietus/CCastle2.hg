# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from castle.monorail.base.visitors import Visitor

from ..aid.convert import fString_2_modulo
from ..aigr.dispatch_tables import Build_EventDispatchTable
from . walker import Walker
from . machinery import Machinery
from . portray import Portray

TextBlock = PTH.Optional[str|Block]

class Renderer(Visitor):
    _defaultType=str                      #used in Visitor, to return a default value of the right type

    def __init__(self, walker:PTH.Optional[Walker]=None, machinery:PTH.Optional[Machinery]=None, portray=None, **kw):
        super().__init__(**kw)
        self.walker = walker if walker else Walker()
        self.machinery = machinery if machinery else Machinery() # type: ignore[abstract] # Machinery-baseclass selects a subclass ad instance that one.
        self.portray = portray if portray else Portray(self)
        logger.debug("Using Machinery: %s,\t and Walker: %s", self.machinery,  self.walker)


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
            logger.debug("%s.render_subNodes: No subnodes --- node: %s" , type(node).__name__, node)
            return None

        txt = Block()
        logger.debug("%s.render_subNodes (len=%s)-> %s ---node: %s" ,  type(node).__name__, len(subnodes), subnodes, node)
        for next_node in subnodes if subnodes else []:
            txt += self.visit(next_node)
        return txt

    def visit_ComponentInterface(self, node)			-> TextBlock:
        interface_name = self.portray.cc_CI_elm_prefix(node.name)
        txt = Block(f'{interface_name} = buildin.CC_B_ComponentInterface(')
        txt.sub(Block((
            (f'name         = "{node.name}",'),
            (f'inherit_from = {self.portray.cc_CI_elm_prefix(node.based_on.name)},'), ## XXXX
            (f'ports        = {tuple(node.ports)},'),
            (f')'),
            )))
        return txt


    def visit_ComponentImplementation(self, node)		-> TextBlock:
        gen_cls_name = self.portray.CC_cls_prefix(node.name)
        isa_elm_name = self.portray.cc_C_elm_prefix(node.name)

        txt = Block((
            f"class {gen_cls_name}({self.portray.CompBase()}):",
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
        txt = Block()
        txt += self._render_ComponentClass(node)
        txt += self._DispatchTables(node)
        return txt

    def _render_ComponentClass(self, node) ->TextBlock:
        isa_elm_name = self.portray.cc_C_elm_prefix(node.name)
        elm = Block(f"{isa_elm_name} = buildin.CC_B_ComponentClass(")
        ind = Block(f"interface = {self.portray.cc_CI_elm_prefix(node.name)},")
        ind += ")"
        elm.sub(ind)
        return elm

    def _DispatchTables(self, node)             ->TextBlock:
        txt = Block()
        txt += self._EventDispatchTables(node)
        if True: #partial implementation: check we have only event-handlers
            for h in node.handlers:
                assert isinstance(h, aigr.EventHandler), f"Only EventHandlers are supported for now in DispatchTables; got {h}"
        return txt

    def _EventDispatchTables(self, node)           ->TextBlock:
        ports = [h.port for h in node.handlers]
        logger.debug("_EventDispatchTables: ports=%s -- node=%s", ports, node)

        tables =[]
        for port in ports: # How about (inheriterd ports that have no handlers here?)
            e_table = Build_EventDispatchTable(comp=node, port=port)
            tables.append(e_table)

        txt = Block()
        for table in tables:
            logger.debug("_EventDispatchTables: table=%s", table)
            txt += self.machinery.render_EventDispatchTable(self, table)
        return txt


    def _render_def(self, node, callDef_name=None) ->Block:
        if callDef_name is None:
            callDef_name = self.portray.callDef_name(node)
        parms = ', '.join(str(p.name) for p in node.parameters)
        return Block(f"def {callDef_name}(self, {parms}):")

    def visit_Method(self, node)						->  TextBlock:
        txt = self._render_def(node)
        txt.sub(self.render_subNodes(node))
        txt += self.depart(node)
        return txt

    def visit_Initializer(self, node)					->  TextBlock:   #BUSY
        txt = self._render_def(node, callDef_name="_init")
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
        logger.info("visit_Call: %s", node)   #XX info->debug
        if isinstance(node.callable, aigr.ID):
            callable = self.visit(node.callable)
            try: #HACK
                if isinstance(node.callable.context.reference, aigr.Method):
                    callable = "self."+callable
            except AttributeError: pass
        else:
            raise NotImplementedError(node)
        args=", ".join(str(self.visit(a)) for a in node.arguments) # XXX
        txt = f'{callable}({args})'
        logger.info("visit_Call: %s -> %s", node, txt)   #XX info->debug 
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
        if isinstance(node.context, aigr.Ref) and node.context.reference != None:
            return self._render_IDRef(node)
        # Any other .context has no effect
        txt = str(node)
        logger.debug("visit_ID: %s, Simply render as str: >>%s<<", node, txt)
        return txt

    def _render_IDRef(self,node):
        "Special case for ID's with a Ref() as .context"
        reference = node.context.reference
        if isinstance(reference, aigr.ID):
            logger.debug("_render_IDRef/ID: %s  ==> visit_ID(%s)", node, reference)
            return self.visit(reference)
        elif isinstance(reference, aigr.NamedNode):
            txt = str(reference.name)
            logger.error("_render_IDRef/NamedNode: Not implemented. HACK:(ref) >>%s<< for %sd", txt, node)
            return txt
        elif isinstance(reference, aigr.AIGR):
            txt = str(node)
            logger.error("_render_IDRef/AIGR: Not Implemented; use node, not ref. %s -> %s", node, txt)
            return txt
        else:
            txt = str(reference)
            logger.warning("visit_ID: %s Ref isn't a aigr-node Render context as str: >>%s<< ; fingers crossed", node, txt)
            return txt

    def visit_RPy_unit(self, node)						->  TextBlock:
        txt = Block()
        txt += self._file_header(node)
        txt += self.render_subNodes(node)
        return txt

# XXX ToDo: move 'CC' out of 'RPy' (`castle/writers/RPy_buildin`?) and fix here
    def _file_header(self, node) -> TextBlock:
        txt = """\
from castle.writers.RPy_buildin import buildin
from castle.writers.RPy_buildin import base
\n
"""
        return txt

    def visit_Become(self, node)						->  TextBlock: # BUSY
        if len(node.targets) != len(node.values):
            raise NotImplementedError("Number of targets and values does not match. That isn't implementation yet")
        assert len(node.targets) == 1, "Only single-assignment is supported"

        txt = Block()
        lhs, rhs = self.visit(node.targets[0]), self.visit(node.values[0])
        logger.info(f"XXX BECOME\t {lhs=} {rhs=} -- {node=}")

        txt += f"{lhs} = {rhs}"
        return txt

