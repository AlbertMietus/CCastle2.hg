# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project
"""
These tests only exist to show we can run a tests in RPy
"""
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.writers import RPy

from pathlib import Path

def test_run():
    print(f"{__name__}::")

def test_import():
    print(f"{__name__}:: {RPy._version}")


def _get_file_dirPath():
    from pathlib import Path
    import os
    return Path(os.path.realpath(__file__)).parent

def end_with_NL(txt):
    return txt +'\n' if (txt[-1] != '\n') else txt

template_dir ="./templates/"
def test_load_template():
    HW_file = 'HW_template.txt'
    t_dir = _get_file_dirPath() / template_dir

    template = RPy.Template(searchpath=t_dir, template=HW_file)
    out=template.render(Hello='{{Hello}}', World='{{World}}')           # Generates itself

    ref=open(t_dir / HW_file).read()
    assert end_with_NL(ref) == end_with_NL(out), f"ref::\n{ref}\nout::\n{out}\nDo not match"
