# (C) Albert Mietus, 2025. Part of Castle/CCastle project

# This is RPYthon code!

"""This file contains a few enums, that are compatible with the same in castle.aigr.
    But rewriten (by codeAI) to become RPYTHON"""


TYPE_CHECKING = False   # A dummy flag that is False at runtime
if TYPE_CHECKING:            # Not for RPYTHON
    import typing as PTH     # type: ignore


class _RPython_Enum(object):
    _NAMES = {}  # type: dict[int, str]

    @classmethod
    def to_number(cls, val):  # type: (PTH.Any) -> int
        return int(val)

    @classmethod
    def to_string(cls, val):  # type: (PTH.Any) -> str
        return cls._NAMES.get(val, "Invalid")

    @classmethod
    def is_valid(cls, val):  # type: (PTH.Any) -> bool
        return val in cls._NAMES

    @classmethod
    def items(cls):  # type: () -> list[tuple[int, str]]
        # Useful if you want to iterate or print
        return [(k, cls._NAMES[k]) for k in sorted(cls._NAMES.keys())]

class CC_ProtocolKind(_RPython_Enum):
    Unknown = 0
    Event   = 1
    Data    = 2
    Stream  = 3
    _unset  = -1

    _NAMES = {
        _unset: "_unset",
        Unknown: "Unknown",
        Event: "Event",
        Data: "Data",
        Stream: "Stream",
    }

class CC_PortDirection(_RPython_Enum):
    Unknown = 0
    In      = 1
    Out     = 2
    BiDir   = 3
    Master  = 4
    Slave   = 5
    #Aliases
    Bidir         = BiDir
    BiDirectional = Bidir
    Bidirectional = Bidir

    _NAMES = {
        Unknown: "Unknown",
        In: "In",
        Out: "Out",
        BiDir: "BiDir", # all aliasses use this one
        Master: "Master",
        Slave: "Slave",
    }
