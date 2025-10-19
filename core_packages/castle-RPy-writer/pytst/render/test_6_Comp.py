# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

def test_0_ComponentInterface(my_renderer):
    expected = """\
cc_CI_Stub = buildin.CC_B_ComponentInterface(
    name         = "Stub",
    inherit_from = base.cc_CI_Component,
    ports        = (),
    )\n"""
    comp = aigr.ComponentInterface(ID("Stub", context=aigr.Def()))
    txt = my_renderer.render(comp)
    verify_line_by_line(expected,txt)
    
