# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import pytest

from . import * # CCompare


from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol
from castle.writers.CC2Cpy.Event import CC_Event
from castle.writers.CC2Cpy.CCbase import CC_TypedParameter

@pytest.fixture
def simpleSieve():
    return CC_EventProtocol("SimpleSieve", events=[CC_Event("input", typedParameters=[CC_TypedParameter(name='event', type=int)])])

ref_simpleSieve="""
   struct CC_B_Protocol  cc_P_SimpleSieve = {
      .name           = "SimpleSieve",
      .kind           = CC_B_ProtocolKindIs_Event,
      .inherit_from   = &cc_P_Protocol,
      .length         = 1,
      .events         = {
         { .seqNo = 0,   .name = "input",   .part_of = &cc_P_SimpleSieve }, } };"""


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


ref_DemoProtocol="""
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

   #define CC_P_DEMO_demoEventA  0
   #define CC_P_DEMO_demoEventB  1
   #define CC_P_DEMO_demoEventC  2
   #define CC_P_DEMO_demoEventD  3
   #define CC_P_DEMO_demoEventE  4
   #define CC_P_DEMO_demoEventF  5

   typedef void (*CC_E_DEMO_demoEventA_FT)(CC_selfType, CC_ComponentType, );
   typedef void (*CC_E_DEMO_demoEventB_FT)(CC_selfType, CC_ComponentType, );
   typedef void (*CC_E_DEMO_demoEventC_FT)(CC_selfType, CC_ComponentType, );
   typedef void (*CC_E_DEMO_demoEventD_FT)(CC_selfType, CC_ComponentType, );
   typedef void (*CC_E_DEMO_demoEventE_FT)(CC_selfType, CC_ComponentType, );
   typedef void (*CC_E_DEMO_demoEventF_FT)(CC_selfType, CC_ComponentType, );
"""



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
    assert CCompare(ref_DemoProtocol, demoProtocol.render())

def test_render_struct_sieve(simpleSieve):
        assert CCompare(ref_simpleSieve, simpleSieve.render_struct())



@pytest.fixture
def emptyProtocol():
    return CC_EventProtocol("EMPTY", events=[], based_on=None)

ref_emptyProtocol_struct="""
   struct CC_B_Protocol cc_P_EMPTY = {
     .name           = "EMPTY",
     .kind           = CC_B_ProtocolKindIs_Event,
     .inherit_from   = NULL,
     .length         = 0,
     .events         = { }
   };
"""


def test_emptyProtocol(emptyProtocol):
    # the "struct" is minimal"
    assert CCompare(ref_emptyProtocol_struct, emptyProtocol.render_struct())
    # and the other parts are absent
    assert CCompare(ref_emptyProtocol_struct, emptyProtocol.render())


@pytest.mark.skip(reason="CURRENT: busy with testing all part of *C&P CC_EventProtocol")
def test_more(): pass
