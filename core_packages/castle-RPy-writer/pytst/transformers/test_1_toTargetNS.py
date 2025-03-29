# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from types import ModuleType
import typing as PTH                                                                                  # Python TypeHints

from castle import aigr
from castle.writers.RPy import transformers

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental import HelloWorld
## HelloWorld is Module
## HelloWorld.Hello_World is Source_NS


def verify_same_nodes(src: aigr.namespaces._NameSpace, out: aigr.namespaces._NameSpace, names:PTH.Sequence[str]=()):
    for n in names if names else src.list_names():
        assert src.findNode(n) is out.findNode(n)
        logger.debug(f'Node: "{n}" is both in {out} as {src}')

def test_0_dummy():
    assert isinstance(HelloWorld, ModuleType)
    assert isinstance(HelloWorld.Hello_World, aigr.Source_NS)
    assert issubclass(transformers.RPy_file, aigr.AIGR)

def test_transformSource_NS():
    src = HelloWorld.Hello_World # Source_NS
    out = transformers.Source2RPy(src)
    assert isinstance(out, transformers.RPy_file), f'Expect a RPy_file type, got {out}'
    verify_same_nodes(src, out)
    verify_same_nodes(out, src)
