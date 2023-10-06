# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin
from CC import base

#Put the Castle/generated imports here
import SimpleSieve


cc_CI_Sieve = buildin.CC_B_ComponentInterface(name="Sieve",
                                inherit_from=base.cc_CI_Component,
                                ports=[])
cc_CI_Sieve.ports.append(buildin.CC_B_C_PortID(name="try",
                                portNo=2,   # XXXX
                                protocol=SimpleSieve.cc_P_SimpleSieve,
                                direction=buildin.PortDirection.In,
                                part_of=cc_CI_Sieve))
cc_CI_Sieve.ports.append(buildin.CC_B_C_PortID(name="coprime",
                                portNo=3,      #XXX
                                protocol=SimpleSieve.cc_P_SimpleSieve,
                                direction=buildin.CC_B_PortDirection.Out,
                                part_of=cc_CI_Sieve))

