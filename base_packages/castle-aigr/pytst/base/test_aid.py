# (C) Albert Mietus, 2025, Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from castle import aigr
from castle.aigr import ID

a_name="ThisIsStr"


def test_TypedParameter_str_becomes_ID():
    t = aigr.TypedParameter(a_name, type=aigr.int)
    name = t.name
    assert isinstance(name, aigr.ID)
    assert str(name) == a_name

def test_TypedParameter_ID_is_ID():
    t = aigr.TypedParameter(ID(a_name), type=aigr.int)
    name = t.name
    assert isinstance(name, aigr.ID)
    assert str(name) == a_name



def test_Argument_str_becomes_ID():
    t = aigr.Argument(value='dummy', name=a_name)
    name = t.name
    assert isinstance(name, aigr.ID)
    assert str(name) == a_name

def test_Argument_ID_is_ID():
    t = aigr.Argument(value='dummy', name=ID(a_name))
    name = t.name
    assert isinstance(name, aigr.ID)
    assert str(name) == a_name

