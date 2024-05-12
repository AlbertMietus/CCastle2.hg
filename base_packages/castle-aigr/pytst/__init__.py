# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints

from castle.aigr import AIGR
from castle.aigr import If

import dataclasses
from dataclasses import dataclass


@dataclass
class Dummy(AIGR):
    mark: PTH.Any

    def __repr__(self):
        return f'<Dummy.{self.mark}>'


def verifyMark(dummy, mark):
    logger.debug("verifyMark: dummy=%s, mark=%s", dummy, mark)
    if mark is None:
        assert dummy is None
    else:
        assert isinstance(dummy, Dummy)
        assert dummy.mark == mark, f"Expecting mark: {mark}, but got {dummy.mark}"


def verifyKids(s):
    logger.debug("verifyKids of %s cls._kids= %s", s, type(s)._kids)
    unique = Dummy('unique')
    for k in s._kids:
        logger.debug("verifyKid  getattr(s,%s,unique) (%s) != unique (%s) %s",
                         k, getattr(s,k,unique), unique, getattr(s,k,unique)!=unique)
        assert unique != getattr(s,k, unique), f"Kid `{k}` should exist in {s}, but doesn't"


def verifyisDataClass(cls):
    logger.debug("verifyisDataClass: %s ", cls)
    assert dataclasses.is_dataclass(cls) # This will also pass when cls inherits from a dataclass
    my_init = getattr(cls, '__init__')
    inherited_init = getattr(cls.mro()[1], '__init__')
    assert my_init is not inherited_init, f"Probably you subclasses a dataclass, but forgot @dataclass for {cls}"
