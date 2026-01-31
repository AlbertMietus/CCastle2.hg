# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path

from castle import aigr
from castle.readers.ladon.load_files import SimpleFileLoader

@pytest.fixture
def myDir() ->Path:
    import os
    return Path(os.path.dirname(os.path.abspath(__file__)))

def test_1_Load_EmptyFile(myDir):
    loader = SimpleFileLoader(myDir/"empty.Castle")
    ast = loader.parse()
    assert isinstance(ast, aigr.Source_NS)

    from pprint import pprint,pformat
    assert False, f"{pformat(ast)=}"


