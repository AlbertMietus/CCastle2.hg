# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest


from . import *

def test_0_simpleIntArg_call_is_packed_and_boxed(my_renderer):
    """A bootstap/simple test: 1 arg, wich is `1` -- se below for variations"""
    call = aigr.Call(callable=ID('call_1_Pos'),
                         arguments=(
                             aigr.Argument(aigr.Constant(value=1, type=aigr.int)),))   #XXX ConstantInt can carry an int ....
    txt= my_renderer.render(call)
    assert txt == "call_1_Pos([CC_B_int(1)], {})\n"


def test_1a_Any_Single_intArg(my_renderer):
    "CCastle:`aCall([int-value])`"""
    template = "aCall([CC_B_int(%s)], {})\n"

    for v in (1,2, 10, 9999, 123456789012345678901234567890):
        call = aigr.Call(callable=ID('aCall'), arguments=( aigr.Argument(aigr.Constant(value=v, type=aigr.int)),))
        txt= my_renderer.render(call)
        logging.info("aCall(%s) ==> %s", v, txt)
        assert txt == template %v

@pytest.mark.slow
def test_1b_veryBig_Single_intArg(my_renderer):
    template = "aCall([CC_B_int(%s)], {})\n"
    #bigNum = 9999 ** 999 * 99 ** 99 * 99 ** 9 # 4212 digits --- VERY SLOW when logging!
    bigNum = 999 ** 999 # an int of 2997 digits -- SLOW, but acceptable for logging
    txt = my_renderer.render(aigr.Call(callable=ID('aCall'), arguments=( aigr.Argument(aigr.Constant(value=bigNum, type=aigr.int)),)))
    assert txt == template % bigNum


def test_2_SomeIntArgs_call_are_packed_and_boxed(my_renderer):
    numbers = (1, -2, 3, -4, +5)
    expected = "callNumbers([" +  ', '.join(f'CC_B_int(%s)' % n  for n in numbers) + "], {})\n"

    txt = my_renderer.render(aigr.Call(callable=ID('callNumbers'), arguments=
             tuple(aigr.Argument(aigr.Constant(value=n, type=aigr.int)) for n in numbers)))
    assert txt == expected

def test_3_SomeFloatArgs_call_are_packed_and_boxed(my_renderer):
    numbers = (-1.0,  2,7, 3.14)
    expected = "callFloats([" +  ', '.join(f'CC_B_float(%s)' % n  for n in numbers) + "], {})\n"

    txt = my_renderer.render(aigr.Call(callable=ID('callFloats'), arguments=
             tuple(aigr.Argument(aigr.Constant(value=n, type=aigr.float)) for n in numbers)))
    assert txt == expected


@pytest.mark.xfail(reason="'Bundler' && visit_Argument() need work")
def test_99_argList_call_with_a_named_arg(my_renderer):
    expected = "XXX TODO"
    named= aigr.Call(callable=ID('call_1_named'), arguments=(aigr.Argument(name=ID('a1'),value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt== expected
