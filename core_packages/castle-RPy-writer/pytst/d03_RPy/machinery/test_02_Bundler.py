# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest

from castle.writers.RPy.writer.machinery import Bundler, NativeBundler
from castle.writers.RPy.aid import Block
from castle.aigr import types as CCTypes

from .fixtures import bundler
from .verify  import *


def test_0_Bundler_is_NativeBundler(bundler):
    assert isinstance(bundler, NativeBundler)


def test_1a_box_int(bundler):
    expr = "1"
    expected = f"CC_B_int({expr})"
    assert bundler.box("1",CCTypes.int) ==expected

def test_1b_unbox_int(bundler):
    parm= "p1"
    expected = f"{parm}.value"
    assert bundler.unbox(parm) == expected

    


def XXX_test_99a_pack_returns_TextBlock(bundler):
    txt = bundler.pack(arguments=(), formal_parameters=())
    assert isinstance(txt, (str, Block))
    verify_ValidPython(txt)


def XXX_test_99b_unpack_returns_TextBlock(bundler):
    txt = bundler.unpack(formal_parameters=())
    assert isinstance(txt, (str, Block))
    verify_ValidPython(txt)


