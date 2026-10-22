# (C) Albert Mietus, 2026. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.RPy import translators

@pytest.fixture
def mockdir():
    from pathlib import Path
    p = Path(__file__)
    dir = p.parent / "_mocks"
    assert dir.is_dir() #check only
    return dir

PY_DEMO	= "demo" # no suffix!
EXE	=     "demo.exe"
## `_mocks/demo` will add "1+2" and return the result

def test_1_mock_eval(mockdir):
    runner =  translators.Evaluate(driver=PY_DEMO, inDir=mockdir)
    std_out = runner.execute()
    assert "3" in std_out

@pytest.mark.slow
def test_2_mock_compile(mockdir):
    (mockdir / EXE).unlink(missing_ok=True) # make sure the exe doesn't exist

    runner =  translators.Compile(driver=PY_DEMO, inDir=mockdir, into=EXE)
    runner.execute()
    assert (mockdir / EXE).exists()


@pytest.mark.slow # indirect slow
def test_3_mock_execute(mockdir):
    assert (mockdir / EXE).exists(), f"we reuse the compiled exe from test_2 -- but it does NOT exist in {mockdir=}"

    runner = translators.Execute(driver=PY_DEMO, inDir=mockdir, into=EXE)
    std_out = runner.execute()
    assert "3" in std_out
