# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *


def test_1a_DummyProtocol_noBase(my_renderer):
    expected = """\
cc_P_DummyProto = buildin.CC_B_Protocol(name="DummyProto",
    kind = buildin.CC_ProtocolKind.Event,
    inherit_from = None,
    events = [])
\n"""
    proto = aigr.EventProtocol(ID('DummyProto', context=aigr.Def()), events=[], based_on=None) #based_on=None differes from no inheritance!
    txt = my_renderer.render(proto)
    verify_line_by_line(expected, txt)


def test_1b_DummyProtocol_withBase(my_renderer):
    expected = """\
cc_P_DummyProto = buildin.CC_B_Protocol(name="DummyProto",
    kind = buildin.CC_ProtocolKind.Event,
    inherit_from = None,
    events = [])
\n"""
    proto = aigr.EventProtocol(ID('DummyProto', context=aigr.Def()), events=[]) # now, .based_on is _RootProtocol
    txt = my_renderer.render(proto)
    #print_out(txt)
    verify_line_by_line(expected, txt)

