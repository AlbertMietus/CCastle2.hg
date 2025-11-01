# (C) Albert Mietus, 2025, Part of CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import ID
from castle import aigr

A_NAME = 'a_name'

@pytest.fixture
def anID():
   return ID(A_NAME)


def test_ID_equalityString(anID):
    assert isinstance(anID, ID)
    assert anID == A_NAME

def test_ID_NoContext_(anID):
    assert anID.context is None

def test_ID_context_Def():
    id = ID('with_def', context=aigr.Def()) 	# See below a nicer syntax: ID.Def()
    assert isinstance(id.context, aigr.Def)

def test_ID_context_Ref():
    id = ID('withref', context=aigr.Ref()) # See below a nicer syntax: ID.Ref()
    assert isinstance(id.context, aigr.Ref)

def test_ID_unusedSet():
    'Just check we can create the object'
    assert ID('notUsedYett', context=aigr.Set())

def test_ID_repr_NoContext(anID):
    assert repr(anID) == f"'{A_NAME}'"

def test_ID_repr_ContextDef():
    id = ID.Def('with_def')
    assert repr(id) == "ID(`with_def`/Def())"

def test_ID_repr_ContextRef():
    id = ID('with_ref', context=aigr.Ref())
    assert repr(id) == "ID(`with_ref`/Ref(reference=None))"

def test_DefID():
    id = ID.Def('autoDef')
    assert isinstance(id, ID)
    assert isinstance(id.context, aigr.Def)

def test_RefID_type(anID):
    id = ID.Ref('autoRef', context=anID)
    assert isinstance(id , ID)
    assert isinstance(id.context, aigr.Ref)
    assert id.context.reference is anID

def test_RefID_Ref(anID):
    "Same as above, but with explicit Ref"
    id = ID.Ref('autoRef', context=aigr.Ref(reference=anID))
    assert isinstance(id , ID)
    assert isinstance(id.context, aigr.Ref)
    assert id.context.reference is anID

def withPTH(dummy: ID.Ref[aigr.ID]) -> ID.Ref[aigr.ID]:
    return dummy

def test_withPTH(anID):
    oke = withPTH(anID) # mypy should be happy
    nok = withPTH(2)    # mypy should complain (but doesn't)
