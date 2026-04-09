# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.writers.RPy.writer.machinery import Bundler, NativeBundler
from castle.writers.RPy.aid import Block

@pytest.fixture
def bundler():
    return Bundler()  # type: ignore[reportAbstractUsage, abstract]


def test_0a_Bundler_is_NativeBundler(bundler):
    assert isinstance(bundler, NativeBundler)

def test_0b_pack_and_unpack_return_TextBlock(bundler):
    txt = bundler.pack(arguments=(), signature=())
    assert isinstance(txt, (str, Block))
    txt = bundler.unpack(signature=())
    assert isinstance(txt, (str, Block))

class NonBundlerStub(Bundler):
    """When pack/unpack are not implemented, those function should raise 'NotImplementedError'
       However, we need a trick (see below) to make sure we can instance NonBundlerStub"""
    def __new__(cls, hint:str="", **kwargs):
        return object.__new__(cls)
    def pack(self, *t, **kw):
        return super().pack(*t,**kw)      # type: ignore # we need this trick to test ...
    def unpack(self, *t, **kw):
        return super().unpack(*t,**kw)    # type: ignore # we need this trick to test ...

def test_0c_abstractmethods_raises():
    b = NonBundlerStub()
    try:
        b.pack(arguments=(), signature=())
        assert False, "shoud raise NotImplementedError"
    except  NotImplementedError: pass
    try:
        b.unpack(signature=())
        assert False, "shoud raise NotImplementedError"
    except  NotImplementedError: pass


