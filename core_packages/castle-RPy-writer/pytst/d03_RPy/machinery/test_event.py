# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

import pytest

from castle import aigr
from castle.aigr import ID

from .. import my_renderer
from .. import verify_line_by_line, print_out
from .mocks import *


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


def test_1_EventToSub_noArgs(machinery, my_renderer):
    """///CastleCode::: .subElm.aPort.anEvent() """
    e = aigr.machinery.EventToSub(comp='XXX_self', receiver='self.subElm', event='anEvent', arguments=()) # XXX ToDo: Use ID.Ref (of ID?)
    expected='cc_S_subElm_aPort[(aPort, anEvent)]()' # 
    blck=machinery.render_EventToSub(renderer=my_renderer, node=e)
    verify_line_by_line(expected, str(blck))

