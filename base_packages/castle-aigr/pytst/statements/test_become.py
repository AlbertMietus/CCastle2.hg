# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import  Dummy, verifyMark, verifyKids

from castle.aigr import Become




def test_1_simpleAssign():
    """ a:=1 """
    s=Become(targets=(Dummy('a'),),values=(Dummy(1),))
    verifyMark(s.targets[0],'a')
    verifyMark(s.values[0],1)

def test_2_MultipleAssignment():
    """ a,b := b,a -- works as expected...
    However, here, there is no implementation (only test the AIGR), and
    there is no need to support more then simpleAssignment now.
    We add it to the test, to verify the AIGR can handles sequences (tuples)
    """
    a,b = Dummy('a'), Dummy('b')
    s=Become(targets=(a,b), values=(b,a))
    for n, c in enumerate("ab"):
        verifyMark(s.targets[n],c)
    for n, c in enumerate(reversed("ab")):
        verifyMark(s.values[n],c)


def test_if_kids():
    verifyKids(Become(targets=(),values=()))


