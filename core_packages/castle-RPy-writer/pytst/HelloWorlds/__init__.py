# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers import RPy
from castle.writers.RPy.writer import Renderer
from castle.aigr_extra.scaffolding import  ScaffolderNameSpace

from .. import my_renderer, verify_line_by_line
from ..verify import *

from pathlib import Path
HW_E_out    = Path('HelloWorlds', 'elemental', '__out')

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World # Source_NS

from .ExpectedTxt import *

@pytest.fixture
def wrapped_Hello_World():
    return ScaffolderNameSpace(Hello_World)

@pytest.fixture
def target_unit() -> RPy.aigr.RPy_unit:
    ns = RPy.transformers.Source2RPy(Hello_World)
    assert isinstance(ns, RPy.aigr.RPy_unit) # check only, no test
    return ns

@pytest.fixture
def wrapped_target(target_unit) -> RPy.aigr.ScaffolderUnit:
    return RPy.aigr.ScaffolderUnit(target_unit)


@pytest.fixture
def TestDoubles_out(TestDoubles_dir, rel_path) -> Path:
    out_dir = TestDoubles_dir / rel_path
    assert out_dir.exists() and out_dir.is_dir(), f" Not valid: {out_dir}"
    return out_dir


def verify_file(expect: str, file: Path|str):
    if isinstance(file, str):
        file = Path(file)
    logger.info("read from: %s", file)
    assert file.is_file()
    verify_line_by_line(expect, file.read_text())
