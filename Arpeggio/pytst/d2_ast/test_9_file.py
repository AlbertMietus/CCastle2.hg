import pytest
import logging; logger = logging.getLogger(__name__)
from pathlib import Path
import os
import grammar
from castle import peg # has the AST classes

from . import parse, assert_ID

def parse_file(filename, dir=Path('..')):
    path_to_current_test = Path(os.path.realpath(__file__))
    path_to_current_dir = path_to_current_test.parent
    with (path_to_current_dir / dir / filename).open() as f:
        txt = f.read()
    ast = parse(txt, grammar.peg_grammar, with_comments=True)

    return ast


def test_grammar():
    parse_file("grammar.peg")
    ...                                                                 # XXX
    assert False, "Need more work"
