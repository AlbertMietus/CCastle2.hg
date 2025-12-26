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
    def implementation(self, ast):
        print(f"Demo_Actions/implementation: {ast=}")
        d={}
        if isinstance(ast, aigr.ComponentImplementation):
            d['implementation']= ast
        else:
            d['rewriter']= ast[0]
            d['implementation']= ast[1]
        return d
    def rewriter(self, ast):
        logger.error(f"No aigr for REWRITER return ast -- {ast=} XXX ToDo: update aigr")
        return ast
    def implement_comp(self, ast):
        print(f"Demo_Actions/implement_comp: {ast=}")
        return aigr.ComponentImplementation(name=ast[1])
    def ID(self, ast):
        print(f"Demo_Actions/ID: {ast=}")
        return aigr.ID(name=ast)
    def _default(self,ast):
        print(f"Demo_Actions/_default: {ast=}")
        return ast

def verify_rewriter(ast, absent):
    if absent:
        assert 'rewriter' not in ast
    else:
        rewriter = ast['rewriter']
        assert rewriter[1]  == 'impliciet'
        assert rewriter[2][1][0] == 'Main'

def verify_comp(ast):
    comp = ast['implementation']
    assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.name == 'Elemental_HelloWorld'
