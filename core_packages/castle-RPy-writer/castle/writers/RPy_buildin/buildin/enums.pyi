# (C) Albert Mietus, 2026. CodeAI=GH.Claude.Opus-4.8
#
# Type stub for ``castle.writers.RPy_buildin.buildin.enums``.
# RPython-compatible enum classes mirroring castle.aigr enums.

import typing as PTH

class _RPython_Enum:
    """RPython-compatible base enum.

    Stores integer constants in class attributes and a ``_NAMES`` dict mapping
    integer -> string name.  All conversions are class-method calls; no Python
    ``enum.Enum`` machinery is used so the code also runs under RPython/PyPy2.
    """

    _NAMES: PTH.ClassVar[dict[int, str]]

    @classmethod
    def to_number(cls, val: PTH.Any) -> int:
        """Convert *val* (int or enum constant) to its integer representation."""
        ...

    @classmethod
    def to_string(cls, val: PTH.Any) -> str:
        """Return the string name for *val*, or ``"Invalid"`` if unknown."""
        ...

    @classmethod
    def is_valid(cls, val: PTH.Any) -> bool:
        """Return ``True`` when *val* is a known constant of this enum."""
        ...

    @classmethod
    def items(cls) -> list[tuple[int, str]]:
        """Return all ``(integer, name)`` pairs sorted by integer value."""
        ...


class CC_ProtocolKind(_RPython_Enum):
    """Protocol-kind discriminator (mirrors ``castle.aigr.ProtocolKind``).

    Constants
    ---------
    Unknown = 0
    Event   = 1
    Data    = 2
    Stream  = 3
    _unset  = -1
    """

    Unknown: PTH.ClassVar[int]
    Event:   PTH.ClassVar[int]
    Data:    PTH.ClassVar[int]
    Stream:  PTH.ClassVar[int]
    _unset:  PTH.ClassVar[int]
    _NAMES:  PTH.ClassVar[dict[int, str]]


class CC_PortDirection(_RPython_Enum):
    """Port-direction discriminator (mirrors ``castle.aigr.PortDirection``).

    Constants
    ---------
    Unknown = 0, In = 1, Out = 2, BiDir = 3, Master = 4, Slave = 5.
    ``Bidir``, ``BiDirectional``, ``Bidirectional`` are aliases for ``BiDir``.
    """

    Unknown:        PTH.ClassVar[int]
    In:             PTH.ClassVar[int]
    Out:            PTH.ClassVar[int]
    BiDir:          PTH.ClassVar[int]
    Master:         PTH.ClassVar[int]
    Slave:          PTH.ClassVar[int]
    Bidir:          PTH.ClassVar[int]
    BiDirectional:  PTH.ClassVar[int]
    Bidirectional:  PTH.ClassVar[int]
    _NAMES:         PTH.ClassVar[dict[int, str]]
