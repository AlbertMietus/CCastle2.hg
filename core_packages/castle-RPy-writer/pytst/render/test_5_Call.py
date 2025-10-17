# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

def test_1b_simple_ID_givesID(my_renderer):
    expected = "foo()"
    foo = aigr.Call(callable=ID('foo'), arguments=())
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_1b_dotted_ID_givesDot(my_renderer):
    expected = "a.b()"
    foo = aigr.Call(callable=ID('a.b'), arguments=())
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_1c_noArgs_givesID(my_renderer):
    expected = "foo()"
    foo = aigr.Call(callable=ID('foo'))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_2a_DefContext_hasNoEfect(my_renderer):
    expected = "a.b.c()"
    foo = aigr.Call(callable=ID('a.b.c', context=aigr.Def()))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_3a_EmptyRefContext_hasNoEfect(my_renderer):
    expected = "a.b.c()"
    foo = aigr.Call(callable=ID('a.b.c', context=aigr.Ref()))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

@pytest.mark.xfail(reason="BUSSY: Ref() is ignored")
def test_3b_RefContext_shouldHaveEfect(my_renderer):
    otherID = ID("another", context=aigr.Def())
    expected = "another()"
    foo = aigr.Call(callable=ID('withRef', context=aigr.Ref(reference=otherID)))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

