# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import pytest
from pathlib import Path
import tatsu


eHW_frame_NoRewriter = """\
   implement Elemental_HelloWorld
   {
   }
"""

eHW_frame = """\
    @impliciet(Main)
"""+ eHW_frame_NoRewriter

@pytest.fixture
def myPath():
    return Path(__file__).parent

@pytest.fixture
def demo_parser(myPath, grammmar_file):
    with open(myPath  / grammmar_file) as f:
        grammar = f.read()
        parser = tatsu.compile(grammar)
        return parser

