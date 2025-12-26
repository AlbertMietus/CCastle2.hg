# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)

import pytest
from pathlib import Path
import tatsu

from castle import aigr

eHW_frame_NoRewriter = """\
   implement Elemental_HelloWorld
   {
   }
"""

eHW_frame = """@impliciet(Main)\n"""+ eHW_frame_NoRewriter

@pytest.fixture
def myPath():
    return Path(__file__).parent

@pytest.fixture
def demo_parser(myPath):
    with open(myPath  / 'demo_grammar.tatsu') as f:
        grammar = f.read()
        parser = tatsu.compile(grammar)
        return parser


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
        logger.warning("`@rewriter` has no AIGR node yet. ToDo XXX")
        print(f"Demo_Actions/rewriter: {ast=}")
        assert False, "ToDo: implement rewriter action"
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




