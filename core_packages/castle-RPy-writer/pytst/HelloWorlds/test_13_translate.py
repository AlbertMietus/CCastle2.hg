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
def TestDoubles_out(TestDoubles_dir, rel_path) -> Path:
    out_dir = TestDoubles_dir / rel_path
    assert out_dir.exists() and out_dir.is_dir(), f" Not valid: {out_dir}"
    return out_dir

@pytest.fixture
def target_files(target_unit, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out)
    return [target_unit.target_file]

@pytest.fixture
def HackMain(TestDoubles_out):
    main = "main_HW.py"
    logging.warning(f"The Main driver >{main}< isn't made, we hope the Hack works (make it manually)")
    assert (TestDoubles_out / main).exists(), f"No {main} in {TestDoubles_out} -- See HackMain"

@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_1_eval(target_files, TestDoubles_out, HackMain):
    runner =  RPy.translators.Evaluate(files=target_files, inDir=TestDoubles_out)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"


