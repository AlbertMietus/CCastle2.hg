# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest

from castle.writers import RPy

from . import EXPECTED_unit
from ..TestDoubles import TestDoubles_dir # Needed for TestDoubles_out
from . import  TestDoubles_out, HW_E_out, target_unit


@pytest.fixture
def target_files(target_unit, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out)
    return [target_unit.target_file]

@pytest.fixture
def HackMain(TestDoubles_out): #XXX
    main = "main_HW.py"
    logging.warning(f"The Main driver >{main}< isn't made, we hope the Hack works (make it manually)")
    assert (TestDoubles_out / main).exists(), f"No {main} in {TestDoubles_out} -- See HackMain"


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_1_eval(target_files, TestDoubles_out, HackMain):
    runner =  RPy.translators.Evaluate(files=target_files, inDir=TestDoubles_out)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"


