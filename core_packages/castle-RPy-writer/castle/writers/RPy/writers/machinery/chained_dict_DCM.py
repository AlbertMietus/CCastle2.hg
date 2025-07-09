# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node :aigr.EventDispatchTable) ->  Block: #XXX node:EventDispatchTable
        all_txt = Block()
        for port in node.list_ports():
            all_txt += self._render_EDT_forPort(renderer, node, port=port)
        return all_txt


    def _render_EDT_forPort(self, renderer, node, port) -> Block: #XXX node:EventDispatchTable
        comp = node.component
        if isinstance(comp, aigr.ComponentImplementation):
            comp = comp.interface
        assert isinstance(comp, aigr.ComponentInterface), "EventDispatchTable should refer to a comp (Interface or Implementation)"
        parent = comp.based_on

        table_name   = renderer._cc_S_dispatchTable(comp.name, port)
        parent_table = renderer._cc_S_dispatchTable(parent.name, port) if parent else 'None'

        txt = Block(f'{table_name} = buildin.machinery.ChainedDict(map={{')
        sub = self._render_EDT_events_forPort(renderer, node, port)
        sub += '},'
        sub += f'parent={parent_table})'
        txt.sub(sub)
        return txt

    def _render_EDT_events_forPort(self, renderer, node, port) -> Block: #XXX node:EventDispatchTable
        txt = Block()
        for event in node.list_events_for_port(port):
            txt += f"{event} : {node.find_byNames(port, event)},"
        return txt
