# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import  Dummy, verifyMark

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

