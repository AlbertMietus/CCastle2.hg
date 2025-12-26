# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from castle import aigr

from . import *

@pytest.fixture
def grammmar_file():
    return 'demo_grammar.tatsu'


def test_0_raw(demo_parser):
    ast = demo_parser.parse(eHW_frame)
    print(f"test_0_raw:: {ast=}")
    assert ast[0][0] == '@'
    assert ast[0][1] == 'impliciet'
    assert ast[0][2][1] == ['Main']
    assert ast[1][0] == 'implement'
    assert ast[1][1] == 'Elemental_HelloWorld'
    assert ast[1][2] == '{'
    assert ast[1][3] == '}'



class Demo_Actions:
    def rewriter(self, ast):
        assert False, f"ToDo: implement rewriter action -- {ast=}"
    def implement_comp(self, ast):
        print(f"Demo_Actions/implement_comp: {ast=}")
        comp = aigr.ComponentImplementation(name=ast[1])
        return comp
    def ID(self, ast):
        print(f"Demo_Actions/ID: {ast=}")
        return aigr.ID(name=ast)
    def _default(self,ast):
        print(f"Demo_Actions/_default: {ast=}")
        return ast

def test_1_actions(demo_parser):
    print("\n---- test_1_actions ----")
    ast = demo_parser.parse(eHW_frame_NoRewriter, semantics=Demo_Actions())
    print("---- test_1_actions (END) ----")
    print(f"test_1_actions:: {ast=}")

    assert isinstance(ast, aigr.ComponentImplementation)
    assert ast.name == 'Elemental_HelloWorld'




