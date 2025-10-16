# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from .. import *


@pytest.fixture
def credible() -> aigr.Source_NS:
    from castle.TESTDOUBLES.aigr.HelloWorlds.credible.HelloWorld import Hello_World
    return Hello_World

@pytest.fixture
def wrapped_Hello_World(credible) -> ScaffolderNameSpace:
    return ScaffolderNameSpace(credible)


