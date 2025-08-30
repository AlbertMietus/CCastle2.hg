# (C) Albert Mietus, 2025. Part of Castle/CCastle project

"""Render (the elemental verion of) HelloWorld to text, and save it into a RPy file"""


import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World # Source_NS

from . import my_renderer, Renderer
from . import verify_line, verify_line_by_line, verify_file
from . import print_out
from . import EXPECTED_unit

from ..TestDoubles import TestDoubles_dir # Needed for TestDoubles_out
from . import target_unit, TestDoubles_out, HW_E_out


def test_1_renderToTxt(target_unit, my_renderer):
    txt = my_renderer.render(target_unit)
    #print_out(txt, label='got'); print_out(EXPECTED_unit, label='EXPECTED_unit')
    verify_line_by_line(EXPECTED_unit, txt)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2a_render_andSafeTo_file(target_unit, my_renderer, TestDoubles_out):
    txt = my_renderer.render(target_unit)
    target_unit.save(txt, inDir=TestDoubles_out)
    verify_file(txt, target_unit.target_file)
    verify_file(EXPECTED_unit, target_unit.target_file)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2b1_writeOut_with_instance_is_allowd(target_unit, my_renderer, TestDoubles_out): # (should be same as above, but now with write_out()
    target_unit.write_out(inDir=TestDoubles_out, renderCls=Renderer)
    verify_file(EXPECTED_unit, target_unit.target_file)

@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2b2_writeOut_with_class(target_unit, my_renderer, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out, renderCls=my_renderer) # should pass a class, but an instance is allowed
    verify_file(EXPECTED_unit, target_unit.target_file)


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2c_writeOut_defaultCls(target_unit, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out,)
    verify_file(EXPECTED_unit, target_unit.target_file)


import re
def show(hack):
    return [match.string.splitlines()[match.string[:match.start()].count('\n')] for match in hack]

#pytest.mark.fail...
def test_99_noHack():
    hacks = list(re.finditer('HACK', EXPECTED_unit, flags=re.IGNORECASE))
    txt = show(hacks)
    assert len(hacks) == 0, pytest.xfail(reason=" There are (%d) hacks::  %s" % (len(txt),txt))

