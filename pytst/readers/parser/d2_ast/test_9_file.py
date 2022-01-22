import pytest
import logging; logger = logging.getLogger(__name__)
from pathlib import Path
import os

from castle.readers.parser import grammar
from castle.ast import peg

from . import parse, assert_PEG

def parse_file(filename, dir=Path('..')):
    path_to_current_test = Path(os.path.realpath(__file__))
    path_to_current_dir = path_to_current_test.parent
    with (path_to_current_dir / dir / filename).open() as f:
        txt = f.read()
    ast = parse(txt, grammar.peg_grammar, with_comments=True)

    return ast


def test_grammar():
    ast = parse_file("grammar.peg")
    assert_PEG(ast)
