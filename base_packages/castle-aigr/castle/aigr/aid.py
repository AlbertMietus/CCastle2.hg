# (C) Albert Mietus, 2023. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from enum import Enum
from dataclasses import dataclass, KW_ONLY
from . import AIGR

# XXX__all__ = [

@dataclass
class TypedParameter(AIGR):
    """This is many a helper class/struct to combine a parameter: a name and an type"""
    name: str
    type: type

@dataclass
class Argument(AIGR):
    """This is many a helper class/struct to combine a argument: a value and optional a name"""
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None


