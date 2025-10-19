# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

from . import credible, wrapped_Hello_World

@pytest.fixture
def become(wrapped_Hello_World):
    initializer = wrapped_Hello_World.search('Credible_HelloWorld.init')
    return initializer.body.statements[0]

def test_0_isBecome(become):
    assert isinstance(become, aigr.Become), f"the fixture should return 'Become', but returns {become}"

def test_1_renderBecome(become, my_renderer):
    expected ="self.credible = CC_Credible()"   #XXX
    txt=my_renderer.render(become)
    verify_line_by_line(expected, txt)
