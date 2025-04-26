# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest

from castle.writers import RPy

from . import EXPECTED_unit
from ..TestDoubles import TestDoubles_dir # Needed for TestDoubles_out
from . import  TestDoubles_out, HW_E_out, target_unit

#pytest.skip(reason="Hello_World now has @impliciet(Component), giving a ComponentImplementation -- with dottedID('base.cc_CI_Component'); see test_06", allow_module_level=True)

@pytest.fixture
def target_files(target_unit, TestDoubles_out):
    target_unit.write_out(inDir=TestDoubles_out)
    return [target_unit.target_file]


#--------HACK--------
from castle.writers.RPy import translators
class Hack_cp(translators.base.RPY_Translator):
    def __init__(self, **kwargs):
        super().__init__(driver=None, **kwargs)

    def runner(self): #called via execute()
        stem = self.files[0]
        logging.warning(f"Making main driver by copy (HACK XXX)")
        return self.process(cmd=["cp", f"../{stem}.rpy", f"{stem}.py"])


@pytest.fixture
def HackMain(TestDoubles_out): #XXX
    HW_stem = "main_HW"
    HW_py   = HW_stem + ".py"
    fpy    = TestDoubles_out / HW_py
    logging.warning(f"The Main driver >{HW_py}< isn't generated; we use a HACK ...")
    if not fpy.exists():
        Hack_cp(files=[HW_stem], inDir=TestDoubles_out).execute()
    assert fpy.exists(), f"No {HW_py} in {TestDoubles_out} -- See HackMain"

#--------/HACK--------

driver='main_HW'
exe='main_HW'


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_1_eval(target_files, TestDoubles_out, HackMain):
    runner =  RPy.translators.Evaluate(files=target_files, inDir=TestDoubles_out, driver=driver)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2_compile(target_files, TestDoubles_out, HackMain):
    runner =  RPy.translators.Compile(files=target_files, inDir=TestDoubles_out, driver=driver)

    print("\tTranslating can take some time ....",end="", flush=True)
    runner.execute()
    print(".. done")

    assert (TestDoubles_out / exe).exists(), f"Expecting {exe} in {TestDoubles_out}, but it isn't there"


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_3_execute(target_files, TestDoubles_out, HackMain):
    runner =  RPy.translators.Execute(inDir=TestDoubles_out, driver=driver) 

    print(f"\tAssuming >>{exe}<< is as translatored above " ,end="", flush=True)
    std_out = runner.execute()

    assert std_out.strip() == "Hello Elemental World"


