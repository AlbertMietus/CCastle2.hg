# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest


from pathlib import Path
from pprint import pprint, pformat

from castle import aigr
from castle.readers.ladon.loaders import SimpleFileLoader

@pytest.fixture
def myDir() ->Path:
    import os
    return Path(os.path.dirname(os.path.abspath(__file__)))

def test_1_Load_EmptyFile(myDir):
    loader = SimpleFileLoader(myDir/"empty.Castle")
    ast = loader.parse()
    validate_topAst(ast, filename="empty")

def test_2_Load_OneStatement(myDir):
    loader = SimpleFileLoader(myDir/"file1.Castle")
    ast = loader.parse()
    validate_topAst(ast, filename="file1", names=['One'])

def validate_topAst(ast, filename, names:list[str]=[] ):
    assert isinstance(ast, aigr.Source_NS)
    logger.debug(pformat(ast))
    assert ast.name == filename
    assert ast.outer_ns is None

    assert len(ast._ns) == len(names)
    for n in names:
        assert n in ast._ns


