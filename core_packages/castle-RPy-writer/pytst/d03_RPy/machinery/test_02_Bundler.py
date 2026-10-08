# (C) Albert Mietus, 2026. Part of Castle/CCastle project

"""Test the four methods of Bundler individually, in isolation;   using the 'NativeBundler'

   * It is verified that NativeBundler is used.
   * See e.g. :file:`test_11_bundler-simple.py` for an intergration test

   .. note:: Render->Machinery ->Bundler

      The :class:`Bundler` is part of the Machinery, and only called during rendering!

      Typically, box/pack for aigr.Call --'calling a function'
      * to pack all arguments into `pos` and `named`;
      * all callables SHOULD have the same signature, for the rpython translater

     In the function *def*, this is undone.
     * `pos` and `named` are "hardcoded" parameters in every function defintion
     * the list `pos` is `unpack()ed` in the lines directly below  the def
     * For every Castle-parameters, one line is generated, to unpack/unbox parameter into a local var

NOTE: unbox used to be read .value -- but that is wrong
"""

import logging; logger = logging.getLogger(__name__)

import pytest

from castle.writers.RPy.writer.machinery import Bundler, NativeBundler
from castle.writers.RPy.aid import Block
from castle.aigr import types as CCTypes, TypedParameter

from .fixtures import bundler
from .verify  import *
from ...verify import verify_line_by_line

"""Note:: positional arg are NOT supported yet -- and not tested. The bundler's API doesn't even have it:-)"""

def test_0_Bundler_is_NativeBundler(bundler):
    assert isinstance(bundler, NativeBundler), "This test-set is valid for the NativeBundler ONLY!"

def test_1a_box_int(bundler):
    expr = "1"
    expected = f"CC_B_int({expr})"
    assert bundler.box("1", CCTypes.int) == expected

def test_1a_box_manyTypes(bundler):
    CC_B_= 'CC_B_'
    for expr, typ, wrap in [
            ("3/2",	  CCTypes.int,     CC_B_ + 'int' ),
            ("3/2",	  CCTypes.float,   CC_B_ + 'float'),
            ("True",  CCTypes.boolean, CC_B_ + 'boolean'),
            ("hello", CCTypes.string,  CC_B_ + 'string'),
            ]:
        expected = f"{wrap}({expr})"
        assert bundler.box(expr, typ) == expected

def test_2_unbox_int(bundler):
    parm = "<dummy>"
    expected = f"CC_B_int.unbox({parm})"
    assert bundler.unbox(parm, CCTypes.int) == expected


def test_3_unbox_manyTypes(bundler):
    CC_B_= 'CC_B_'
    boxed = "pos[something]" # Note: not a valid value, but fine to check the text
    for cc_b_value_type, cc_type in [
            (CC_B_ + 'int' ,    CCTypes.int),
            (CC_B_ + 'float',   CCTypes.float),
            (CC_B_ + 'boolean', CCTypes.boolean),
            (CC_B_ + 'string',  CCTypes.string),
            ]:
        expected = f"{cc_b_value_type}.unbox({boxed})"
        assert bundler.unbox(boxed, cc_type) == expected


def test_4_pack_some_pos(bundler):
    expected = '[A, B, C], {}'
    pos = ('A', 'B', 'C')     # Fake (positional) args! Not boxed, no args -- just text
    txt = bundler.pack(pos, formal_parameters=None) # formal_parameters are not used
    assert isinstance(txt, (str, Block))
    assert txt == expected


def test_5a_unpack_oneInt(bundler): # The NEW, not mixed unpack
    parms = (TypedParameter('i', type=CCTypes.int),)
    expected = [
        # parm-name, pos
        ("i",       "pos[0]"),
        ]
    lines = bundler.unpack(formal_parameters = parms)
    logger.debug(lines)
    i = 0
    got_name, expected_name = lines[i][0], expected[i][0]
    assert got_name == expected_name,  f"Expected {expected_name=}, Got  {got_name=}"
    got_pos,  expected_pos  = lines[i][1], expected[i][1]
    assert got_pos == expected_pos,  f"Expected {expected_pos=}, Got  {got_pos=}"



@pytest.mark.xfail(reason="OLD unpack, need update")
def test_6a_unpackunbox_1IntParm(bundler):
    parms = (TypedParameter('i', type=CCTypes.int),)
    expected = "i = pos[0].value\n"
    assert False, f"expected is old style: {expected}"
    txt = bundler.unpack(formal_parameters=parms)
    assert str(txt) == expected
    assert isinstance(txt, (str, Block))
    verify_ValidPython(txt)

@pytest.mark.xfail(reason="OLD unpack, need update")
def test_6b_unpackunbox_MoreParms(bundler):
    parms = (
        TypedParameter('i1', type=CCTypes.int),
        TypedParameter('f2', type=CCTypes.float),
        TypedParameter('b3', type=CCTypes.boolean),
        TypedParameter('s4', type=CCTypes.string))
    expected = """\
i1 = pos[0].value
f2 = pos[1].value
b3 = pos[2].value
s4 = pos[3].value
"""
    assert False, f"expected is old style: {expected}"
    txt = str(bundler.unpack(parms))
    verify_line_by_line(expected,  txt)
