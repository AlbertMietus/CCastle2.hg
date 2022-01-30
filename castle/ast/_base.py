from .serialization import Serialize



class AST_BASE:
    """Base class for all Castle ATS nodes"""

    def __init__(self, *, parse_tree=None, **kwargs):
        assert len(kwargs)==0, "Do not call 'Object' with kwargs (caller is wrong)"
        super().__init__(**kwargs)
        self._parse_tree = parse_tree

    def __str__(self): # mostly for debugging
        return '\n__DEBUG__ ' + str(type(self).__name__) + "\n\t" + "\n\t".join(f'{n}\t{str(v)}:{type(v).__name__}' for n,v in self.__dict__.items() if n[0]!='_')

    def serialize(self, strategy="XML") -> str:
        return Serialize(strategy).serialize(self)

    @property
    def position(self): return self._parse_tree.position
    @property
    def position_end(self): return self._parse_tree.position_end

    ### Mostly for debugging
    @staticmethod
    def _typeName(of):
        return type(of).__name__

    def _valType(self, of:None):
        if not of: of=self
        return f'{of}:{self._typeName(of)}'


class IDError(ValueError):
    "The given ID is not valid as an ID"



class ID(AST_BASE):
    import re
    _pattern = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')

    @staticmethod
    def validate_or_raise(value):
        if isinstance(value, ID): return
        if not isinstance(value, str):
            raise IDError(f">>{value}<<: not a str (or an ID)")
        if ID._pattern.fullmatch(value) is None:
            raise IDError(f">>{value}<<: not a valid pattern")

    def __init__(self, *, name, **kwargs):
        super().__init__(**kwargs)
        self.validate_or_raise(name)
        if isinstance(name, ID):
            name=name.name
        self.name=name

    def __str__(self): # mostly for debugging
        return self.name
