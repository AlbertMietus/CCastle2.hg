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
    logger.info(f"test_0_raw::\n{ast=}")

    rewriter = ast[0]
    assert rewriter[0] == '@'
    assert rewriter[1] == 'impliciet'
    assert rewriter[2][1] == ['Main']

    comp = ast[1]
    assert comp[0] == 'implement'
    assert comp[1] == 'Elemental_HelloWorld'
    assert comp[2] == '{'
    assert comp[3] == '}'



class Demo_Actions:
    def rewriter(self, ast):
        assert False, f"ToDo: implement rewriter action -- {ast=}"
    def implement_comp(self, ast):
        print(f"Demo_Actions/implement_comp: {ast=}")
        return aigr.ComponentImplementation(name=ast[1])
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

    #The rewriter is not in the AST

    comp = ast
    assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.name == 'Elemental_HelloWorld'




