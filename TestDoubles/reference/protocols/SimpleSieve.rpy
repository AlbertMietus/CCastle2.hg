# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin
from CC import base

import SlowStart_1


##
## EventIndexes (All 1 events of SimpleSieve)
##

CC_P_SimpleSieve_input = 1


cc_P_SimpleSieve = buildin.CC_B_Protocol(name="SimpleSieve",
                                kind=buildin.ProtocolKind.Event,
                                inherit_from=SlowStart_1.cc_P_SlowStart_1,
                                events=[])

cc_P_SimpleSieve.events.append(buildin.CC_B_P_EventID(name="input",
                                seqNo=CC_P_SimpleSieve_input,
                                part_of=cc_P_SimpleSieve))

