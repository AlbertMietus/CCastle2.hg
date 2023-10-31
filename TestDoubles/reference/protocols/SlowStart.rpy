# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin

#Put the Castle/generated imports here
from CC import base



##
## EventIndexes (All 1 events of SlowStart)
##

CC_P_SlowStart_setMax = 0


cc_P_SlowStart = buildin.CC_B_Protocol(name="SlowStart",
                                parameters=(
                                    ('queue_max', int),
                                ),
                                kind=buildin.ProtocolKind.Event,
                                inherit_from=base.cc_P_Protocol,
                                events=[])

cc_P_SlowStart.events.append(buildin.CC_B_P_EventID(name="setMax",
                                seqNo=CC_P_SlowStart_setMax,
                                part_of=cc_P_SlowStart))

