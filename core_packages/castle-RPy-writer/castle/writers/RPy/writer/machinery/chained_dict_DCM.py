# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers import RPy
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node) ->  Block: # node : RPy.aigr.EventDispatchTable

        table_name = renderer._cc_S_dispatchTable(comp=node.comp, port=node.port)
        parent_table = renderer._cc_S_dispatchTable(comp=node.parentTable, port=node.port) if node.parentTable else 'None'

        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
        sub = Block();
        for (protocol, event), callable in node.map.items():
            sub+=f"'{renderer._CC_P_eventTrigger(str(protocol),event)}' : {renderer._CC_cls_prefix(node.comp)}.{callable},"
        sub+= '},' #end map
        sub+= f'parent={parent_table})',
        txt.sub(sub)

        logger.debug("M_DC_chained_dict.render_EventDispatchTable %s ==> %s", node, txt)
        return txt

