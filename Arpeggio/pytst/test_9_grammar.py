import pytest

from grammar import *

show_dot=True

def parse_file(filename, dir="pytst"):
    with open(dir +"/" + filename) as f:
        txt = f.read()

    parser = ParserPython(peg_grammar, comment, debug=show_dot)
    tree = parser.parse(txt)

    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{regex[tree.position: tree.position_end]}<<; Not: >>{regex[tree.position_end:]}<<."
    return tree

def test_grammar(): parse_file("grammar.peg")
