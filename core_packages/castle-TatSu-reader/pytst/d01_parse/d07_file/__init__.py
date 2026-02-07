# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from pathlib import Path
from pprint import pprint, pformat

from castle import aigr
from castle.aigr_extra.scaffolding import ScaffolderNameSpace
from castle.readers.ladon.loaders import SimpleFileLoader

@pytest.fixture
def myDir() ->Path:
    import os
    return Path(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def load_and_wrap(myDir) -> aigr.Source_NS:
    def do_it(filename):
        loader = SimpleFileLoader(myDir/filename)
        ast = loader.parse()
        assert isinstance(ast, aigr.Source_NS)
        logger.info(pformat(ast))                          #Info->debug
        return ScaffolderNameSpace(ast)
    return do_it


def validate_topAst(ast, filename, names:list[str]=[] ):
    assert isinstance(ast, aigr.Source_NS)
    logger.debug(pformat(ast))
    assert ast.name == filename
    assert ast.outer_ns is None

    assert len(ast._ns) == len(names)
    for n in names:
        assert n in ast._ns


