# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from .. import verifyKids

from castle.aigr import expressions, ID
from castle import aigr 

def test_call():
    c = expressions.Call(callable=ID('foo'), arguments=())
    assert str(c.callable) == 'foo'
    assert c.arguments==()
    verifyKids(c)

def test_call_noArgs():
    c = expressions.Call(callable=ID('foo'))
    assert str(c.callable) == 'foo'
    assert c.arguments==()
    verifyKids(c)


def verify_Part(p, base=None, attribute=None, index=None):
    assert p.base      == base
    assert p.attribute == attribute
    assert p.index     == index

def test_Part_attribute():
    c = expressions.Part(base=ID('base'), attribute=ID('attribute'))
    verify_Part(c, base='base', attribute='attribute')

def test_Part_index():
    c = expressions.Part(base=ID('base'), index=ID('index'))
    verify_Part(c, base='base', index='index')

def test_Part_onePart():
    with pytest.raises(aigr.errors.PartError):
        expressions.Part(base=ID('base'))

def test_Part_notBoth():
    with pytest.raises(aigr.errors.PartError):
        expressions.Part(base=ID('base'), attribute=ID('attribute'), index='index')
