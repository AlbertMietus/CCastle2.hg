# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

@pytest.mark.skip
def xtest_1_Protocol(my_renderer):
    expected = """\
    TODO: EventProtocol rendering not yet implemented
\n"""
    proto = aigr.EventProtocol(ID('DummyProto', context=aigr.Def()), events=[])
    txt = my_renderer.render(proto)
    verify_line_by_line(expected, txt)

