# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr
from castle.aigr import ID

from . import *

def test_1_empty_EH(castle_parser):
    txt = """std.invoke() on self.std {}"""
    handler = castle_parser(txt, start='event_handler')
    logger.debug(f"{txt=} ==> {handler=}")

    assert isinstance(handler, aigr.EventHandler)
    assert handler.name == 'std_invoke__std'
    assert isinstance(handler.protocol, ID) and handler.protocol == 'std'
    assert isinstance(handler.event, ID)    and handler.event    == 'invoke'
    assert len(handler.port) == 2
    assert isinstance(handler.port[0], ID)  and handler.port[0]  == 'self'
    assert isinstance(handler.port[1], ID)  and handler.port[1]  == 'std'
    assert isinstance(handler.body, aigr.Body and len(handler.body.statements) == 0), "{handler.body=}"




