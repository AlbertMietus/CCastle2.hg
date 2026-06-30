# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *


###
### argList (see: :ref:`argList`)
###
### 1. Calling:
###    a) *Pack* all (castle) args (``list[aigr.Argument]``) into a list (called arglist) when calling a method (via dispatch_tables)
###    b) Call the callable, with only 1 arg: arglist
### 2) Definition
###    a) The callable has only 1 argument: arglist -- aside of self:-)
###    b) *Unpack* "arglist" XXX (still ``list[aigr.Argument]`` and/or using the tuple[aigr.TypedParameter] as definited in de callable DEFINITION

@pytest.mark.skip(reason="WRONG AIGR (as input to renderer) -- resulting text is not relevant")
def test_00_argList_call_with_a_DIRECT_fString(my_renderer):
    """"This is missing `aigr.Argument()`!!
        - The TestDoubles (eHW) is doing it this way ... (wrong)
        - The ``castle-TatSu-reader`` parser is adding aigr.Argument's!
    """
    logger.error("this test is using a WRONG aigr!! -- `Call.arguments` should use `aigr.Argument` no direct values")
    wrong_aigr = aigr.Call(callable=ID('call_args_should_use_Argument'), arguments=(aigr.fString("WRONG: use direct value"),))
    txt= my_renderer.render(wrong_aigr)
    logger.warning("WRONG_AIGR: renders to: %s", txt)
    assert False, f"{wrong_aigr=}"


# Now correctly: arguments=<list of aigr.Arguments>

def test_5a_argList_call_with_a_pos_Argument(my_renderer):
    expected = "XXX TODO"
    named= aigr.Call(callable=ID('call_1_Pos'), arguments=(aigr.Argument(value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt == expected



def xxx_test_5b_argList_call_with_a_named_arg(my_renderer):
    expected = "XXX TODO"
    named= aigr.Call(callable=ID('call_1_named'), arguments=(aigr.Argument(name=ID('a1'),value=1),))
    txt= my_renderer.render(named)

    logger.error("argList:: %s ==>%s", named, txt)   #XXX
    assert txt== expected
