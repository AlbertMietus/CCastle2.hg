# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy

template_dir ="./templates/"
t_dir = get_dirPath_of_file(__file__) / template_dir

def test_simpel_template():
    HW_file = 'HW_template.txt'

    template = RPy.Template(template=HW_file, search_path=t_dir)
    out=template.render(Hello='{{Hello}}', World='{{World}}')           # Generates itself

    ref=open(t_dir / HW_file).read()
    assert end_with_NL(ref) == end_with_NL(out), f"ref::\n{ref}\nout::\n{out}\nDo not match"


def test_template_extends():
    child = 'child.txt'
    base  = 'base.txt' # Not used to render, only to test

    template = RPy.Template(template=child, search_path=t_dir)
    out = template.render(v1 ='Var 1', v2 ='Var 2', TOP='top: but not completely', BOTTOM="bottom, really")

    ref_lines = open(t_dir / base).readlines()
    out_lines = out.splitlines(keepends=True)

    assert ref_lines[0] == out_lines[0], "Rendering child, should return the topline of base"
    assert ref_lines[1] == out_lines[1], "Last line should the same too"

    assert     any('NOT-IN-CHILD' in l for l in ref_lines), "Make sure the marker is in `base`"
    assert not any('NOT-IN-CHILD' in l for l in out_lines), "The 1st BLOCK should be replaced"

    assert any('SUPER-CHILD' in l for l in ref_lines), "Make sure the marker is in `base`"
    assert any('SUPER-CHILD' in l for l in out_lines), "As the 2nd block uses `super()` it should be in"


def test_use_RPy_template():
    file = "protocol.jinja2"
    template = RPy.Template(file)
    assert template.def_template is not None, "Can't find ``fine``, should be in <RPy-module>/templates"
    out = template.render()
    assert out is not None, "At least some lines should be there"


def test_template_parts():
    big_file  = "big.txt"                                             # Uses: part-include.txt &  part-import.txt

    template = RPy.Template(template=big_file, search_path=t_dir)
    out = template.render()

    assert 'INCLUDED' in out, "this line in part-include.txt"
    assert 'IMPORTED' in out, "this line in part-import.txt"

