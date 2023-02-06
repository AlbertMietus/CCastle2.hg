# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)

import pytest

from . import * # CCompare

from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol
from castle.writers.CC2Cpy.Event import CC_Event
from castle.writers.CC2Cpy.CCbase import CC_TypedParameter

###
### NOTE
###
### The leading whitespace in the `ref_...` strings are relevant.
### Each space is an 'indent'; the renderXXX() formating uses this
### It does change the prepend/indent and counts the have "the same" number

@pytest.fixture
def emptyProtocol():
    return CC_EventProtocol("EMPTY", events=[], based_on=None)

ref_emptyProtocol_struct="""\
struct CC_B_Protocol cc_P_EMPTY = {
 .name           = "EMPTY",
 .kind           = CC_B_ProtocolKindIs_Event,
 .inherit_from   = NULL,
 .length         = 0,
 .events         = {
 }
};
"""

@pytest.fixture
def simpleSieve():
    return CC_EventProtocol("SimpleSieve", events=[CC_Event("input", typedParameters=[CC_TypedParameter(name='event', type=int)])])

ref_simpleSieve="""\
struct CC_B_Protocol  cc_P_SimpleSieve = {
 .name           = "SimpleSieve",
 .kind           = CC_B_ProtocolKindIs_Event,
 .inherit_from   = &cc_P_Protocol,
 .length         = 1,
 .events         = {
  { .seqNo = 0,   .name = "input",   .part_of = &cc_P_SimpleSieve },
 }
};
"""

@pytest.fixture
def demoProtocol():
    return CC_EventProtocol("DEMO",
                            events=[
                                    CC_Event("demoEventA"),
                                    CC_Event("demoEventB"),
                                    CC_Event("demoEventC"),
                                    CC_Event("demoEventD"),
                                    CC_Event("demoEventE"),
                                    CC_Event("demoEventF")])

ref_demo_struct="""\
struct CC_B_Protocol cc_P_DEMO = {
 .name           = "DEMO",
 .kind           = CC_B_ProtocolKindIs_Event,
 .inherit_from   = &cc_P_Protocol,
 .length         = 6,
 .events         = {
  {  .seqNo   = 0,   .name    = "demoEventA",   .part_of = &cc_P_DEMO },
  {  .seqNo   = 1,   .name    = "demoEventB",   .part_of = &cc_P_DEMO },
  {  .seqNo   = 2,   .name    = "demoEventC",   .part_of = &cc_P_DEMO },
  {  .seqNo   = 3,   .name    = "demoEventD",   .part_of = &cc_P_DEMO },
  {  .seqNo   = 4,   .name    = "demoEventE",   .part_of = &cc_P_DEMO },
  {  .seqNo   = 5,   .name    = "demoEventF",   .part_of = &cc_P_DEMO },
 }
};
"""

ref_demo_index="""\
#define CC_P_DEMO_demoEventA  0
#define CC_P_DEMO_demoEventB  1
#define CC_P_DEMO_demoEventC  2
#define CC_P_DEMO_demoEventD  3
#define CC_P_DEMO_demoEventE  4
#define CC_P_DEMO_demoEventF  5
"""

ref_demo_FTs="""\
typedef void (*CC_E_DEMO_demoEventA_FT)(CC_selfType, CC_ComponentType, );
typedef void (*CC_E_DEMO_demoEventB_FT)(CC_selfType, CC_ComponentType, );
typedef void (*CC_E_DEMO_demoEventC_FT)(CC_selfType, CC_ComponentType, );
typedef void (*CC_E_DEMO_demoEventD_FT)(CC_selfType, CC_ComponentType, );
typedef void (*CC_E_DEMO_demoEventE_FT)(CC_selfType, CC_ComponentType, );
typedef void (*CC_E_DEMO_demoEventF_FT)(CC_selfType, CC_ComponentType, );
"""
ref_demo="\n".join([ref_demo_struct, ref_demo_index, ref_demo_FTs])


def test_0_isEvent(demoProtocol):
    assert demoProtocol.kind == CC_ProtocolKind.Event

def test_1_events_demo(demoProtocol):
    events = demoProtocol.event_dict()
    assert isinstance(events, dict)
    assert len(events) == 6


def test_2_events_mix():
    a = CC_EventProtocol("A", events=[CC_Event("a1")])
    b = CC_EventProtocol("B", events=[CC_Event("b2"),CC_Event("b3")],based_on=a)

    assert len(b.event_dict(mine=False, inherired=False))  == 0
    assert len(b.event_dict(mine=False, inherired=True))   == 1
    assert len(b.event_dict(mine=True,  inherired=False))  == 2
    assert len(b.event_dict(mine=True,  inherired=True))   == 3

    # are the defaults correct? mine=True inherired=False
    assert len(b.event_dict())  == 2

def test_render(demoProtocol):
    assert CCompare(ref_demo, demoProtocol.render())

def test_render_struct_sieve(simpleSieve):
    assert CCompare(ref_simpleSieve, simpleSieve.render_struct())

def test_emptyProtocol(emptyProtocol):
    # the "struct" is minimal"
    assert CCompare(ref_emptyProtocol_struct, emptyProtocol.render_struct())
    # and the other parts are absent
    assert CCompare(ref_emptyProtocol_struct, emptyProtocol.render())


def test_whitespace(emptyProtocol):
    # More or less leading whitespace should not have effect
    assert CCompare(ref_emptyProtocol_struct, emptyProtocol.render(prepend="\t\t", indent=""))

def verify_prepend(protocol): # prepend shoud be on any (not empty) line
    prepend="PREPEND_"
    out = protocol.render(prepend=prepend)
    logger.info("Protocol %s results in::\n%s", protocol.name, out)
    for l in out.splitlines():
        if len(l)>0:
            assert l.startswith(prepend)
            assert not l[len(prepend):].startswith(prepend) # No more prepend's

def test_prepend_empty(emptyProtocol):
    verify_prepend(emptyProtocol)

def test_prepend_simpleSieve(simpleSieve):
    verify_prepend(simpleSieve)

def test_prepend_demo(demoProtocol):
    verify_prepend(demoProtocol)


def test_indent_empty(emptyProtocol):
    verify_indents(ref_emptyProtocol_struct, emptyProtocol.render_struct)

def test_indent_simpleSieve(simpleSieve):
    verify_indents(ref_simpleSieve, simpleSieve.render_struct)

def test_indent_demo(demoProtocol):
    verify_indents(ref_demo, demoProtocol.render_struct)


def test_prepend_indexes(demoProtocol):
    assert CCompare(ref_demo_index, demoProtocol.render_indexes())
    assert CCompare(ref_demo_index, demoProtocol.render_indexes(prepend=""))
    assert CCompare(ref_demo_index, demoProtocol.render_indexes(prepend="\t"))

def test_prepend_FTs(demoProtocol):
    assert CCompare(ref_demo_FTs, demoProtocol.render_FTs())
    assert CCompare(ref_demo_FTs, demoProtocol.render_FTs(prepend=""))
    assert CCompare(ref_demo_FTs, demoProtocol.render_FTs(prepend="\t"))
