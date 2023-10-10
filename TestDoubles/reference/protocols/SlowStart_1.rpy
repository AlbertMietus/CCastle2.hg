# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin
from CC import base

#Put the Castle/generated imports here



##
## EventIndexes (All 1 events of SlowStart_1)
##

CC_P_SlowStart_1_setMax = 0


cc_P_SlowStart_1 = buildin.CC_B_Protocol(name="SlowStart_1",
                                kind=buildin.ProtocolKind.Event,
                                inherit_from=cc_P_SlowStart,
                                events=[])

cc_P_SlowStart_1.events.append(buildin.CC_B_P_EventID(name="setMax",
                                seqNo=CC_P_SlowStart_1_setMax,
                                part_of=cc_P_SlowStart_1))

