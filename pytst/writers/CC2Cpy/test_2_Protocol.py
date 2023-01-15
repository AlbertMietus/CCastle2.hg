# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

from . import * # CCompare

from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol

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

##qazProtocol = CC_EventProtocol("QAZ",
##                               events=[
##                                   CC_Event("qazEventA"),
##                                   CC_Event("qazEventB"),
##                                   CC_Event("qazEventC"),
##                                   CC_Event("qazEventD"),
##                                   CC_Event("qazEventE"),
##                                   CC_Event("qazEventF"),
