# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import  Dummy, verifyMark, verifyKids

from castle.aigr import Body

def test_0_Body_has_kids():
    verifyKids(Body())

def test_1_emptyBody():
    b = Body()
    assert len(b) == 0

def test_2_Body_withIndex():
    s1,s2 = Dummy('s1'), Dummy('s2')
    b = Body(statements=(s1,s2))
    assert len(b.statements) == 2
    verifyMark(b[0], 's1')
    verifyMark(b[1], 's2')

def test_3a_Body_canGrowOne():
    b = Body()
    s0 = Dummy('s0')
    b.expand(s0)  # One statement
    assert len(b.statements) == 1


def test_3a_Body_canGrowSome():
    b = Body(statements=(Dummy('s0'),))
    s1,s2 = Dummy('s1'), Dummy('s2')
    b.expand(s1,s1) # Multiple statements
    assert len(b.statements) == 3


