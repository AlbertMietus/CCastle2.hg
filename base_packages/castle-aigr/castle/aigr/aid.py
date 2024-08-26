# (C) Albert Mietus, 2023.2024. Part of Castle/CCastle project


import typing as PTH                                       # Python TypeHints
from dataclasses import dataclass, KW_ONLY
from dataclasses import field as dc_field
from . import AIGR

""" XXX ToDo: refactor, rename & relocate ..."""


@dataclass
class TypedParameter(AIGR):
    """A parameter is a placeholder in a function/callable **definition**.
       It acts as variable inside the body In Castle, it always has a Type."""
    name: str   # XXX ToDo ``str`` or ``ID``?
    type: type  # XXX ToDo: Really `type`? A python type?

@dataclass
class Argument(AIGR):
    """An argument is a value passed during function/callable **invocation**.
       In Castle, we support both positional and named arguments. Hence, an argument can have a name."""
    value: PTH.Any
    _: KW_ONLY
    name: PTH.Optional[str]=None # XXX ToDo str or  ID?




