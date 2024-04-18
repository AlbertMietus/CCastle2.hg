# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from . import  Dummy, verifyMark, verifyKids

from castle.aigr import If


def test_1a_if3():
    s = If(test=Dummy('if-test'),body=Dummy('then-body'), orelse=Dummy('else'))
    verifyMark(s.test, 'if-test')
    verifyMark(s.body, 'then-body')
    verifyMark(s.orelse,'else', )

def test_1a_if2():
    s = If(test=Dummy('if-test'),body=Dummy('then-body'))
    verifyMark(s.test,'if-test')
    verifyMark(s.body, 'then-body')
    verifyMark(s.orelse, None)

def test_2_if_missing():
    with pytest.raises(TypeError): If(test=Dummy('WRONG'))
    with pytest.raises(TypeError): If(body=Dummy('WRONG'))
    with pytest.raises(TypeError): If()


def test_if_kids():
    verifyKids(If(test=Dummy('1/3'), body=Dummy('2/3'), orelse=Dummy('3/3')))
    verifyKids(If(test=Dummy('1/2'), body=Dummy('2/2')))

