# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

from castle import aigr

from . import *

def test_1a_SimpleEventProto(castle_parser):
    txt = """\
protocol SimpleProto {
    anEvent(parm :type);
    anotherEvent(p1:t1, p2:t2);
}
"""
    proto = castle_parser(txt, start='protocol_definition')
    logger.debug(f"{txt=} ==> {proto=}")
    verify_EventProtocol(proto, name="SimpleProto", events_spec =[
        ('anEvent',      [('parm', 'type')]),
        ('anotherEvent', [('p1', 't1'), ('p2', 't2')])])


def test_1b_EventWithReturnType(castle_parser):
    txt = """\
protocol EventWithReturnType {
    anEvent(parm :type1) -> type2;
}
"""
    proto = castle_parser(txt, start='protocol_definition')
    logger.debug(f"{txt=} ==> {proto=}")
    verify_EventProtocol(proto, name="EventWithReturnType", events_spec=[
        ('anEvent', [('parm', 'type1'),], 'type2')])


def test_2_StartSieve(castle_parser):
    txt = """\
protocol StartSieve :EventProtocol {
     runTo(max :int);
     newMax(max :int);
}
"""
    proto = castle_parser(txt, start='protocol_definition')
    logger.debug(f"{txt=} ==> {proto=}")
    verify_EventProtocol(proto, name="StartSieve", base='EventProtocol', events_spec=[
        ('runTo',  [('max', 'int'),]),
        ('newMax', [('max', 'int'),])])


