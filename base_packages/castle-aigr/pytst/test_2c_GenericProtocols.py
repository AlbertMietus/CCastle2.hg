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

    In the AIGR, the specialised *SlowStart(1)* protocol is modeled by a ``Specialise`` wrapper; which in placed
    in-between (the generic) Slowstart and SimpleSieve.

    .. hint:: (implementation of Generic Protocols)

       With ``functools.partial``, it seams possible to make a "partial class". BUT, that is NOT VALID RPython!
       (see:  .../PyPy+Rpython/new/partialCLass.py).

       So, it will be implemented in normal the normale AST-->AIGT-->AIGT-->RPY train (as in C++ template's): just fill in
"""

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.aigr import Protocol, ProtocolKind
from castle.aigr import Event, EventProtocol
from castle.aigr.aid import TypedParameter, Argument, Specialise

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
    return EventProtocol("Sub_a", events=[], based_on=Specialise(name="", based_on=base, arguments=(Argument(name='queue_max', value=1),)))

@pytest.fixture
def sub_b(base):
    return EventProtocol("Sub_b", events=[], based_on=Specialise(None, based_on=base, arguments=(Argument(value=1),)))

def assert_GP_kind(base, sub):
    assert sub.kind == base.kind
    assert sub.based_on.kind == base.kind
    assert sub.based_on.based_on is base

def test_GenericProtocol_kind_a(base, sub_a):
    assert_GP_kind(base, sub_a)

def test_GenericProtocol_kind_b(base, sub_b):
    assert_GP_kind(base, sub_b)

class EventProtocol_Spy(EventProtocol):
    def __init__(self, *t,**d):
        super().__init__(*t, **d)
        self._trace=["init"]

    def _noEvents(self):
        n = super()._noEvents()
        self._trace.append(f'noEvents={n}')
        return n
    def mole(self):
        TXT="I'm a mole, and do not exist in real classes"
        self._trace.append(TXT)
        return TXT

def test_GenericProtocol_Spydelegate():
    spy = EventProtocol_Spy("SpyBase", events=[], typedParameters=[TypedParameter(name='queue_max', type=int)])
    specialised = Specialise("", based_on=spy, arguments=(Argument(value=1),))

    assert specialised._noEvents() == 0
    assert spy._trace[-1] == "noEvents=0"
    assert spy.mole() == spy._trace[-1]




