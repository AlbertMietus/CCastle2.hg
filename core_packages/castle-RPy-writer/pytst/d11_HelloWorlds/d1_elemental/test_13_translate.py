# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import typing as PTH                                                                                  # Python TypeHints

from pathlib import Path
import pytest

pytestmark = pytest.mark.xfail(reason="Need the new 'Bundler' (in AIGR) firrst", allow_module_level=True) #type: ignore



from castle.writers import RPy

from . import EXPECTED_unit
from ...TestDoubles import TestDoubles_dir # Needed for TestDoubles_out
from . import  TestDoubles_out, HW_E_out, elemental, target_unit, wrapped_target # target_unit is needef for wrapped_target

## Some settings
driver_stem = 'main_HW'                                    # the .py extension is added later DO NOT CHANGE
gen_exe     = driver_stem                                  # used without  extension (Any name)


@pytest.fixture
def generated_files(wrapped_target, TestDoubles_out) -> list[Path]:              # Returns a list of generated RPy files
    wrapped_target.write_out(inDir=TestDoubles_out)                              # Here the file is generated and saved
    return [wrapped_target.node.target_file]


from castle.writers.RPy import translators
class CopyFile(translators.base.RPY_Translator):
    def runner(self): #called via execute()
        for stem in self.files:
            logging.info(f"CopyFile: cp ../{stem}.rpy {stem}.py")
            self.process(cmd=["cp", f"../{stem}.rpy", f"{stem}.py"])

@pytest.fixture
def Copy_Not_GeneratedFiles(TestDoubles_out, stems=[driver_stem, "MACHINERY"]): # It is about the side effects!
    CopyFile(files=stems, inDir=TestDoubles_out).execute()
    return stems # for logging purposes only



@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_1_eval(generated_files, Copy_Not_GeneratedFiles, TestDoubles_out):
    runner =  RPy.translators.Evaluate(files=generated_files, inDir=TestDoubles_out, driver=driver_stem)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"


@pytest.mark.slow
@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_2_compile(generated_files, Copy_Not_GeneratedFiles, TestDoubles_out):
    runner =  RPy.translators.Compile(files=generated_files, inDir=TestDoubles_out, driver=driver_stem, into=gen_exe)
    print("\tTranslating can take some time ....",end="", flush=True)
    runner.execute()
    print(".. done")
    assert (TestDoubles_out / gen_exe).exists(), f"Expecting {gen_exe} in {TestDoubles_out}, but it isn't there"


# Note: it depends on `test_2_compile`, above
@pytest.mark.slow
@pytest.mark.parametrize('rel_path,', [HW_E_out])
def test_3_execute(TestDoubles_out):
    assert (TestDoubles_out / gen_exe).exists(), f"Expecting {gen_exe} already in {TestDoubles_out}, but it isn't"

    runner =  RPy.translators.Execute(inDir=TestDoubles_out, into=gen_exe)
    std_out = runner.execute()
    assert std_out.strip() == "Hello Elemental World"


