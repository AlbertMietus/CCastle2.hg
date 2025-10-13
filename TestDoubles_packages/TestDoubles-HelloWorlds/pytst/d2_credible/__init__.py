# (C) Albert Mietus 2025, Part of Castle/CCastle project

from .. import *

@pytest.fixture
def credible() -> aigr.Source_NS:
    from castle.TESTDOUBLES.aigr.HelloWorlds.credible.HelloWorld import Hello_World
    assert isinstance(Hello_World, aigr.Source_NS) # check only, no test
    return Hello_World

@pytest.fixture
def HW(credible) ->aigr.ComponentImplementation:
    return find_impl(credible, 'Credible_HelloWorld')
