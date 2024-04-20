# (C) Albert Mietus, 2024. Part of Castle/CCastle project

import pytest
from castle.aigr import expressions, ID


def test_call():
    c = expressions.Call(callable=ID('foo'), arguments=())
    assert str(c.callable) == 'foo'
    assert c.arguments==()

def test_call_noArgs():
    c = expressions.Call(callable=ID('foo'))
    assert str(c.callable) == 'foo'
    assert c.arguments==()
