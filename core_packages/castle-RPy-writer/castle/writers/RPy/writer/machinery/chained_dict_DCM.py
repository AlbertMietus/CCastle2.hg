# (C) Albert Mietus, 2025. 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers import RPy
from castle.writers.RPy.aid import Block

from castle.writers.RPy.aigr.dispatch_tables import EventDispatchTable

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node) ->  Block: #Node : RPy.aigr.EventDispatchTable
        table= PTH.cast(EventDispatchTable, node)
        table_name = renderer.portray.cc_S_dispatchTable(comp=table.comp, port=table.port)
        parent_table = renderer.portray.cc_S_dispatchTable(comp=table.parentTable.comp, port=table.port) if table.parentTable else 'None' # XXXX

        logger.debug("render_EventDispatchTable(node/table=%s), table_name=%s, parent_table=%s", node, table_name, parent_table)

        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
        sub = Block();
        for (protocol, event), callable in table.map.items():
            sub+=f"'{renderer.portray.CC_P_eventTrigger(protocol ,event)}' : {renderer.portray.CC_cls_prefix(table.comp)}.{callable},"
        sub+= '},' #end map
        sub+= f'parent={parent_table})',
        txt.sub(sub)

        logger.debug("M_DC_chained_dict.render_EventDispatchTable %s ==> %s", table, txt)
        return txt

    def render_EventOverPort(self, renderer, node) ->  Block:
        raise NotImplementedError


    def render_EventToSub(self, renderer, node) ->  Block:
        node = PTH.cast(aigr.machinery.EventToSub, node)
        logger.debug(f"XXX render_EventToSub:: node={node}")

        logging.error(""""chained_dict_DCM::render_EventToSub:: `protocol`\
        The algorithm to find the Protocol (-name) is an HACK!""")
        protocol = node.inport.context.reference.type.name           #XXX HACK

        logging.error(""""chained_dict_DCM::render_EventToSub:: `comp`\
        The DispatchTable is now hardcoded --with the name of the sub (var) ... \
        That is WRONG! We should dynamicly find it via the pin --- to be designed""")
        comp = str(node.receiver).removeprefix('self.')

        elm  = str(node.receiver)
        dispatch_table = renderer.portray.cc_S_dispatchTable(comp=comp, port=str(node.inport))
        key = renderer.portray.CC_P_eventTrigger(protocol=protocol, event=node.event)

        # C&P: from renderer.py::_render_CallArgs_bundled
        # self <-> renderer
        boxed_args = [renderer.machinery.arg_bundler.box(renderer.visit(a), a.value.type) for a in node.arguments]
        packed  = renderer.machinery.arg_bundler.pack(arguments=boxed_args, formal_parameters=None)  # XXX OptionalTypedParameterList is needed

        txt = Block(f"{dispatch_table}['{key}']({elm}, {packed})\n")
        logger.info(f"XXX render_EventToSub:: {str(txt)=}")

        return txt
        raise NotImplementedError










