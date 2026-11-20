# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints


import pytest

from . import *
from .mocks import *
from .fixtures import machinery
from castle import aigr

"""
aigr.machinery.EventToSub(
    comp:       'ID.Ref[componentInterface]', ##sender
    receiver:   'ID.Ref[componentInterface]',
    event:      'ID.Ref[Event]',
    arguments: 'PTH.Sequence[Argument]',
) -> None
"""
"""
        cc_S_Elemental_HelloWorld_std['CC_P_std_invoke'](main_elm)
"""

def refID(name) ->aigr.ID.Ref:
    return aigr.ID.Ref(name, ID(name))

stubProto=aigr.EventProtocol('stubProto', events=[])
mockPort=aigr.Port("mockPort", direction=aigr.PortDirection.In, type=stubProto)


def test_1_EventToSub_noArgs(machinery, my_renderer):
    """///CastleCode:::
       .subElm.mockPort.dummyEvent()"""

    expected="""cc_S_subElm_mockPort[CC_P_stubProto_dummyEvent](subElm, [], {})"""

    e = aigr.machinery.EventToSub(
        comp     = refID('self'),
        receiver = refID('self.subElm'),
        inport   = aigr.ID.Ref('mockPort', mockPort),
        event    = refID('dummyEvent'),
        arguments=())

    logging.warning(""""test_1_EventToSub_noArgs::\
    It works, but the implementation uses an hack ---\
    .. seealso:: chained_dict_DCM::render_EventToSub()
    """)
    blck = machinery.render_EventToSub(renderer=my_renderer, node=e)
    verify_line_by_line(expected, str(blck))


