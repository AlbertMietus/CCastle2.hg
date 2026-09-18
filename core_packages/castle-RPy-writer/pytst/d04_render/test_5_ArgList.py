# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest


from . import *

@pytest.mark.xfail(reason="Rendering.Call needs the new 'Bundler'")
def test_5a_argList_call_with_a_pos_Argument(my_renderer):
    expected = "call_1_Pos([CC_B_int(1)], {})"   # Educated Guess, by GH-CP (claude-haiku-4.5)
    named= aigr.Call(callable=ID('call_1_Pos'), arguments=(aigr.Argument(value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt == expected


@pytest.mark.xfail(reason="Rendering.Call needs the new 'Bundler'")
def test_5b_argList_call_with_a_named_arg(my_renderer):
    expected = "XXX TODO"
    named= aigr.Call(callable=ID('call_1_named'), arguments=(aigr.Argument(name=ID('a1'),value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt== expected
