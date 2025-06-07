# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy.aid import Block

from . import Machinery, _M_DC_dict

@Machinery.register('DirectCall.dict.chained', "chained.dict", "chained_dict", "chained-dict", default=True)
class M_DC_chained_dict(_M_DC_dict):

    def render_EventDispatchTable(self, renderer, node :aigr.machinery.eDispatchTable) 						->  Block:
        txt = Block()
        txt += """ HACK XXXX
cc_S_Elemental_HelloWorld_std = {
    'CC_P_std_invoke' : CC_Elemental_HelloWorld.std_invoke__std
    }
/hack
"""
        return txt
