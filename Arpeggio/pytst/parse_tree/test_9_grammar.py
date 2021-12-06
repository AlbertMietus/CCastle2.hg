import pytest

from grammar import *


def parse_file(filename):                                               # Assume we run in '.../pytst/.'
    with open(filename) as f:
        txt = f.read()

    parser = ParserPython(peg_grammar, comment)
    tree = parser.parse(txt)

    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{regex[tree.position: tree.position_end]}<<; Not: >>{regex[tree.position_end:]}<<."
    return tree

def test_grammar(): parse_file("grammar.peg")
