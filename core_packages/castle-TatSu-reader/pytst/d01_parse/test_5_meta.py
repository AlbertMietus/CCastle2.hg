# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from . import *

def test_1_impliciet(castle_parser): # XXX no meta-actions (nor :class:`airg.Rewriter` yet)
    txt = """@impliciet(Main)"""
    ast = castle_parser(txt, start='rewriter') ### For now: a dict
    logger.debug(f"{txt=} ==> {ast=}")

    assert isinstance(ast, dict)
    assert ast.hack == '@'

    rewriter = ast['rewriter']
    args     = ast['args']

    assert isinstance(rewriter, ID) and rewriter == 'impliciet'
    assert isinstance (args, (tuple, list))
    assert len(args) == 1
    arg = args[0]
    assert isinstance(arg, aigr.Argument)
    assert arg.name is None
    assert isinstance(arg.value, aigr.Constant)
    assert arg.value.value == 'Main'




    logger.warning("REWRITERs are not supported yet")

