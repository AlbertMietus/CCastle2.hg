# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

def test_1a_simple_ID_givesID(my_renderer):
    txt = my_renderer.render(ID('simple'))
    verify_line_by_line("simple", txt)

def test_1b_name_withoutRef_givesName(my_renderer):
    for name in (
            'simple',
            'a.b.c',
            'self.x.y'
            '.leading.dot' # XXX correct?
            ):
        verify_line_by_line(name, ID(name))
        verify_line_by_line(name, ID(name, context=aigr.Def()))
        verify_line_by_line(name, ID(name, context=aigr.Set()))

def test_2_RefContext_shouldHaveEfect(my_renderer):
    otherID = ID("another", context=aigr.Def())
    txt = my_renderer.render(ID('this',context=aigr.Ref(reference=otherID)))
    verify_line_by_line("another", txt)

