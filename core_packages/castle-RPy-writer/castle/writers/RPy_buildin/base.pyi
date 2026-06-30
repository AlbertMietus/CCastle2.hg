# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.base``.

import typing as PTH
from .buildin.CC_B_ComponentInterface import CC_B_ComponentInterface

cc_CI_Component: CC_B_ComponentInterface
"""The root ``CC_B_ComponentInterface`` instance (name="Component", no ports).

This singleton is the ``inherit_from`` value for every generated component
interface that has no explicit base in the Castle source.  It is the runtime
equivalent of the implicit Castle ``Component`` root.
"""
