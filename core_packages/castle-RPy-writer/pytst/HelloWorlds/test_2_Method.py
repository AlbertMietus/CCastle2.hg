# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.TESTDOUBLES.aigr.HelloWorlds.elemental.HelloWorld import Hello_World

from . import my_renderer, verify_line
from . import print_out

@pytest.fixture
def Method():
    impl = Hello_World.findNode('Elemental_HelloWorld')
    m = impl.findNode('HelloWorld')
    assert m # check only, no test
    return m


def test_1_1stLine_is_def(Method, my_renderer):
    txt = my_renderer.render(Method)
    verify_line('def HelloWorld(self, label):',txt, 0)

##HelloWorld = Method(ID('HelloWorld', context=aigr.Def()),
##                    returns=None,
##                    outer_ns=Elemental_HelloWorld,
##                    parameters=(aigr.TypedParameter(name=ID('label'), type=str),),
##                    body=aigr.Body(statements=[
##                        aigr.VoidCall(
##                            aigr.Call(callable=ID(print),
##                                      arguments=(
##                                          aigr.Constant(value="Hello {label} World"),
##                                          ID('label',context=aigr.Ref()))))]))
@pytest.mark.skip(reason="BUSY")
def test_2_print(Method, my_renderer):
    """def HelloWorld(self, label):
           print(f'''Hello {label} World''')
    """
    txt = my_renderer.render(Method)

    print_out(txt)
    verify_line("""   print(f'''Hello {label} World''')""", txt, 1)



