# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_ComponentClass``.

import typing as PTH
from .._debug import DebugMixIn

class CC_B_ComponentClass(DebugMixIn):
    """Metadata descriptor for a Castle component implementation.

    One ``CC_B_ComponentClass`` instance is generated per Castle
    ``implement`` block.  It links the component to its interface
    (:class:`CC_B_ComponentInterface`) and holds method-pointer tables.

    In generated code it appears as the ``isa`` argument to
    :class:`CC_B_Component.__init__`.

    Usage (in generated code)
    -------------------------
    ::

        cc_C_MyComp = buildin.CC_B_ComponentClass(
            interface = cc_CI_MyComp,
        )
    """

    interface: PTH.Any
    """The :class:`CC_B_ComponentInterface` this implementation realises."""
    methods: list[PTH.Any]
    """List of method function-pointers (may be empty)."""
    isa: PTH.Any
    """Meta-class back-reference; currently always ``None``."""

    def __init__(
        self,
        interface: PTH.Any,
        methods: list[PTH.Any] = ...,
        isa: PTH.Any = ...,
    ) -> None: ...
