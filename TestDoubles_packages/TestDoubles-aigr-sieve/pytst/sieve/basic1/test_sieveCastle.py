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

@pytest.fixture
def event_handler(comp):
      # Notes
      ##  - event(`input`) -- this protocol has only one event, so its simple
      ##  - port('try')    -- thats the 1ste one. But keep it in sync (CastleCode is leading)
    (protocol, event, port)  = protocols.SimpleSieve, protocols.SimpleSieve.events[0], components.SieveMoat.ports[0]
    handler = find_name_in_body(mangle_event_handler(protocol=protocol.name,  event=event.name,  port=port.name), comp.body)
    assert isinstance(handler, aigr.EventHandler), f"Expected EventHandler, got {handler} (type={type(handler)})" # Not a test, only to check.
    logger.debug("Found <%s> as event_handler", handler)
    return handler


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

def test_2_handler_on_try(event_handler):
    verify_IDref(event_handler.protocol, "SimpleSieve")
    verify_IDref(event_handler.event,    "input")
    verify_IDref(event_handler.port,     "try")


def test_3a_EH_is_one_statement(event_handler):
    "This eventhandler has basically one (multiline) statement: an if an 1 statement inside"
    body = event_handler.body
    assert isinstance(body, aigr.Body), f"any EH Should have a Body (instance), but found {body} (type={type(body)})"
    assert len(body)==1, f"Expected a single (long) statement, but found {len(body)} statement(s)"


def test_3b_EH_is_one_if(event_handler):
    if_statement=event_handler.body[0]
    assert isinstance(if_statement, aigr.If) # Not a test, only to check.

    test = if_statement.test
    then = if_statement.body
    orelse = if_statement.orelse
    logger.debug("if_statement: test=%s, then=%s, orelse=%s", test,then,orelse)

    assert isinstance(test, aigr.expressions._expression) # The expressions itself is below
    assert isinstance(then, aigr.Body) and len(then)==1   # The statement is tested below
    assert orelse is None


def test_3c_EH_test_exps(event_handler):
    if_statement = event_handler.body[0]
    test = if_statement.test

    assert False, "ToDo if-expr"


def test_3d_EH_then_send(event_handler):
    if_statement=event_handler.body[0]
    then = if_statement.body
    assert len(then) == 1 # Not a test, only to check.
    send = then[0]

    assert False, "ToDo if-then"

