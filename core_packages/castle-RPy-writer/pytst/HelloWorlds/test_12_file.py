# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest


from castle.writers import RPy

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World # Source_NS

from . import my_renderer, Renderer
from . import verify_line, verify_line_by_line, verify_file
from . import print_out
from . import TestDoubles_dir
from . import EXPECTED_unit

HW_E_out    = Path('HelloWorlds', 'elemental', '__out')


@pytest.fixture
def target_unit():
    ns = RPy.transformers.Source2RPy(Hello_World)
    assert isinstance(ns, RPy.writers.RPy_unit) # check only, no test
    return ns

@pytest.fixture
def TestDoubles_out(TestDoubles_dir, rel_path):
    out_dir = TestDoubles_dir / rel_path
    assert out_dir.exists() and out_dir.is_dir(), f" Not valid: {out_dir}"
    return out_dir


def test_1_txt(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    #print_out(txt, label='got')
    #print_out(EXPECTED_unit, label='EXPECTED_unit')
    verify_line_by_line(EXPECTED_unit, txt)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2a_file(target_unit, my_renderer, TestDoubles_out):
    txt = my_renderer.render(target_unit)
    target_unit.save(txt, inDir=TestDoubles_out)
    verify_file(txt, target_unit.target_file)
    verify_file(EXPECTED_unit, target_unit.target_file)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2b1_file(target_unit, my_renderer, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out, renderCls=my_renderer) # an instance if allowed ...
    verify_file(EXPECTED_unit, target_unit.target_file)

@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2b2_file(target_unit, my_renderer, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out, renderCls=Renderer)
    verify_file(EXPECTED_unit, target_unit.target_file)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2c_file(target_unit, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out,)
    verify_file(EXPECTED_unit, target_unit.target_file)

