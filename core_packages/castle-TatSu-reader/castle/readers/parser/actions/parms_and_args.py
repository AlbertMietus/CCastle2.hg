# (C) Albert Mietus, 2025. Part of Castle/CCastle project
from castle import aigr

class ParmsArgs():
    def parameter(self, ast):
        return aigr.TypedParameter(name=ast.name, type=ast.type) #XXX type: str OR aigr.type.string?
