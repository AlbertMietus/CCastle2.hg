# (C) Albert Mietus, 2023. Part of Castle/CCastle project

""" With :file:`test_2b_protocol.py` most/all normal cases are verified. This file focus on **GenericProtocols**:
   GenericProtocols are protocols that inherited from a protocol with parameters. We focus on EventProtocols, but it
   will be entende to all protocols.

    .. code-block: Castle:

       protocol SlowStart(queue_max:int): EventProtocol  ...
       protocol SimpleSieve : SlowStart(1) ...

    * `SlowStart` is a **Generic Protocol** with a (1) parameter: the (initial) (max) size of the queue.
    * `SimpleSieve` used that protocol, and set that parameter to 1.

    The parameter to SlowStart, in SimpleSieve, can be seen as a template-specialisation as it is called in C++

    .. code-block: C++

       // A C++ Template approximation of above: using classes not protocols ...
       template <int queue_max>
       class SlowStart {...}

       class SimpleSieve : SlowStart<1>  { ...}

    In both examples the value ``1`` is filled in (aka hard-coded) into the implementation of SlowStart: Wherever
    `queue_max` is used the value `1` is used -- as if the source always has had a `1`....

    .. note:: The Castle syntax uses parentheses, as for normal (formal) arguments, not chevrons <angle brackets> as in C++

    It read as-if SlowStart is instantiated (as in Python: calling ``SlowStart()``), but actually it is
    **specialised*, by filling in the template/parentheses. The result is a not an instance of SlowStart, but a "new
     Protocol, which kind-of inherits from SlowStart -- and SimpleSieve inherits from that one.

    This *syntax detail* is handled in the parser!

    In the AIGR, the specialised *SlowStart(1)* protocol is modeled by a ProtocolWrapper; which in placed in-between
    (the generic) Slowstart and SimpleSieve. """

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Protocol, ProtocolKind
from castle.aigr import Event, EventProtocol
from castle.aigr.aid import TypedParameter, Argument
from castle.aigr.protocols import ProtocolWrapper

""" There are a few cases
///CastleCode
   protocol Base(queue_max:int): EventProtocol
   protocol Sub_a: Base(queue_max=1)                   # (a): named argument
   protocol Sub_b: Base(1)                             # (b): positional arg

"""


@pytest.fixture
def base():
    return EventProtocol("Base", events=[], typedParameters=[TypedParameter(name='queue_max', type=int)])

@pytest.fixture
def sub_a(base):
    return EventProtocol("Sub_a", events=[], based_on=ProtocolWrapper(based_on=base, arguments=(Argument(name='queue_max', value=1),)))

@pytest.fixture
def sub_b(base):
    return EventProtocol("Sub_b", events=[], based_on=ProtocolWrapper(based_on=base, arguments=(Argument(value=1),)))

def assert_GP_kind(base, sub):
    assert sub.kind == base.kind
    assert sub.based_on.kind == base.kind
    assert sub.based_on.based_on is base

def test_GenericProtocol_kind_a(base, sub_a):
    assert_GP_kind(base, sub_a)

def test_GenericProtocol_kind_b(base, sub_b):
    assert_GP_kind(base, sub_b)


def assert_GP_name(base, sub):
    assert "Wrapper"   in sub.based_on.name
    assert "Base"      in sub.based_on.name

def test_GenericProtocol_name_a(base, sub_a):
    assert_GP_name(base, sub_a)
    assert "queue_max" in sub_a.based_on.name   # the argument-name is only in the (a) version

def test_GenericProtocol_name_b(base, sub_b):
    assert_GP_name(base, sub_b)
    assert "queue_max" not in sub_b.based_on.name   # the argument-name is only in the (a) version



def test_strange_1(base):
    """This is (very) atypical use -- but it helps to get coverage"""
    sub_strange = EventProtocol("SubStrange", events=[], based_on=ProtocolWrapper(name="Strange",
                                                                                  kind=42,
                                                                                  based_on=base,
                                                                                  arguments=(Argument(value=1),)))
    assert sub_strange.based_on.name == "Strange"
    assert sub_strange.based_on.kind == 42, "When we set a strange kind-number it should be stored"

def test_strange_2(base):
    """This is (very) atypical use -- but it helps to get coverage"""
    sub_strange = EventProtocol("SubStrange", events=[], based_on=ProtocolWrapper(name="Strange",
                                                                                  kind=None,
                                                                                  based_on=base,
                                                                                  arguments=(Argument(value=1),)))

    assert sub_strange.based_on.name == "Strange"

