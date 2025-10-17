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
    """Typically, a ID-Ref points to another aigr-node.
        But any Ref should result that the name of the ID isn't used, but that of Ref.
        Even for text"""
    some_txt = "Unusual_but_Fine"
    txt = my_renderer.render(ID('this',context=aigr.Ref(reference=some_txt)))
    verify_line_by_line(some_txt, txt)

def test_3_RefID_renders_anotherID(my_renderer):
    otherID = ID("another", context=aigr.Def())
    txt = my_renderer.render(ID('ID_withRef',context=aigr.Ref(reference=otherID)))
    verify_line_by_line("another", txt)

def test_4_RefRefID_works_too(my_renderer):
    goalID = ID("goal")
    skipID = ID('HaasjeOver', context=aigr.Ref(reference=goalID))
    txt = my_renderer.render(ID('ID_withRef_toRef',context=aigr.Ref(reference=skipID)))
    verify_line_by_line("goal", txt)


@pytest.mark.xfail(reason="TODO: render_asID_portray_visitor")
def test_5_RefToOther_returnsOtherasID(my_renderer):
    """When an ID Reference another AIGR, f.e. an Component,
       the (portray) name should be return, not the definitions"""
    regTo =aigr.ComponentInterface("Comp_OrAnyNonID")
    txt = my_renderer.render(ID("Comp", context=aigr.Ref(reference=regTo)))
    verify_line_by_line("cc_CI_Comp_OrAnyNonID" , txt)

