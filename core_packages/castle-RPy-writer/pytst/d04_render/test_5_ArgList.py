# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest


from . import *

def test_0_simpleIntArg_call_is_packed_and_boxed(my_renderer):
    """A bootstap/simple test: 1 arg, wich is `1` -- se below for variations"""
    named= aigr.Call(callable=ID('call_1_Pos'), arguments=(
        aigr.Argument(aigr.Constant(value=1, type=aigr.int)),))   #XXX ConstantInt can carry an int ....
    txt= my_renderer.render(named)
    assert txt == "call_1_Pos([CC_B_int(1)], {})\n"


def test_1_Any_Single_intArg(my_renderer):
    "CCastle:`aCall([int-value])`"""
    template = "aCall([CC_B_int(%s)], {})\n"

    for v in (1,2, 10, 9999, 123456789012345678901234567890):
        named= aigr.Call(callable=ID('aCall'), arguments=( aigr.Argument(aigr.Constant(value=v, type=aigr.int)),))
        txt= my_renderer.render(named)
        logging.info("aCall(%s) ==> %s", v, txt)
        assert txt == template %v


def test_2_veryBig_Single_intArg(my_renderer):
    template = "aCall([CC_B_int(%s)], {})\n"
    bigNum = 999 ** 999 # an int of 2997 digits (upto 4300 digits will work, but is extremely SLOW 
    txt = my_renderer.render(aigr.Call(callable=ID('aCall'), arguments=( aigr.Argument(aigr.Constant(value=bigNum, type=aigr.int)),)))
    assert txt == template % bigNum


@pytest.mark.xfail(reason="'Bundler' && visit_Argument() need work")
def test_5b_argList_call_with_a_named_arg(my_renderer):
    expected = "XXX TODO"
    named= aigr.Call(callable=ID('call_1_named'), arguments=(aigr.Argument(name=ID('a1'),value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt== expected
