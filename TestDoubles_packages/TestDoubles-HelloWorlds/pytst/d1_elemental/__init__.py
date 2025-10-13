# (C) Albert Mietus 2025, Part of Castle/CCastle project

from .. import *

@pytest.fixture
def elemental() -> aigr.Source_NS:
    from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World
    return Hello_World

@pytest.fixture
def HW(elemental) ->aigr.ComponentImplementation:
    return find_impl(elemental, 'Elemental_HelloWorld')



