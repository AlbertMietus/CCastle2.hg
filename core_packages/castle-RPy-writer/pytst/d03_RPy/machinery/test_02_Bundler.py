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
    assert bundler.box("1", CCTypes.int) == expected

def test_1b_unbox_int(bundler):
    parm= "p1"
    expected = f"{parm}.value"
    assert bundler.unbox(parm) == expected

def test_2_box_manyTypes(bundler):
    CC_B_= 'CC_B_'
    for expr, typ, cast in [
            ("3/2",	  CCTypes.int,     CC_B_ + 'int' ),
            ("3/2",	  CCTypes.float,   CC_B_ + 'float'),
            ("True",  CCTypes.boolean, CC_B_ + 'boolean'),
            ("hello", CCTypes.string,  CC_B_ + 'string'), # same as above
            ]:
        expected = f"{cast}({expr})"
        assert bundler.box(expr, typ) == expected

def test_3_unbox_Any(bundler):
    #Unboxing does not depend on type ...
    parm= "any"
    expected = f"{parm}.value"
    assert bundler.unbox(parm) == expected


def test_99a_pack_returns_TextBlock(bundler):
    expected = "[], {}"
    txt = bundler.pack(arguments=(), formal_parameters=())
    assert txt == expected
    assert isinstance(txt, (str, Block))
    verify_ValidPython(txt)


def XXX_test_99b_unpack_returns_TextBlock(bundler):
    txt = bundler.unpack(formal_parameters=())
    assert isinstance(txt, (str, Block))
    verify_ValidPython(txt)


