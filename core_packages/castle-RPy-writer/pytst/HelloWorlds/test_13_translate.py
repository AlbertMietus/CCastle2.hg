# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest

from castle.writers import RPy

from . import EXPECTED_unit
from ..TestDoubles import TestDoubles_dir # Needed for TestDoubles_out
from . import  TestDoubles_out, HW_E_out, target_unit, wrapped_target # target_unit is needef for wrapped_target

@pytest.fixture
def target_files(wrapped_target, TestDoubles_out):
    wrapped_target.write_out(inDir=TestDoubles_out)
    return [wrapped_target.node.target_file]


#--------HACK--------
from castle.writers.RPy import translators
class Hack_cp(translators.base.RPY_Translator):
    def __init__(self, **kwargs):
        super().__init__(driver=None, **kwargs)

    def runner(self): #called via execute()
        stem = self.files[0]
        logging.warning(f"cp ../{stem}.rpy {stem}.py")
        return self.process(cmd=["cp", f"../{stem}.rpy", f"{stem}.py"])


@pytest.fixture
def CopyHack(TestDoubles_out, stems=["main_HW","MACHINERY"]): #XXX
    for stem in stems:
        py_file =stem + ".py"
        fpy    = TestDoubles_out / py_file
        if not fpy.exists():
            logging.warning(f"The file >{fpy}< isn't generated; we use a Copy-Hack ...")
            Hack_cp(files=[stem], inDir=TestDoubles_out).execute()
    assert fpy.exists()
#--------/HACK--------

driver='main_HW'
exe='main_HW'


@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_1_eval(target_files, TestDoubles_out, CopyHack):
    runner =  RPy.translators.Evaluate(files=target_files, inDir=TestDoubles_out, driver=driver)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"

@pytest.mark.slow
@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2_compile(target_files, TestDoubles_out, CopyHack):
    runner =  RPy.translators.Compile(files=target_files, inDir=TestDoubles_out, driver=driver)

    print("\tTranslating can take some time ....",end="", flush=True)
    runner.execute()
    print(".. done")

    assert (TestDoubles_out / exe).exists(), f"Expecting {exe} in {TestDoubles_out}, but it isn't there"

# Note: it depends on `test_2_compile`, above
@pytest.mark.slow
@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_3_execute(target_files, TestDoubles_out, CopyHack):
    runner =  RPy.translators.Execute(inDir=TestDoubles_out, driver=driver)

    print(f"\tAssuming >>{exe}<< is as translatored above " ,end="", flush=True)
    std_out = runner.execute()

    assert std_out.strip() == "Hello Elemental World"


