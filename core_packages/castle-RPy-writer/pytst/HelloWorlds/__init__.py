# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.writers.RPy.writers import Renderer

@pytest.fixture
def my_renderer() ->Renderer:
    cls = Renderer
    logger.debug(f'Using "{cls}" as Renderer')
    return cls()

def verify_line(expect, got, line=None):
    txt = got.splitlines()[line] if line else got
    assert expect in txt, f"Expected: {expect}...., got: {txt}"

def print_out(txt):
    print(f"\n=====[print]=====\n{txt}\n=====[ end ]=====\n")
