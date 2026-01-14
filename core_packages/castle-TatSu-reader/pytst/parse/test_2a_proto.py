# (C) Albert Mietus, 2025,2026- Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

import typing as PTH                                                                                  # Python TypeHints
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


def test_protocol_definition_IS_interface_definitions(castle_parser):
    txt = """\
protocol SimpleProto {
    anEvent(parm :type);
    anotherEvent(p1:t1, p2:t2);
}
"""
    interfaces = castle_parser(txt, start='interface_definitions')
    assert isinstance(interfaces, list) and len(interfaces) == 1, f"Expecting a list of 1 EventProtocol, {got=}"
    verify_EventProtocol(interfaces[0], name="SimpleProto", events_spec =[
        ('anEvent',      [('parm', 'type')]),
        ('anotherEvent', [('p1', 't1'), ('p2', 't2')])])



def verify_EventProtocol(proto, name, base=None, events_spec=None):
    """ events_spec ::= SEQUENCE[ event-name, <parm-list>, PTH.Optional[return_type] ]
        parm-list   ::= SEQUENCE[ TUPLE( ID<name>, ID<type> ) ] """
    assert isinstance(proto, aigr.Protocol) and (proto.kind == aigr.ProtocolKind.Event)
    assert isinstance(proto, aigr.EventProtocol)
    assert proto.name == name
    assert proto.based_on is None or str(proto.based_on) == base
    if events_spec:
        assert len(proto.events) == len(events_spec)
        for i, spec in enumerate(events_spec):
            name_spec   = spec[0]
            parm_spec   = spec[1]
            return_spec = spec[2] if len(spec)==3 else None
            verify_Event(event=proto.events[i], name=name_spec, parms=parm_spec, return_type=return_spec)


def verify_Event(event, name, parms, return_type=None):
    assert event.name == name
    assert event.return_type == return_type, f"Got {event.return_type=}, exported: {return_type=}"
    assert len(event.typedParameters) == len(parms)
    for i, p_spec in enumerate(parms):
        name_spec, type_spec = p_spec[0], p_spec[1]
        got_parm = event.typedParameters[i]
        assert isinstance(got_parm, aigr.TypedParameter)
        assert isinstance(got_parm.name, aigr.ID) and got_parm.name == name_spec, f"Wrong parm[{i}] -- {got_parm.name=} not {name_spec=} for {event.name}"
        assert isinstance(got_parm.type, aigr.ID) and got_parm.type == type_spec, f"Wrong parm[{i}] -- {got_parm.type=} not {type_spec=} for {event.name}"


