# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers import RPy
from castle.writers.RPy.aid import Block

from castle.writers.RPy.aigr.dispatch_tables import EventDispatchTable

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node) ->  Block: # node : RPy.aigr.EventDispatchTable
        table= PTH.cast(EventDispatchTable, node)
        table_name = renderer.portray.cc_S_dispatchTable(comp=table.comp, port=table.port)
        parent_table = renderer.portray.cc_S_dispatchTable(comp=table.parentTable.comp, port=table.port) if table.parentTable else 'None' # XXXX

        logger.info("render_EventDispatchTable(node/table=%s), table_name=%s, parent_table=%s", node, table_name, parent_table) 

        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
        sub = Block();
        for (protocol, event), callable in table.map.items():
            sub+=f"'{renderer.portray.CC_P_eventTrigger(protocol ,event)}' : {renderer.portray.CC_cls_prefix(table.comp)}.{callable},"
        sub+= '},' #end map
        sub+= f'parent={parent_table})',
        txt.sub(sub)

        logger.debug("M_DC_chained_dict.render_EventDispatchTable %s ==> %s", table, txt)
        return txt

