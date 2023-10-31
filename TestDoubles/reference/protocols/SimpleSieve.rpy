# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin

#Put the Castle/generated imports here
from CC import base

import SlowStart


##
## EventIndexes (All 1 events of SlowStart_1)
##

CC_P_SlowStart_1_setMax = 0


##
## EventIndexes (All 1 events of SimpleSieve)
##

CC_P_SimpleSieve_input = 1


cc_P_SlowStart_1 = buildin.CC_B_Protocol(name="SlowStart_1",
                                kind=buildin.ProtocolKind.Event,
                                inherit_from=SlowStart.cc_P_SlowStart,
                                events=[])

cc_P_SlowStart_1.events.append(buildin.CC_B_P_EventID(name="setMax",
                                seqNo=CC_P_SlowStart_1_setMax,
                                part_of=cc_P_SlowStart_1))

cc_P_SimpleSieve = buildin.CC_B_Protocol(name="SimpleSieve",
                                kind=buildin.ProtocolKind.Event,
                                inherit_from=SlowStart_1.cc_P_SlowStart_1,
                                events=[])

cc_P_SimpleSieve.events.append(buildin.CC_B_P_EventID(name="input",
                                seqNo=CC_P_SimpleSieve_input,
                                part_of=cc_P_SimpleSieve))

