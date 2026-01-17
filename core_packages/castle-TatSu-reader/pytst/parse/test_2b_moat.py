# (C) Albert Mietus, 2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from . import *
from .test_2a_proto import  verify_EventProtocol

def test_AGiven_ProtoDef_canAlsoBeParsedWith_interface_definitions(castle_parser):
    """ This the same test as 'test_2a_proto.py::test_1a_SimpleEventProto, but for the start.
    When `start='interface_definitions'` a list (of 1) is returned."""
    txt = """\
protocol SimpleProto {
    anEvent(parm :type);
    anotherEvent(p1:t1, p2:t2);
}
"""
    interfaces = castle_parser(txt, start='interface_definitions')
    logger.debug(f"{txt=} ==> {interfaces=}")
    assert isinstance(interfaces, list) and len(interfaces) == 1, f"Expecting a list of 1 EventProtocol, got: {interfaces=}"
    verify_EventProtocol(interfaces[0], name="SimpleProto", events_spec =[
        ('anEvent',      [('parm', 'type')]),
        ('anotherEvent', [('p1', 't1'), ('p2', 't2')])])



