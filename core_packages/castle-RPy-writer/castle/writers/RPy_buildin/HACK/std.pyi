# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.HACK.std``.
# HACK module: hard-coded "std" protocol and "Main" component interface.

import typing as PTH
from ..buildin.CC_B_Protocol import CC_B_Protocol
from ..buildin.CC_B_ComponentInterface import CC_B_ComponentInterface

cc_P_std: CC_B_Protocol
"""Hard-coded ``std`` protocol (invoke, stdin, stdout, stderr events).

This is a temporary HACK providing a standard I/O protocol until the Castle
compiler can generate it from source.  It mirrors the Castle declaration::

    protocol std : EventProtocol {
        invoke();
        stdin(line:txt);
        stdout(line:txt);
        stderr(line:txt);
    }
"""

cc_CI_Main: CC_B_ComponentInterface
"""Hard-coded ``Main`` component interface with a single bidir ``std`` port.

Mirrors the Castle declaration::

    component Main : Component {
        port std<bidir>:std;
    }
"""
