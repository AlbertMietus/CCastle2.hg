# (C) Albert Mietus, 2025. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *

mockBody = aigr.Body(statements=[aigr.Become(targets=(ID('LHS'),), values=(ID('RHS'),))]) # LHS:=RG in CastleCode
exp_Body = 'LHS = RHS'

def test_0_Init_always_has_std_name(my_renderer):
    expected = f"""\
def _castle_init(self):
    {exp_Body}
"""
    Init = aigr.Initializer(name=ID('ShouldNotBeUsed'), parameters=(), body=mockBody)
    txt = my_renderer.render(Init)
    verify_line_by_line(expected, txt)

#def test_1_Init_WithNoParmeters(my_renderer) -- See test_0

def test_2_Init_With1Parmeter(my_renderer):
    expected = f"""\
def _castle_init(self, p1):
    {exp_Body}
"""
    Init2 = aigr.Initializer(name=ID('ShouldNotBeUsed'), body=mockBody,
            parameters=(aigr.TypedParameter(name=ID('p1'), type=aigr.aigr.types.string),))
    txt = my_renderer.render(Init2)
    verify_line_by_line(expected, txt)

def test_2_Init_SomeParmeter(my_renderer):
    expected = f"""\
def _castle_init(self, p1, p2, p3):
    {exp_Body}
"""
    Init2 = aigr.Initializer(name=ID('ShouldNotBeUsed'), body=mockBody,
            parameters=(
                aigr.TypedParameter(name=ID('p1'), type=aigr.aigr.types.string),
                aigr.TypedParameter(name=ID('p2'), type=aigr.aigr.types.string),
                aigr.TypedParameter(name=ID('p3'), type=aigr.aigr.types.string),
                ))
    txt = my_renderer.render(Init2)
    verify_line_by_line(expected, txt)
    
