# (C) Albert Mietus, 2025, Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
import typing as PTH                                                                                  # Python TypeHints
from dataclasses import dataclass, KW_ONLY

from castle.aigr import ID
from castle import aigr

A_NAME = 'a_name'

@pytest.fixture
def anID():
   return ID(A_NAME)


def test_ID_equalityString(anID):
    assert isinstance(anID, aigr.ID)
    assert anID == A_NAME

def test_ID_NoContext_(anID):
    assert anID.context is None

def test_ID_context_Def():
    id = ID('with_def', context=aigr.Def())
    assert isinstance(id.context, aigr.Def)

def test_ID_context_Ref():
    id = ID('withref', context=aigr.Ref())
    assert isinstance(id.context, aigr.Ref)

def test_ID_unusedSet():
    'Just check we can create the object'
    assert ID('notUsedYett', context=aigr.Set())

def test_ID_repr_NoContext(anID):
    assert repr(anID) == f"'{A_NAME}'"

def test_ID_repr_ContextDef():
    id = ID('with_def', context=aigr.Def())
    assert repr(id) == "ID(`with_def`/Def())"

def test_ID_repr_ContextRef():
    id = ID('with_ref', context=aigr.Ref())
    assert repr(id) == "ID(`with_ref`/Ref(reference=None))"
