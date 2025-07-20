# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node :aigr.EventDispatchTable) ->  Block: #XXX node:EventDispatchTable
        assert False, "M_DC_chained_dict::render_EventDispatchTable needs to be implemented"
        txt = Block()
        return txt




#OLD#    def _render_EDT_forPort(self, renderer, node, port) -> Block: #XXX node:EventDispatchTable
#OLD#        comp = node.component
#OLD#        if isinstance(comp, aigr.ComponentImplementation):
#OLD#            comp = comp.interface
#OLD#        assert isinstance(comp, aigr.ComponentInterface), "EventDispatchTable should refer to a comp (Interface or Implementation)"
#OLD#        parent = comp.based_on
#OLD#
#OLD#        table_name   = renderer._cc_S_dispatchTable(comp.name, port)
#OLD#        parent_table = renderer._cc_S_dispatchTable(parent.name, port) if parent else 'None'
#OLD#
#OLD#        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
#OLD#        sub = self._render_EDT_events_forPort(renderer, node, port)
#OLD#        sub += '},'
#OLD#        sub += f'parent={parent_table})'
#OLD#        txt.sub(sub)
#OLD#        return txt
#OLD#
#OLD#    def _render_EDT_events_forPort(self, renderer, node, port) -> Block: #XXX node:EventDispatchTable
#OLD#        txt = Block()
#OLD#        for event in node.list_events_for_port(port):
#OLD#            txt += f"{event} : {node.find_byNames(port, event)},"
#OLD#        return txt
