# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle import aigr

from castle.writers import RPy
from castle.writers.RPy.writers import Renderer

from ..TestDoubles import *
from .ExpectedTxt import *

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World # Source_NS

HW_E_out    = Path('HelloWorlds', 'elemental', '__out')

@pytest.fixture
def my_renderer() ->Renderer:
    cls = Renderer
    logger.debug(f'Using "{cls}" as Renderer')
    return cls()



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




def verify_line(expect, got, line=None):
    logger.debug("verify_line\n\texpect:\t%s\ngot\t>>%s<<\n\tline=%s", expect, got, line)
    if expect == got:
        return
    try:
        txt = got.splitlines()[line] if line else got
    except IndexError:
        assert False, f"line={line} does not exist in got:>>{got}<< -- Expected: {expect}"
    assert expect in txt, imprint((expect,'EXPECT'),(got, 'Got'))

def print_out(txt,label='print'):
    print(imprint((txt, label)))
    pass

def imprint(*parts):
    return "\n".join(f"\n=====[{label}:{len(txt)}/{len(txt.splitlines())}]=====\n{txt}\n=====[end]=====\n" for txt, label in parts)

def verify_line_by_line(expect, got):
    expect_lines, got_lines = expect.splitlines(), got.splitlines()
    for e,g, no in zip(expect_lines, got_lines, range(999)):
        NL,context="\n\t",3
        assert e == g, f'Line: {no+1} not as expected\nexpect:\n{e}\ngot:\n{g}\nBefore\n{NL.join(got_lines[:no][-context:])}\nAfter\n{NL.join(got_lines[no+1:][:context])} '
    assert len(expect) == len(got), f"Not the same number of lines: expect: {len(expect)}, got: {len(got)}"


def verify_file(expect: str, file: Path|str):
    if isinstance(file, str):
        file = Path(file)
    logger.info("read from: %s", file)
    assert file.is_file()
    verify_line_by_line(expect, file.read_text())
