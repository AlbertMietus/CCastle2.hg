# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy


template_dir ="./templates/"
def test_load_template():
    HW_file = 'HW_template.txt'
    t_dir = get_dirPath_of_file(__file__) / template_dir

    template = RPy.Template(searchpath=t_dir, template=HW_file)
    out=template.render(Hello='{{Hello}}', World='{{World}}')           # Generates itself

    ref=open(t_dir / HW_file).read()
    assert end_with_NL(ref) == end_with_NL(out), f"ref::\n{ref}\nout::\n{out}\nDo not match"
