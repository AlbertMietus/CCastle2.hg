# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints


import pytest

from . import *
from .mocks import *
from .fixtures import machinery
from castle import aigr


def refID(name) ->aigr.ID.Ref:
    return aigr.ID.Ref(name, ID(name))

stubProto=aigr.EventProtocol('stubProto', events=[])
mockPort=aigr.Port("mockPort", direction=aigr.PortDirection.In, type=stubProto)


@pytest.mark.xfail(reason="Passing only due HACK in implementation")
def test_1_EventToSub_noArgs(machinery, my_renderer):
    """///CastleCode:::
       .subElm.mockPort.dummyEvent()"""

    expected="""cc_S_subElm_mockPort['CC_P_stubProto_dummyEvent'](self.subElm, [], {})"""

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

@pytest.mark.xfail(reason="Passing only due HACK in implementation")
def test_2_EventToSub_oneArgs(machinery, my_renderer):
    expected="""cc_S_subElm_mockPort['CC_P_stubProto_dummyEvent'](self.subElm, [CC_B_string('''foo''')], {})"""

    e = aigr.machinery.EventToSub(
        comp     = refID('self'),
        receiver = refID('self.subElm'),
        inport   = aigr.ID.Ref('mockPort', mockPort),
        event    = refID('dummyEvent'),
        arguments= [aigr.Argument(value=aigr.Constant(value="foo", type=aigr.types.string))])


    blck = machinery.render_EventToSub(renderer=my_renderer, node=e)
    verify_line_by_line(expected, str(blck))
