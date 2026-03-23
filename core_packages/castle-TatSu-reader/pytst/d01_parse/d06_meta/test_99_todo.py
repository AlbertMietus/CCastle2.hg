# (C) Albert Mietus, 2025- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

#@pytest.mark.skip(reason="'@impliciet()' not in the AIGR yet")
def test_99_rewriter(castle_parser):
    txt = "@impliciet(Main)"
    parms = castle_parser(txt, start='rewriter')
    logger.debug(f"{txt=} ==> {parms=}")

    assert False
