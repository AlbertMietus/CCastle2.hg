# (C) Albert Mietus, 2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
#import pytest

import ast
from castle.writers.RPy.aid import Block


def verify_ValidPython(txt):
    assert isinstance(txt, (str, Block)), f"Should be a TextBlock, NOT {type(txt)} --{txt=}"

    text = str(txt)     # txt can be  a string of a (Text)Block; so make it a string
    text= text.strip()  # Ingonre leading (and training) space
    try:
        ast.parse(text)
    except SyntaxError:
        logger.warning("text is not parsable: >>%s<<", txt)
        assert False, f"Not valid Python: {text=}"

