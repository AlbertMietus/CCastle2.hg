# (C) Albert Mietus, 2025. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

TESTDOUBLES = Path('TestDoubles')

@pytest.fixture
def TestDoubles_dir():
    import os;
    dir = Path(os.getcwd())
    while not (dir / TESTDOUBLES).exists():
        assert str(dir)!=str(dir.parent), f"Can't find {TESTDOUBLES}-dir from {os.getcwd()}" # .f.e. `dir` has become root
        dir = dir.parent
    the_dir = dir / TESTDOUBLES
    assert the_dir.is_dir(), f"found {the_dir}, but it isn't a dir"
    return the_dir


