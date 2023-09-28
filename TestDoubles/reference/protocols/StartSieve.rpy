# -*- python -*-
# Generated (R)Python file
# (C) Albert Mietus, 2023. Part of Castle/CCastle project

####
from CC import buildin
from CC import base

#Put the Castle/generated imports here



##
## EventIndexes (All 2 events of StartSieve)
##

CC_P_StartSieve_runTo = 0
CC_P_StartSieve_newMax = 1


cc_P_StartSieve = buildin.CC_B_Protocol(name="StartSieve",
				kind=buildin.ProtocolKind.Event,
				inherit_from=cc_P_Protocol
				events = [])
cc_P_StartSieve.events.append(buildin.CC_B_P_EventID(name="runTo",
				seqNo=CC_P_StartSieve_runTo,
				part_of=cc_P_StartSieve ))
cc_P_StartSieve.events.append(buildin.CC_B_P_EventID(name="newMax",
				seqNo=CC_P_StartSieve_newMax,
				part_of=cc_P_StartSieve ))

 

