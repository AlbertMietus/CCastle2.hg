# (C) Albert Mietus, 2025. Part of Castle/CCastle project

from . import *

def test_1_call_simple_ID(my_renderer):
    expected = "foo()"
    foo = aigr.Call(callable=ID('foo'), arguments=())
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

