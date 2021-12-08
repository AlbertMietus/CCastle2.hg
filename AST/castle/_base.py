class AST_BASE:
    """Base class for all Castle ATS nodes"""

    def __init__(self, *, parse_tree=None):
        self._parse_tree = parse_tree

    @property
    def position(self): return self.parse_tree.position
    @property
    def position_end(self): return self.parse_tree.position_end

class ID(str): pass
