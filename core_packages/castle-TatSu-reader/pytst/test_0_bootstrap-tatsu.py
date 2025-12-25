# (C) Albert Mietus, 2025- Part of Castle/CCastle project

import pytest

import tatsu
from pprint import pprint

@pytest.fixture
def demo_actions():
    """Return an **instance** of visitor with (semantics) actions, or None."""
    return None

@pytest.fixture
def demo_grammar(demo_actions):
    with open('pytst/demo_grammar.tatsu') as f:
        grammar = f.read()
        parser = tatsu.compile(grammar, semantics=demo_actions)
        return parser

def test_0(demo_grammar):
    txt = """\
@impliciet(Main)
implement Elemental_HelloWorld
{
}
"""
    ast = demo_grammar.parse(txt)
    pprint(ast)
    assert ast[0][0] == '@'
    assert ast[0][1] == 'impliciet'
    assert ast[0][2][1] == ['Main']

    assert ast[1][0] == 'implement'
    assert ast[1][1] == 'Elemental_HelloWorld'
    assert ast[1][2] == '{'
    assert ast[1][3] == '}'

        



