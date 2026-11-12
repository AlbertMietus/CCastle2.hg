# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *

""".. note:: `my_renderer` (using the NativeBundler) does NOT bundle arguments for `Call`
"""


def test_9_call_fString_wrong_(my_renderer): # Each arg to a call should be an `aigr.Argument`! It's NOT
    """CastleCode: print("Test no {x}")"""
    expected = '''foo("Test no %s" % (x,))'''
    foo = aigr.Call(callable=ID('foo'), arguments=[aigr.fString("Test no {x}")])
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

def test_9_call_fString_correctly(my_renderer): # Each arg to a call should be an `aigr.Argument`!
    """CastleCode: print("Test no {x}")"""
    expected = '''foo("Test no %s" % (x,))'''
    foo = aigr.Call(callable=ID('foo'), arguments=(aigr.Argument(value=aigr.fString("Test no {x}")),))
    txt = my_renderer.render(foo)
    verify_line_by_line(expected,txt)

