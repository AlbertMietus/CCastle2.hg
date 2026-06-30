# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

pytestmark = pytest.mark.xfail(reason="Rendering.Call ness the new 'Bundler'", allow_module_level=True) #type: ignore


from . import credible, wrapped_Hello_World

def test_1_method_HW(wrapped_Hello_World, my_renderer):
    expected ="""\
def HelloWorld(self, label):
    print("Hello %s World" % (label,))
\n""" #Same as for elemental
    m1 = wrapped_Hello_World.search('Credible.HelloWorld')
    txt=my_renderer.render(m1)
    verify_line_by_line(expected, txt)

#@pytest.mark.xfail(reason="body of initializer has Become needs work")
def test_2_method_init(wrapped_Hello_World, my_renderer):
    """//CastleCode
    init() {
       .credible := Credible();
    }"""
    expected ="""\
def _castle_init(self, ):
    self.credible = CC_Credible()
\n"""
    m1 = wrapped_Hello_World.search('Credible_HelloWorld.init')
    txt=my_renderer.render(m1)
    verify_line_by_line(expected, txt)

