# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy

my_dir =  get_dirPath_of_file(__file__)
template_r_dir = "./templates/"
template_a_dir = my_dir / template_r_dir

def test_simpel_template():
    HW_file = 'HW_template.txt'
    template = RPy.Template(template=HW_file, search_path=template_a_dir)
    out=template.render(Hello='{{Hello}}', World='{{World}}')           # Generates itself

    ref=open(template_a_dir / HW_file).read()
    assert end_with_NL(ref) == end_with_NL(out), f"ref::\n{ref}\nout::\n{out}\nDo not match"

def test_simpel_template_2():
    HW_file = 'HW_template.txt'
    template = RPy.Template(template=HW_file, top_dir=my_dir)
    out=template.render(Hello='{{Hello}}', World='{{World}}')           # Generates itself

    ref=open(template_a_dir / HW_file).read()
    assert end_with_NL(ref) == end_with_NL(out), f"ref::\n{ref}\nout::\n{out}\nDo not match"


def test_template_extends():
    child = 'child.txt'
    base  = 'base.txt' # Not used to render, only to test

    template = RPy.Template(template=child, search_path=template_a_dir)
    out = template.render(v1 ='Var 1', v2 ='Var 2', TOP='top: but not completely', BOTTOM="bottom, really")

    ref_lines = open(template_a_dir / base).readlines()
    out_lines = out.splitlines(keepends=True)

    assert ref_lines[0] == out_lines[0], "Rendering child, should return the topline of base"
    assert ref_lines[1] == out_lines[1], "Last line should the same too"

    assert     any('NOT-IN-CHILD' in l for l in ref_lines), "Make sure the marker is in `base`"
    assert not any('NOT-IN-CHILD' in l for l in out_lines), "The 1st BLOCK should be replaced"

    assert any('SUPER-CHILD' in l for l in ref_lines), "Make sure the marker is in `base`"
    assert any('SUPER-CHILD' in l for l in out_lines), "As the 2nd block uses `super()` it should be in"


def test_template_parts():
    big_file  = "big.txt"                                             # Uses: part-include.txt &  part-import.txt

    template = RPy.Template(template=big_file, search_path=template_a_dir)
    out = template.render()

    assert 'INCLUDED' in out, "this line in part-include.txt"
    assert 'IMPORTED' in out, "this line in part-import.txt"


def test_not_founda_1():
    T= RPy.Template()
    try:
        T.render()
        assert False, "No (default) templates shouldn't render..."                   # pragma: no cover
    except FileNotFoundError:
        pass

def test_not_founda1():
    import jinja2
    try:
        RPy.Template('This file does NOT exist')
        assert False, "Handled by jinja"                                         # pragma: no cover  
    except jinja2.TemplateNotFound:
        pass

def test_verion():
    assert RPy._version == "VERY_DRAFT"
