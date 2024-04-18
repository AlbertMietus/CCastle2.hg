# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints

from castle.aigr import AIGR
from castle.aigr import If

from dataclasses import dataclass


@dataclass
class Dummy(AIGR):
    mark: PTH.Any

    def __repr__(self):
        return f'<Dummy.{self.mark}>'


def verifyMark(dummy, mark):
    if mark is None:
        assert dummy is None
    else:
        assert isinstance(dummy, Dummy)
        assert dummy.mark == mark, f"Expecting mark: {mark}, but got {dummy.mark}"

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

def verifyKids(s):
    logger.debug("verifyKids: statements: %s", s)
    unique = Dummy('unique')
    for k in s._kids:
        logger.debug("verifyKid  getattr(s,%s,unique) (%s) != unique (%s) %s",
                         k, getattr(s,k,unique), unique, getattr(s,k,unique)!=unique)
        assert unique != getattr(s,k, unique), f"Kid `{k}` should exist in {s}, but doesn't"

def test_if_kids():
    verifyKids(If(test=Dummy('1/3'), body=Dummy('2/3'), orelse=Dummy('3/3')))
    verifyKids(If(test=Dummy('1/2'), body=Dummy('2/2')))

