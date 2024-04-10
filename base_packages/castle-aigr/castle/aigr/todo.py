# (C) Albert Mietus, 2024. Part of Castle/CCastle project

from dataclasses import dataclass
import typing as PTH

@dataclass
class mark_Dataclass:
    "Mark a (data)class that is isn't Implemented yet"
    def __post_init__(self, *t, **d):
        raise NotImplementedError(f"This {type(self)} ToDo class is't supported (yet) --sorry")

class Typing():
    """Specify the type is to be done"""
    def __new__(cls, *t, **d):
        return PTH.NewType('Todo', None)


