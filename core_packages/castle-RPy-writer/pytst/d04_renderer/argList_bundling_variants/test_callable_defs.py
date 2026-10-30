# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.aigr import types as CC_types

"""Most _callables (the implementation of Method/etc) are no using Bundling. Only EventHandlers do"""


@pytest.mark.xfail
def test_1_Method_withNoParms_def_is_renderd_flat(my_renderer):
    expected ="""\
def foo0()
"""
    func = aigr.Method("foo0", parameters=())
    got = my_renderer.render(func)
    verify_line_by_line(expected, got)


@pytest.mark.xfail
def test_1_Method_with1Parm_def_is_renderd_flat(my_renderer):
    expected ="""\
def foo1(parm1)
"""
    func = aigr.Method("foo", parameters=(aigr.TypedParameter(name=ID('parm1'), type=CC_types.int),))
    got = my_renderer.render(func)
    verify_line_by_line(expected, got)

def test_10_EventHandlers_def_is_rendered_with_unBundling(my_renderer):
    expected="""\
def e_handler(self, pos, named):
    parm = CC_B_int.unbox(pos[0])
"""
    hndl = aigr.EventHandler("e_handler", protocol=ID("P1"), event=ID("E"), port=ID("p2"),
        parameters=(aigr.TypedParameter(name=ID('parm'), type=CC_types.int),))
    got = my_renderer.render(hndl)
    verify_line_by_line(expected, got)
