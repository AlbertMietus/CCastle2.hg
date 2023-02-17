# (C) Albert Mietus, 2022, 2023. Part of Castle/CCastle project

import logging; logger = logging.getLogger(__name__)
import pytest

from castle.writers.CC2Cpy.Component import * # CC_B_ComponentInterface
from castle.writers.CC2Cpy.Protocol import * #CC_EventProtocol

########## empty ##########
def emptyComp():
    return CC_B_ComponentInterface('empty')

ref_emptyComp="""\
struct CC_B_ComponentInterface cc_CI_empty = {
 .name          = "empty",
 .inherit_from  = NULL,
 .length        = 0,
 .ports = {
 },
} ;
"""

ref_emptyClass="""\
struct CC_B_ComponentClass  cc_C_empty = {
 .isa           = NULL,
 .interface     = &cc_CI_empty,
 .instance_size = sizeof(CC_C_empty),
 .methods       = cc_S_empty_methods,
};
"""

########## demo2Comp ##########
def demo2Comp():
    jap = CC_EventProtocol("JustAProtocol", events=[], based_on=None)
    return CC_B_ComponentInterface('demo2Comp', ports =[
        CC_Port(name='no_1', type=None, direction=CC_PortDirection.In),
        CC_Port(name='jap2', type=jap)])

ref_demo2Comp="""\
struct CC_B_ComponentInterface cc_CI_demo2Comp = {
 .name          = "demo2Comp",
 .inherit_from  = NULL,
 .length        = 2,
 .ports = {
  {
   .portNo    =  0,
   .protocol  =  NULL,
   .direction =  CC_B_PortDirectionIs_in,
   .name      = "no_1",
   .part_of   = &cc_CI_demo2Comp },
  {
   .portNo    =  1,
   .protocol  = &cc_P_JustAProtocol,
   .direction =  CC_B_PortDirectionIs_UNKNOWN,
   .name      = "jap2",
   .part_of   = &cc_CI_demo2Comp },
 },
} ;
"""

ref_demo2Class="""\
struct CC_B_ComponentClass  cc_C_demo2Comp = {
 .isa           = NULL,
 .interface     = &cc_CI_demo2Comp,
 .instance_size = sizeof(CC_C_demo2Comp),
 .methods       = cc_S_demo2Comp_methods,
};
"""

########## subComp ##########
def subComp(base):
    return CC_B_ComponentInterface('sub', based_on=base)

ref_subComp="""\
struct CC_B_ComponentInterface cc_CI_sub = {
 .name          = "sub",
 .inherit_from  = &cc_CI_demo2Comp,
 .length        = 0,
 .ports = {
 },
} ;
"""
