# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node) ->  Block: #XXX node:EventDispatchTable -- not in aigr, but PRY one

        table_name = renderer._cc_S_dispatchTable(comp=node._comp, port=node._port)
        parent_table = renderer._cc_S_dispatchTable(comp=node._parentTable, port=node._port) if node._parentTable else 'None'

        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
        sub = Block();
        for e,h in node.map.items():
            sub+=f"'{e}' : {h},"
        sub+= '},' #end map
        sub+= f'parent={parent_table})',
        txt.sub(sub)

        logger.debug("M_DC_chained_dict.render_EventDispatchTable %s ==> %s", node, txt)
        return txt

