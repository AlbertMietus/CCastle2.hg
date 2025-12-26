# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from castle import aigr

from . import *
del eHW_frame_NoRewriter # Not needed here

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

def test_1_actions(demo_parser):
    print("\n---- test_1_actions ----")
    ast = demo_parser.parse(eHW_frame, semantics=Demo_Actions())
    print("---- test_1_actions (END) ----")
    print(f"test_1_actions:: {ast=}")

    rewriter = ast.rewriter # No AIGR.rewriter, but w can use the dict
    assert rewriter.name  == 'impliciet'
    assert rewriter.parms[0].name == 'Main'

    comp = ast.implement_comp
    assert isinstance(comp, aigr.ComponentImplementation)
    assert comp.name == 'Elemental_HelloWorld'




