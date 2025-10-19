# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from .. import *
from .ExpectedTxt import * # expected txts for HelloWorlds.elemental

@pytest.fixture
def credible() -> aigr.Source_NS:
    from castle.TESTDOUBLES.aigr.HelloWorlds.credible.HelloWorld import Hello_World
    return Hello_World

@pytest.fixture
def wrapped_Hello_World(credible) -> ScaffolderNameSpace:
    return ScaffolderNameSpace(credible)


@pytest.fixture
def target_unit(credible) -> RPy.aigr.RPy_unit:
    ns = RPy.transformers.Source2RPy(credible)
    assert isinstance(ns, RPy.aigr.RPy_unit) # check only, no test
    return ns

@pytest.fixture
def wrapped_target(target_unit) -> RPy.aigr.ScaffolderUnit: #depends on elemental
    return RPy.aigr.ScaffolderUnit(target_unit)
