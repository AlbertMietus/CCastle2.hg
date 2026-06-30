# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.CC_B_Component``.

import typing as PTH
from .._debug import DebugMixIn

class CC_B_Component(DebugMixIn):
    """Base class for all generated Castle component classes.

    The RPy writer emits ``class CC_<Name>(buildin.CC_B_Component):`` for each
    Castle ``ComponentImplementation``.  This class provides the common
    infrastructure (``isa`` link to the :class:`CC_B_ComponentClass` metadata,
    and the ``_castle_init`` hook for the Castle-level initializer).

    Usage (in generated code)
    -------------------------
    ::

        class CC_MyComp(buildin.CC_B_Component):
            def __init__(self, *args):
                buildin.CC_B_Component.__init__(self, isa=cc_C_MyComp)
                self._castle_init(*args)
            def _castle_init(self, *args):
                ...  # generated Castle init body
    """

    isa: PTH.Any
    """Back-reference to the :class:`CC_B_ComponentClass` instance (the metadata)."""

    def __init__(self, isa: PTH.Any) -> None:
        """Initialise with *isa*, the component-class metadata object."""
        ...

    def _castle_init(self, *args: PTH.Any) -> None:
        """Hook called by ``__init__`` to run the Castle-level initializer.

        The RPy writer overrides this in each generated subclass with the body
        of the Castle ``init`` block.  The base implementation is a no-op.
        """
        ...

def _debug_name(self: PTH.Any) -> str:
    """Module-level standalone function (not a method of CC_B_Component).

    Note: this function takes ``self`` as a positional argument -- it appears
    to be a leftover method that was accidentally left at module scope.
    Returns a string based on ``self.isa.interface._debug_name()``.
    """
    ...
