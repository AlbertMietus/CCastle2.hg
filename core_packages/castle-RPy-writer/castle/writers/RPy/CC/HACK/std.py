# (C) Albert Mietus, 2025.  Part of Castle/CCastle project

from castle.writers.RPy.CC import buildin
from castle.writers.RPy.CC import base

"""///CastleCode
protocol std : EventProtocol {
   invoke();
   stdin(line:txt);  //Todo
   stdout(line:txt); //ToDo
   stderr(line:txt); //ToDo
}"""
cc_P_std = buildin.CC_B_Protocol(
    name="std",
    kind=buildin.CC_ProtocolKind.Event,
    inherit_from=-1,                        #XXX
    events=[]) # event are added below
cc_P_std.events.append(buildin.CC_B_P_EventID(name="invoke", seqNo=-99, part_of=cc_P_std))
cc_P_std.events.append(buildin.CC_B_P_EventID(name="stdin",  seqNo=-99, part_of=cc_P_std))
cc_P_std.events.append(buildin.CC_B_P_EventID(name="stdout", seqNo=-99, part_of=cc_P_std))
cc_P_std.events.append(buildin.CC_B_P_EventID(name="stderr", seqNo=-99, part_of=cc_P_std))


"""///CastleCode
component Main : Component {
   port std<bidir>:std; // Or spilt it?
}"""
cc_CI_Main = buildin.CC_B_ComponentInterface(
    name           = "Main",
    inherit_from   = base.cc_CI_Component,
    ports          = []) # ports are added below
cc_CI_Main.ports.append(buildin.CC_B_C_PortID(
    name="std",
    portNo=0,
    protocol=cc_P_std,
    direction=buildin.CC_PortDirection.BiDir,
    part_of=cc_CI_Main))
