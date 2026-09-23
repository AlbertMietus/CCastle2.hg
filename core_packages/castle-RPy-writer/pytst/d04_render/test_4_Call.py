# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from castle.aigr import ID


"""\
.. note:: The (Native)Bundler makes the call signature always : pos:ArgumentList, kw: dist -- the kw is ToBeDone

   #. So, pos is a list, kw is hardcoded as "{}" for now
   # Even when there are no (Castle) args, an (empty] '[]' is needed
"""
EXPECTED_FOR_EMPTY_ARGS="[], {}"

def test_1a_simple_ID_givesID(my_renderer):
    expected = f"foo({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('foo'), arguments=())
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_1b_dotted_ID_givesDot(my_renderer):
    expected = f"a.b({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('a.b'), arguments=())
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_1c_noArgs_givesID(my_renderer):
    expected = f"foo({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('foo'))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_2a_DefContext_hasNoEfect(my_renderer):
    expected = f"a.b.c({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('a.b.c', context=aigr.Def()))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_3a_EmptyRefContext_hasNoEfect(my_renderer):
    expected = f"a.b.c({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('a.b.c', context=aigr.Ref()))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_3b_RefContext_shouldHaveEfect(my_renderer):
    otherID = ID("another", context=aigr.Def())
    expected = f"another({EXPECTED_FOR_EMPTY_ARGS})"
    foo = aigr.Call(callable=ID('withRef', context=aigr.Ref(reference=otherID)))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_4a_CallMethod(my_renderer):
    # Calling aMethod is the same calling any _callable!! The AIGR solves this befor the writers are used
    expected = f"aMethod({EXPECTED_FOR_EMPTY_ARGS})"
    m = aigr.Call(callable=ID('aMethod'))   #note: aigr.Method is the definiton of a method!
    txt = my_renderer.render(m)
    verify_line_by_line(expected, txt)

# For call with arguments: see `test_5_ArgList.py`
