# (C) Albert Mietus, 2025,2026. Part of Castle/CCastle project
import logging; logger = logging.getLogger(__name__)
import pytest

import typing as PTH                                                                                  # Python TypeHints

from castle import aigr




def verify_parms_tuple(parms, length):
    assert isinstance(parms, tuple), f"Expecting a tuple, got: {type(parms)} :: {parms}"
    assert len(parms) == length,     f"Expecting {length} parameter(s), got {len(parms)}"


def verify_parm(parm, name, type_, check_optional=False):
    assert isinstance(parm, aigr.TypedParameter), f"Expecting a TypedParameter, got: {type(parm)} :: {parm}"
    assert isinstance(parm.name, aigr.ID) and parm.name == name, f"Expecting {aigr.ID(name)=}, got {parm.name!r}"
    assert parm.type == type_, f"Expecting type {type_=!r}, got {parm.type!r} for {parm=}"
    assert isinstance(parm.type, aigr.ID)
    assert isinstance(parm.type.context, aigr.base.names.Ref) # Note aigr.base.names.Ref) != aigr.ID.Ref
    if check_optional:
        assert False, "optional parameters not yet supported in AIGR"



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
            _verify_Event(event=proto.events[i], name=name_spec, parms=parm_spec, return_type=return_spec)


def _verify_Event(event, name, parms, return_type=None):
    assert event.name == name
    assert event.return_type == return_type, f"Got {event.return_type=}, exported: {return_type=}"
    assert len(event.typedParameters) == len(parms)
    for i, p_spec in enumerate(parms):
        name_spec, type_spec = p_spec[0], p_spec[1]
        got_parm = event.typedParameters[i]
        assert isinstance(got_parm, aigr.TypedParameter)
        assert isinstance(got_parm.name, aigr.ID) and got_parm.name == name_spec, f"Wrong parm[{i}] -- {got_parm.name=} not {name_spec=} for {event.name}"
        assert isinstance(got_parm.type, aigr.ID) and got_parm.type == type_spec, f"Wrong parm[{i}] -- {got_parm.type=} not {type_spec=} for {event.name}"

def verify_ComponentInterface(comp, name, base:PTH.Optional[aigr.ID]=None, ports_spec=None):
    """ ports_spec ::= SEQUENCE[ ( name, type, direction) ] """
    assert isinstance(comp, aigr.ComponentInterface), f"Expecting an ComponentInterface, got: {comp}"
    # direct attributes
    assert comp.name == name
    assert comp.based_on is None or str(comp.based_on) == base
    if ports_spec:
        # ports
        assert len(comp.ports) == len(ports_spec)
        for i, p_spec in enumerate(ports_spec):
            _verify_Port(comp.ports[i], *p_spec)


def _verify_Port(port, name:str, type:str, direction:aigr.PortDirection.In):
    assert isinstance(port, aigr.Port), f"{port=}"
    assert isinstance(port.name, aigr.ID) and port.name == name, f"Got: {port.name=} -- expecting {name=}"
    assert isinstance(port.type, aigr.ID) and port.type == type, f"Got: {port.type=} -- expecting {type=}"
    assert isinstance(port.direction, aigr.PortDirection) and port.direction is direction, f"Got: {port.direction=} -- expecting {direction}"



def verify_ComponentImplementation(comp, name, parameters=[], handlers=0, local_names=[]):
    # parameters: [(name,type), ....]
    assert isinstance(comp, aigr.ComponentImplementation)
    # direct attributes
    assert comp.name == name
    assert comp.interface is None               #XXXX
    assert len(comp.parameters) == len(parameters), f"Expected {len(parameters)=}, got {comp.parameters=}"
    
    # check (number of) local names
    assert len(comp.handlers)   == handlers,   f"Expected {handlers=}, got {comp.handlers=}"
    for l_name in local_names:
        assert l_name in comp._ns, f"Expected {l_name=} not in {comp._ns.keys()=}"

    # check the parameters
    assert len(comp._ns)        == len(local_names),   f"Expected {len(local_names)=}, got {comp._ns=} -- Spec:{local_names=}"
    for (got,spec) in zip(comp.parameters, parameters, strict=True):
        name, type_ = spec[0], spec[1]
        verify_parm(got, name, type_)        
    
    # inherited via _hasScope --|> Scope --|> _NameSpace
    assert isinstance(comp._ns,      dict)
    assert isinstance(comp.outer_ns, (dict, type(None))) #.outer_ns is a ref that can be empty ...
    #handlers's outer_ns should be comp
    for h in comp.handlers:
        assert h.outer_ns == comp, f"{h.outer_ns=} of {h.name=} does not point to Comp ({comp.name}): -- {h.outer_ns=}"


