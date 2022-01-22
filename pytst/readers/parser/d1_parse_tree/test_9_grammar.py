import pytest
from pathlib import Path
import os

from castle.readers.parser import grammar
import arpeggio

def parse_file(filename, dir=Path('..')):
    path_to_current_test = Path(os.path.realpath(__file__))
    path_to_current_dir = path_to_current_test.parent
    with (path_to_current_dir / dir / filename).open() as f:
        txt = f.read()

    parser = arpeggio.ParserPython(grammar.peg_grammar, grammar.comment, debug=False)
    tree = parser.parse(txt)

    assert tree.position_end == len(txt) , f"Not parsed whole input; Only: >>{regex[tree.position: tree.position_end]}<<; Not: >>{regex[tree.position_end:]}<<."

    print("\nPARSE TREE\n" + tree.tree_str())
    return tree

def test_grammar(): parse_file("grammar.peg")
