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

@pytest.mark.skip(reason="Events (especially to subs) are not needed for elemental")
def test_1_EventToSub_noArgs(machinery, my_renderer):
    """///CastleCode::: .subElm.aPort.anEvent()"""
    expected='cc_S_subElm_aPort[(aPort, anEvent)]()'
    e = aigr.machinery.EventToSub(
        comp     =aigr.ID.Ref('XXX_self',    context='XXX'),
        receiver =aigr.ID.Ref('self.subElm', context='XXX'),
        event     =aigr.ID.Ref('anEvent',    context='XXX'),
        arguments=()) 
    blck=machinery.render_EventToSub(renderer=my_renderer, node=e)
    verify_line_by_line(expected, str(blck))

