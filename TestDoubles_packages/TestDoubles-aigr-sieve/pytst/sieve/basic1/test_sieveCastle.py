# (C) Albert Mietus 2024, Part of Castle/CCastle project
"""Test the AIGR TestDoubles of the Sieve protocols (basic1 variant)
   See: http://docideas.mietus.nl/en/default/CCastle/4.Blog/b.TheSieve.html#the-design
"""
import logging; logger = logging.getLogger(__name__)

import pytest


from castle import aigr
from castle.aigr_extra.blend import mangle_event_handler

from castle.TESTDOUBLES.aigr.sieve.basic1 import sieveCastle
from castle.TESTDOUBLES.aigr.sieve.basic1 import protocols, components


from . import find_name_in_body


@pytest.fixture
def comp():
    return sieveCastle.Sieve


def test_0a_types(comp):
    assert isinstance(comp, aigr.ComponentImplementation)
    assert isinstance(comp.interface, aigr.ComponentInterface)
    assert isinstance(comp.parameters, (type(None), tuple))
    assert isinstance(comp.body, aigr.Body)

def test_0b_nameIsName(comp):
    assert comp.name == comp.interface.name
    assert comp.name == 'Sieve'

def test_0c_noParms(comp):
    assert comp.parameters == ()


def test_1_init_has_2lines(comp):
    init = find_name_in_body('init', comp.body)
    assert isinstance(init, aigr.Method), f"Expected an init method, got {init}"
    assert len(init.body)==2, f"Expected that 'init' has 2 statements, but found: {len(init.body.statements)}"


def verify_IDref(id, expected_name):
    assert id == expected_name,              f"ID does not match, expected {expected_name}, got {id}"
    assert isinstance(id, aigr.ID),          f"ID ({id}) is not an ID, but type:{type(id)}"
    assert isinstance(id.context, aigr.Ref), f"found ID '{id}' has not ref"
    # XXX ToDo: check the ref -- for now empty is fine


def test_2_handler_on_try(comp):
    """The event-handler name and the name of protocol/event/port are all text, but ...
       should match the names of the earlier/elsewere defined protocol/event/port structure.
       """
      # Notes
      #@  - event(`input`) -- this protocol has only one event, so its simple
      ##  - port('try')    -- thats the 1ste one. But keep it in sync (CastleCode is leading)
    (protocol, event, port)  = protocols.SimpleSieve, protocols.SimpleSieve.events[0], components.SieveMoat.ports[0]

    handler = find_name_in_body(mangle_event_handler(protocol=protocol.name,  event=event.name,  port=port.name), comp.body)
    assert handler, "No handler found"

    verify_IDref(handler.protocol, protocol.name)
    verify_IDref(handler.event,    event.name)
    verify_IDref(handler.port,     port.name)
