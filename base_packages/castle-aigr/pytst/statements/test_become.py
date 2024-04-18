# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from . import  Dummy, verifyMark, verifyKids

from castle.aigr import Become




def test_1_simpleAssign():
    "a:=1"
    s=Become(targets=(Dummy('a'),),values=(Dummy(1),))
    verifyMark(s.targets[0],'a')
    verifyMark(s.values[0],1)



def test_if_kids():
    verifyKids(Become(targets=(),values=()))


