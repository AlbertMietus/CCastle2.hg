# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.machinery.chained_dict``.

import typing as PTH

class ChainedDict:
    """Read-only chained dispatch-table used in RPy generated code.

    Each ``ChainedDict`` holds *only* the event handlers defined (or
    overridden) by *this* component.  Inherited handlers live in the
    :attr:`_parent` ``ChainedDict``.  Look-up walks the chain from child to
    parent, so an overriding handler shadows the parent's entry.

    The map is built at module initialisation time by the generated code; it
    is read-only at runtime.

    Usage (in generated code)
    -------------------------
    ::

        cc_S_MyComp_clk = buildin.machinery.ChainedDict(
            map={
                'CC_P_Clock_tick': CC_MyComp.Clock_tick__clk,
            },
            parent=None,
        )

        handler = cc_S_MyComp_clk['CC_P_Clock_tick']
        handler(receiver, *args)
    """

    _parent: PTH.Optional["ChainedDict"]
    """Parent chain entry (inherited handlers), or ``None`` for the root."""
    _dict: dict[str, PTH.Any]
    """This level's own handler map (key: trigger string, value: callable)."""

    def __init__(
        self,
        map: PTH.Optional[dict[str, PTH.Any]] = ...,
        parent: PTH.Optional["ChainedDict"] = ...,
    ) -> None: ...

    def __getitem__(self, key: str) -> PTH.Any:
        """Look up *key*, walking the parent chain if not found locally.

        Raises ``KeyError`` if not found anywhere in the chain.
        """
        ...

    def __setitem__(self, key: str, value: PTH.Any) -> None:
        """Set *key* in the local dict (used only during construction/testing)."""
        ...

    def __contains__(self, key: object) -> bool:
        """Return ``True`` if *key* exists anywhere in the chain."""
        ...
