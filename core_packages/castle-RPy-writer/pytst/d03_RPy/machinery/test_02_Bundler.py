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

from castle import aigr
from castle.writers.RPy.writer.machinery import Bundler, NativeBundler

from castle.writers.RPy.writer.machinery.native_bundler import TypeTag, ParameterListElement
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
    got = bundler.unpack(formal_parameters = parms)
    validate_UnBundleResults(got, expected)


def test_5b_unpack_some(bundler): # The NEW, not mixed unpack
    parms = (
        TypedParameter('i0', type=CCTypes.int),
        TypedParameter('i1', type=CCTypes.int),
        TypedParameter('f2', type=CCTypes.float),
        TypedParameter('s3', type=CCTypes.string),
        TypedParameter('b4', type=CCTypes.boolean),
        )
    expected = [
        # parm-name, pos
        ("i0",       "pos[0]"),
        ("i1",       "pos[1]"),
        ("f2",       "pos[2]"),
        ("s3",       "pos[3]"),
        ("b4",       "pos[4]"),
        ]
    got = bundler.unpack(formal_parameters = parms)
    validate_UnBundleResults(got, expected)


def test9a_unpack_unbox__one(bundler):
    parms = (TypedParameter('i', type=CCTypes.int),)
    expected = [('i','CC_B_int.unbox(pos[0])'),]
    got = bundler.unpack_unbox(parms)
    validate_UnBundleResults(got, expected)


def test9a_unpack_unbox__some(bundler):
    parms = (
        TypedParameter('i0', type=CCTypes.int),
        TypedParameter('i1', type=CCTypes.int),
        TypedParameter('f2', type=CCTypes.float),
        TypedParameter('s3', type=CCTypes.string),
        TypedParameter('b4', type=CCTypes.boolean),
        )
    expected = [
        #name  (=) value
        ("i0",       "CC_B_int.unbox(pos[0])"),
        ("i1",       "CC_B_int.unbox(pos[1])"),
        ("f2",       "CC_B_float.unbox(pos[2])"),
        ("s3",       "CC_B_string.unbox(pos[3])"),
        ("b4",       "CC_B_boolean.unbox(pos[4])"),
        ]
    got = bundler.unpack_unbox(parms)
    validate_UnBundleResults(got, expected)




def validate_UnBundleResults(got, expected):
    assert len(got) == len(expected), f"Expected {len(expected)=}, but got {len(got)=} elements"

    for g, e in zip(got, expected, strict=True):
        got_name, expected_name = g[0], e[0]
        got_pos,  expected_pos  = g[1], e[1]
        assert got_name == expected_name,  f"Expected {expected_name=}, Got  {got_name=}"
        assert got_pos  == expected_pos,   f"Expected {expected_pos=},  Got  {got_pos=}"





