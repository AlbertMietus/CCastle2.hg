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


def verify_ID(id, name, isRef=False, isDef=False, isSet=False):
    assert isinstance(id, aigr.ID), f"Expected an ID, found {type(id)} for {id}"
    assert id == name, f"wrong ID, expected {name}, got {id}"
    if isRef: assert isinstance(id.context, aigr.Ref)
    if isDef: assert isinstance(id.context, aigr.Def)
    if isSet: assert isinstance(id.context, aigr.Set)


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

def test_1a_init_has_2lines(comp):
    init = find_name_in_body('init', comp.body)
    assert isinstance(init, aigr.Method), f"Expected an init method, got {init}"
    assert len(init.body)==2, f"Expected that 'init' has 2 statements, but found: {len(init.body.statements)}"


def test_1b_init_1st_line_superinit(comp):
    """ CastleCode:  super.init(); """
    init = find_name_in_body('init', comp.body)
    line = init.body[0]

    assert isinstance(line, aigr.VoidCall) and isinstance(line.call, aigr.Call)
    callable, arguments = line.call.callable, line.call.arguments

    assert isinstance(callable, aigr.Part)
    assert isinstance(callable.base, aigr.Call) and callable.base.callable == "super" and callable.base.arguments is ()
    verify_ID(callable.attribute, "init", isRef=True)
    assert callable.index is None

    assert arguments is (), f"Expected no arguments, but found: {arguments}"


def test_1c_init_2nd_line_become(comp):
    """ CastleCode: .myPrime := onPrime; """

    init = find_name_in_body('init', comp.body)
    line = init.body[1]

    assert isinstance(line, aigr.Become) and len(line.targets)==1 and len(line.values)==1
    myPrime, onPrime = line.targets[0], line.values[0]

    assert isinstance(myPrime, aigr.Part)
    verify_ID(myPrime.base, "self")
    verify_ID(myPrime.attribute, "myPrime", isSet=True)

    verify_ID(onPrime, "onPrime", isRef=True)


def test_2_handler_on_try(event_handler):
    verify_ID(event_handler.protocol, "SimpleSieve", isRef=True)
    verify_ID(event_handler.event,    "input",       isRef=True)
    verify_ID(event_handler.port,     "try",         isRef=True)


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
    """ CastleCode: try % .myPrime) !=0 """
    if_statement = event_handler.body[0]
    test_expr = if_statement.test

    assert isinstance(test_expr, aigr.Compare) and isinstance(test_expr.ops, aigr.operators.NotEqual) and len(test_expr.values) == 2
    lhs, rhs = test_expr.values[0], test_expr.values[1]

    #The lhs:
    logger.debug("lhs: %s -- ``try %% .myPrime``", lhs)
    assert isinstance(lhs, aigr.expressions._expression) and isinstance(lhs.op, aigr.expressions.operators.Modulo)

    assert len(lhs.values) == 2
    var_try, myPrime = lhs.values[0], lhs.values[1]

    verify_ID(var_try, "try", isRef=True)
    verify_ID(myPrime, "myPrime", isRef=True)

    # The rhs is easy/simple
    logger.debug("rhs: %s -- ``0``", rhs)
    assert isinstance(rhs, aigr.expressions.Constant) and rhs.value==0



def test_3d_EH_then_send(event_handler):
    """ CastleCode: .coprime.input(try); """
    if_statement=event_handler.body[0]
    then = if_statement.body
    assert len(then) == 1 # Not a test, only to check.
    send = then[0]

    assert isinstance(send, aigr.machinery.sendEvent)

    assert isinstance(send.outport, aigr.Part)
    verify_ID(send.outport.base, "self")
    verify_ID(send.outport.attribute, "coprime", isRef=True)

    verify_ID(send.event, "input", isRef=True)

    assert isinstance(send.arguments, (tuple, list)) and len(send.arguments) == 1
    assert isinstance(send.arguments[0], aigr.Argument)
    verify_ID(send.arguments[0].value, "try", isRef=True)

