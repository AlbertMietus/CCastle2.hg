# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle.writers import RPy
from castle.writers.RPy import transformers

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World # Source_NS

from . import my_renderer, verify_line, verify_line_by_line
from . import print_out
from . import EXPECTED_RPY_CODE

TESTDOUBLES = Path('TestDoubles')
HW_E_out    = Path('HelloWorlds', 'elemental', '__out')

@pytest.fixture
def target_unit():
    ns = RPy.transformers.Source2RPy(Hello_World)
    assert isinstance(ns, RPy.transformers.RPy_file) # check only, no test
    return ns


@pytest.fixture
def TestDoubles_dir():
    import os; 

    dir = Path(os.getcwd())
    while not (dir / TESTDOUBLES).exists():
        assert str(dir)!=str(dir.parent), f"Can't find {TESTDOUBLES}-dir from {os.getcwd()}"
        dir = dir.parent
    the_dir = dir / TESTDOUBLES
    assert the_dir.is_dir(), f"found {the_dir}, but it isn't a dir"
    return the_dir

@pytest.fixture
def TestDoubles_out(TestDoubles_dir):
    out_dir = TestDoubles_dir / HW_E_out
    assert out_dir.exists() and out_dir.is_dir(), f" Not valid: {out_dir}"
    return out_dir

def test_1_txt(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    #print_out(txt)
    verify_line_by_line(EXPECTED_RPY_CODE, txt)

@pytest.mark.skip
def test_2a_file(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    target_unit.save(txt, dir='xxx',)
    assert False, "ToDo: How to check"

@pytest.mark.skip
def test_2b_file(target_unit):
    target_unit.write_out(dir='xxx',)
    assert False, "ToDo: How to check"


def test_0_curdir():
    import os
    print_out(os.getcwd(), label='current')

def test_0_outdir(TestDoubles_out):
    print_out(str(TestDoubles_out), label='__out')
