class AST_BASE:
    """Base class for all Castle ATS nodes"""

    def __init__(self, *, parse_tree=None, **kwargs):
        super().__init__(**kwargs)
        self._parse_tree = parse_tree


    @property
    def position(self): return self._parse_tree.position
    @property
    def position_end(self): return self._parse_tree.position_end


class IDError(ValueError):
    "The given ID is not valid as an ID"

import re

class ID(str):
    _pattern = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')

    @staticmethod
    def validate_or_raise(value):
        if not isinstance(value, str):
            raise IDError("not a str of ID")
        if ID._pattern.fullmatch(value) is None:
            raise IDError("not a valid pattern")

