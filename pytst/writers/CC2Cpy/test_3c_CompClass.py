# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest
from . import * # CCompare

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentClass

from . import common

def test_1a_render_empty():
    compClass = CC_B_ComponentClass(common.emptyComp())
    assert CCompare(common.ref_emptyClass, compClass.render_Fill_ComponentClass())

def test_1a_render_demo2():
    compClass = CC_B_ComponentClass(common.demo2Comp())
    assert CCompare(common.ref_demo2Class, compClass.render_Fill_ComponentClass())

def test_2_render_whitespace():
    assert CCompare(common.ref_emptyClass, CC_B_ComponentClass(common.emptyComp()).render_Fill_ComponentClass())

def test_3a_indent_empty():
    verify_indents(common.ref_emptyComp, common.emptyComp().render)

def test_3b_indent_demo():
    verify_indents(common.ref_demo2Comp, common.demo2Comp().render)

def test_3c_indent_sub():
    verify_indents(common.ref_subComp, common.subComp(base=common.demo2Comp()).render)

