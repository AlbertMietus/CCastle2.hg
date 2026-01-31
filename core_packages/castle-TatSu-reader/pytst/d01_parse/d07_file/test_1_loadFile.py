# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle import aigr
from castle.readers.ladon.parser import CastleParser
from castle.readers.ladon.load_files import SimpleFileReader

from pprint import pprint

@pytest.fixture
def myDir() ->Path:
    import os
    return Path(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def loaderCls():
    return SimpleFileReader

def test_1_Load_EmptyFile(myDir, loaderCls):
    ast = loaderCls(myDir/"empty.Castle").parse()
    assert isinstance(ast, aigr.Source_NS)

    pprint(ast)
    assert False, "More tests are needed"


