# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from castle import aigr

from . import *

@pytest.fixture
def grammmar_file():
    return 'demo_grammar_dict.tatsu'


def test_0_raw(demo_parser):
    ast = demo_parser.parse(eHW_frame)
    logger.info(f"test_0_raw::\n{ast=}")

    rewriter = ast.rewriter
    assert rewriter.name  == 'impliciet'
    assert len(rewriter.parms) == 1
    assert rewriter.parms[0].name == 'Main'
    assert rewriter.parms[0].type is None
    assert rewriter.parms[0].modifiers == []

    comp = ast.implement_comp
    assert comp.name == 'Elemental_HelloWorld'



def test_1a_actions_NoRewriter(demo_parser):
    print("\n---- test_1a_actions ----")
    ast = demo_parser.parse(eHW_frame_NoRewriter, semantics=Demo_Actions())
    print("---- test_1a_actions (END) ----")
    print(f"test_1a_actions:: {ast=}")

    verify_rewriter(ast, absent=True)
    verify_comp(ast)

def test_1b_actions_WithRewriter(demo_parser):
    print("\n---- test_1b_actions ----")
    ast = demo_parser.parse(eHW_frame, semantics=Demo_Actions())
    print("---- test_1b_actions (END) ----")
    print(f"test_1b_actions:: {ast=}")

    verify_rewriter(ast, absent=False)
    verify_comp(ast)

###
###    end of tests
###

class Demo_Actions:
    def rewriter(self, ast):
        logger.error(f"No aigr for REWRITER return ast -- {ast=} XXX ToDo: update aigr")
        return ast
    def implement_comp(self, ast):
        print(f"Demo_Actions/implement_comp: {ast=}")
        return aigr.ComponentImplementation(name=ast.name)
    def ID(self, ast):
        print(f"Demo_Actions/ID: {ast=}")
        return aigr.ID(name=ast)
    def _default(self,ast):
        print(f"Demo_Actions/_default: {ast=}")
        return ast

def verify_rewriter(ast, absent):
    rewriter = ast.rewriter # No AIGR.rewriter, but we can use the dict
    if absent:
        assert rewriter is None
    else:
        assert rewriter.name  == 'impliciet'
        assert rewriter.parms[0].name == 'Main'

def verify_comp(ast):
    comp = ast.implement_comp
    assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.name == 'Elemental_HelloWorld'
