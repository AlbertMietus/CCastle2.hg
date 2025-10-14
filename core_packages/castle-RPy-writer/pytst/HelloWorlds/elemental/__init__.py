# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from .. import *

HW_E_out    = Path('HelloWorlds', 'elemental', '__out')
from .ExpectedTxt import * # expected txts for HelloWorlds.elemental

@pytest.fixture
def elemental() -> aigr.Source_NS:
    from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
    return Hello_World

@pytest.fixture
def wrapped_Hello_World(elemental) -> ScaffolderNameSpace:
    return ScaffolderNameSpace(elemental)


@pytest.fixture
def target_unit(elemental) -> RPy.aigr.RPy_unit:
    ns = RPy.transformers.Source2RPy(elemental)
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


